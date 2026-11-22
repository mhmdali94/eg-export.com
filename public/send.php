<?php
/*
 * EGE contact form handler.
 * Receives the enquiry form (contact.html in en/fr/ar), sends it by Gmail SMTP,
 * then redirects to thanks.html or sorry.html in the visitor's language.
 * Settings and password live in mail-config.php OUTSIDE public_html (see tools/README.md).
 */
declare(strict_types=1);

const LANGS = ['en', 'fr', 'ar'];

function back(string $lang, bool $ok): void
{
    $prefix = $lang === 'en' ? '' : $lang . '/';
    header('Location: ' . $prefix . ($ok ? 'thanks.html' : 'sorry.html'), true, 303);
    exit;
}

function field(string $name, int $max): string
{
    $v = isset($_POST[$name]) && is_string($_POST[$name]) ? trim($_POST[$name]) : '';
    $v = str_replace("\0", '', $v);
    return mb_substr($v, 0, $max, 'UTF-8');
}

function one_line(string $v): string
{
    return trim(preg_replace('/[\r\n\t]+/', ' ', $v) ?? '');
}

function enc_header(string $text): string
{
    return '=?UTF-8?B?' . base64_encode($text) . '?=';
}

/** Minimal SMTP client (AUTH LOGIN over SSL 465 or STARTTLS 587). Pass $to = [] to only test the login. */
function smtp_send(array $cfg, array $to, string $subject, string $body, string $replyEmail = '', string $replyName = ''): void
{
    $port = (int) $cfg['smtp_port'];
    $remote = ($port === 465 ? 'ssl://' : 'tcp://') . $cfg['smtp_host'] . ':' . $port;
    $ctx = stream_context_create(['ssl' => ['verify_peer' => true, 'verify_peer_name' => true]]);
    $fp = @stream_socket_client($remote, $errno, $errstr, 20, STREAM_CLIENT_CONNECT, $ctx);
    if (!$fp) {
        throw new RuntimeException("SMTP connect failed ($errno): $errstr");
    }
    stream_set_timeout($fp, 20);

    $read = function () use ($fp): string {
        $data = '';
        while (($line = fgets($fp, 515)) !== false) {
            $data .= $line;
            if (strlen($line) < 4 || $line[3] === ' ') {
                break;
            }
        }
        return $data;
    };
    // $label is what appears in error messages, so credentials never reach the logs.
    $cmd = function (?string $line, $expect, string $label) use ($fp, $read): string {
        if ($line !== null) {
            fwrite($fp, $line . "\r\n");
        }
        $reply = $read();
        if (!in_array((int) substr($reply, 0, 3), (array) $expect, true)) {
            throw new RuntimeException("SMTP $label failed: " . trim($reply));
        }
        return $reply;
    };

    $helo = 'EHLO ' . (preg_replace('/[^A-Za-z0-9.\-]/', '', (string) ($_SERVER['SERVER_NAME'] ?? '')) ?: 'localhost');
    $cmd(null, 220, 'greeting');
    $cmd($helo, 250, 'EHLO');
    if ($port === 587) {
        $cmd('STARTTLS', 220, 'STARTTLS');
        if (!stream_socket_enable_crypto($fp, true, STREAM_CRYPTO_METHOD_TLS_CLIENT)) {
            throw new RuntimeException('SMTP TLS negotiation failed');
        }
        $cmd($helo, 250, 'EHLO after TLS');
    }
    $cmd('AUTH LOGIN', 334, 'AUTH');
    $cmd(base64_encode($cfg['smtp_user']), 334, 'AUTH user');
    $cmd(base64_encode($cfg['smtp_pass']), 235, 'AUTH password');

    if ($to) {
        $cmd('MAIL FROM:<' . $cfg['smtp_user'] . '>', 250, 'MAIL FROM');
        foreach ($to as $rcpt) {
            $cmd('RCPT TO:<' . $rcpt . '>', [250, 251], 'RCPT TO');
        }
        $cmd('DATA', 354, 'DATA');

        $headers = [
            'Date: ' . date('r'),
            'From: ' . enc_header($cfg['from_name']) . ' <' . $cfg['smtp_user'] . '>',
            'To: ' . implode(', ', array_map(fn($a) => '<' . $a . '>', $to)),
            'Subject: ' . enc_header($subject),
            'Message-ID: <' . bin2hex(random_bytes(12)) . '@' . substr(strrchr($cfg['smtp_user'], '@'), 1) . '>',
            'MIME-Version: 1.0',
            'Content-Type: text/plain; charset=UTF-8',
            'Content-Transfer-Encoding: base64',
        ];
        if ($replyEmail !== '') {
            $headers[] = 'Reply-To: ' . ($replyName !== '' ? enc_header($replyName) . ' ' : '') . '<' . $replyEmail . '>';
        }
        $data = implode("\r\n", $headers) . "\r\n\r\n" . rtrim(chunk_split(base64_encode($body), 76, "\r\n")) . "\r\n.";
        $cmd($data, 250, 'message');
    }
    $cmd('QUIT', 221, 'QUIT');
    fclose($fp);
}

function load_config(): ?array
{
    foreach ([dirname(__DIR__) . '/mail-config.php', dirname(__DIR__) . '/server/mail-config.php'] as $path) {
        if (is_file($path)) {
            $cfg = require $path;
            return is_array($cfg) ? $cfg : null;
        }
    }
    return null;
}

/** Simple per-IP limit, stored in the system temp folder. */
function rate_limited(int $max): bool
{
    $ip = (string) ($_SERVER['REMOTE_ADDR'] ?? 'unknown');
    $file = sys_get_temp_dir() . '/ege-form-' . hash('sha256', $ip);
    $now = time();
    $hits = is_file($file) ? (json_decode((string) file_get_contents($file), true) ?: []) : [];
    $hits = array_values(array_filter($hits, fn($t) => is_int($t) && $t > $now - 3600));
    if (count($hits) >= $max) {
        return true;
    }
    $hits[] = $now;
    @file_put_contents($file, json_encode($hits), LOCK_EX);
    return false;
}

// --------------------------------------------------------------------------- main
if (PHP_SAPI === 'cli' && ($argv[1] ?? '') === '--check-login') {
    // Local test: php public/send.php --check-login   (logs in to Gmail, sends nothing)
    $cfg = load_config();
    if (!$cfg) {
        fwrite(STDERR, "mail-config.php not found\n");
        exit(1);
    }
    smtp_send($cfg, [], '', '');
    echo "SMTP login OK for {$cfg['smtp_user']} via {$cfg['smtp_host']}:{$cfg['smtp_port']}\n";
    exit(0);
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Location: contact.html', true, 303);
    exit;
}

$lang = in_array($_POST['lang'] ?? '', LANGS, true) ? $_POST['lang'] : 'en';

// Honeypot: real visitors never see or fill this field. Pretend success to bots.
if (field('website', 200) !== '') {
    back($lang, true);
}

$name     = one_line(field('name', 120));
$company  = one_line(field('company', 160));
$email    = one_line(field('email', 200));
$phone    = one_line(field('phone', 60));
$country  = one_line(field('country', 100));
$product  = one_line(field('product', 120));
$quantity = one_line(field('quantity', 200));
$message  = field('message', 5000);

$valid = $name !== ''
    && filter_var($email, FILTER_VALIDATE_EMAIL) !== false
    && $product !== ''
    && $message !== ''
    && preg_match_all('~https?://~i', $message) <= 3;

if (!$valid) {
    back($lang, false);
}

$cfg = load_config();
if (!$cfg) {
    error_log('EGE form: mail-config.php not found (expected one level above public_html)');
    back($lang, false);
}
if (rate_limited((int) ($cfg['max_per_hour'] ?? 5))) {
    back($lang, false);
}

$langName = ['en' => 'English', 'fr' => 'French', 'ar' => 'Arabic'][$lang];
$subject = "Website enquiry: $product — $name";
$body = "New enquiry from the website contact form\n"
    . str_repeat('-', 44) . "\n"
    . "Name:      $name\n"
    . "Company:   " . ($company ?: '-') . "\n"
    . "Email:     $email\n"
    . "Phone:     " . ($phone ?: '-') . "\n"
    . "Country:   " . ($country ?: '-') . "\n"
    . "Product:   $product\n"
    . "Quantity:  " . ($quantity ?: '-') . "\n"
    . "Language:  $langName\n"
    . str_repeat('-', 44) . "\n\n"
    . $message . "\n\n"
    . str_repeat('-', 44) . "\n"
    . 'Sent ' . date('Y-m-d H:i T') . ' from ' . ($_SERVER['HTTP_HOST'] ?? 'website') . ". Reply to this email to answer the customer.\n";

try {
    smtp_send($cfg, (array) $cfg['to'], $subject, $body, $email, $name);
    back($lang, true);
} catch (Throwable $e) {
    error_log('EGE form: ' . $e->getMessage());
    back($lang, false);
}
