<?php
/*
 * EGE contact form — mail settings TEMPLATE. Copy to mail-config.php and fill in the password.
 *
 * Upload this file ONE LEVEL ABOVE public_html, e.g. /home/eg-export.com/mail-config.php
 * (never inside public_html, never in the site zip).
 * Even if it ended up inside public_html by mistake, opening it in a browser shows a blank page:
 * it only returns an array and prints nothing.
 */
return [
    // Gmail SMTP. 465 = SSL (default). If your host blocks 465, try 587 (STARTTLS).
    'smtp_host' => 'smtp.gmail.com',
    'smtp_port' => 465,
    'smtp_user' => 'your-account@gmail.com',
    'smtp_pass' => 'your-16-letter-app-password',   // Gmail app password (no spaces)

    // Shown as the sender name. Gmail always sends from smtp_user.
    'from_name' => 'EGE Website',

    // Who receives the enquiries. Add more addresses if needed.
    'to' => ['info@eg-export.com'],

    // Anti-spam: max submissions per visitor IP per hour.
    'max_per_hour' => 5,
];
