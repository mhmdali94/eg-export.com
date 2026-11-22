# Site generator

The website in `public/` is plain static HTML. You can edit those files by hand.
This generator is optional: it rebuilds all 48 pages (English, French and Arabic) when you'd
rather change something once than in 48 files (header, footer, product copy, contact details).

**Running it overwrites every `.html` file in `public/`**, so hand edits made to those files
are lost. Make lasting changes here, then rerun.

## Run

From the project root (macOS's built-in Python 3.9 works; nothing to install):

```bash
python3 tools/build.py
```

It writes:
- `public/**/*.html`: English pages at the root, French under `public/fr/`, Arabic under `public/ar/`
- `public/sitemap.xml` and `public/robots.txt`
- `data/products.json` → `ege_description` (the final EN, FR and AR copy shown on each product page)

## Where to change things

| What | File | Where |
|---|---|---|
| Product copy (EN + AR), applications, benefits, packaging | `tools/content.py` | `PRODUCTS` |
| French copy (all pages) | `tools/content.py` | `FR` (keyed by the English text), `SPEC_*_FR` |
| Spec values | `data/products.json` | `specifications` (copied exactly) |
| Hide a spec row (e.g. pH) | `tools/build.py` | `HIDE_SPEC_KEYS` |
| Replace a product photo with the placeholder | `tools/build.py` | `HIDE_IMAGES` |
| Phone, email, address, WhatsApp | `tools/build.py` | constants at the top |
| Google Map | `tools/build.py` | `MAP_EMBED_HTML` (paste the full `<iframe>` code) |
| Header, footer, page layouts, UI wording | `tools/build.py` | `header()`, `footer()`, page functions, `T` |
| Styling | `public/css/style.css` | not generated; edit directly |

`public/css/style.css`, `public/js/main.js` and the images are never touched by the generator.

## French

French text lives in `FR` in `tools/content.py`, keyed by the exact English text. If you change an
English string, update its key in `FR` as well. The build stops and lists any English text with no
French version, so nothing silently falls back to English.

## Contact form (PHP)

The enquiry form on `contact.html` (all languages) posts to `public/send.php`, which sends the
message through Gmail SMTP and redirects to `thanks.html` or `sorry.html` in the visitor's language.

- Settings and the Gmail app password are in `server/mail-config.php`. **Never put this file in
  `public/` or in the upload zip.** On CyberPanel, upload it one level above `public_html`:
  `/home/eg-export.com/mail-config.php`.
- Recipients: `'to'` in `mail-config.php`. Replies go straight to the customer (Reply-To).
- Test the Gmail login without sending anything: `php public/send.php --check-login`
- If the host blocks port 465, set `'smtp_port' => 587`.
- Spam protection: hidden honeypot field, max 5 submissions per IP per hour, max 3 links per message.
- Errors are written to the PHP error log (prefixed `EGE form:`); the password is never logged.
