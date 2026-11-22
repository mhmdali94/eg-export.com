"""Generator for the EGE static site. See tools/README.md.

Reads data/products.json + tools/content.py and writes plain .html files into public/.
It also writes the final page copy back into data/products.json -> ege_description.
The live site has no dependency on this script or on the JSON.

Usage (from the project root):  python3 tools/build.py
"""
import sys, os, json, html
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import (PRODUCTS, PACK, SPEC_KEY_AR, SPEC_NOTE_AR, SPEC_VALUE_AR,
                     FR, NB, SPEC_KEY_FR, SPEC_NOTE_FR, SPEC_VALUE_FR)

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public")
DATA = json.load(open(os.path.join(ROOT, "data", "products.json"), encoding="utf-8"))
SRC = {p["source"]["slug"]: p for p in DATA["products"]}

DOMAIN = "https://eg-export.com"
PHONE_DISPLAY = "+20 104 044 0090"
PHONE_TEL = "+201040440090"
WA_NUMBER = "201040440090"
EMAIL = "info@eg-export.com"
ADDRESS = ("Osama Mutair Mall, El Qantara West, Ismailia, Egypt", "القنطرة غرب - مول أسامة مطير - الإسماعيلية - مصر",
           "Mall Osama Mutair, El Qantara Ouest, Ismaïlia, Égypte")
MAP_Q = "Osama Mutair Mall, El Qantara West, Ismailia, Egypt"
# Exact pin from the company's Google Maps link (https://maps.app.goo.gl/CrrjcH7WSjjrFcHJ8)
MAP_LAT, MAP_LNG = "30.854079", "32.3136176"
MAP_LINK = "https://maps.app.goo.gl/CrrjcH7WSjjrFcHJ8"

# Google Maps embed. Paste the full <iframe ...></iframe> code from Google Maps
# (Share -> Embed a map) between the triple quotes to use it on both contact pages.
# Leave empty to use the address-search map built from MAP_Q.
MAP_EMBED_HTML = """"""

# Spec rows hidden on the site until their values are confirmed (kept in products.json).
HIDE_SPEC_KEYS = {"pH Level"}

# Products whose main photo is replaced by a neutral placeholder.
# The listed source images are left out of the site entirely (kept in data/original-images/).
PLACEHOLDER = {"file": "/images/placeholders/product-placeholder.svg", "width": 1600, "height": 1200}
HIDE_IMAGES = {"water-softening-tablet-salt": {"water-softening-tablet-salt-hero.jpg"}}

# Photo used on product cards (home, products page, "Other products"), when not the main photo.
CARD_IMAGE = {"water-softening-tablet-salt": "water-softening-tablet-salt-variant-2.jpg"}
YEAR = "2026"

e = html.escape


# Languages: English at the site root, the others in a sub-folder.
LANGS = ["en", "fr", "ar"]
LANG_LABEL = {"en": "EN", "fr": "FR", "ar": "العربية"}
LANG_NAME = {"en": "English", "fr": "Français", "ar": "العربية"}
OG_LOCALE = {"en": "en_US", "fr": "fr_FR", "ar": "ar_EG"}
RTL = {"ar"}
MISSING_FR = []


def tr(lang, en, ar, fr=None):
    """Pick the text for `lang`. French comes from `fr` if given, otherwise from the FR dictionary (content.py)."""
    if lang == "en":
        return en
    if lang == "ar":
        return ar
    if fr is not None:
        return fr
    if en not in FR:
        MISSING_FR.append(en)
        return en
    return FR[en]


def L(lang, pair):
    return tr(lang, pair[0], pair[1], pair[2] if len(pair) > 2 else None)


def spec_text(lang, kind, value):
    maps = {"key": (SPEC_KEY_AR, SPEC_KEY_FR), "note": (SPEC_NOTE_AR, SPEC_NOTE_FR), "value": (SPEC_VALUE_AR, SPEC_VALUE_FR)}[kind]
    if lang == "en":
        return value
    return (maps[0] if lang == "ar" else maps[1]).get(value, value)


# ---------------------------------------------------------------- UI strings
T = {
    "brand": ("Egyptian Global Export", "المصرية العالمية للتصدير"),
    "brand_short": ("EGE", "EGE"),
    "nav_home": ("Home", "الرئيسية"), "nav_products": ("Products", "المنتجات"), "nav_about": ("About", "من نحن"),
    "nav_faq": ("FAQ", "الأسئلة الشائعة"), "nav_contact": ("Contact", "تواصل معنا"),
    "quote": ("Request a Quote", "اطلب عرض سعر"),
    "quote_on_wa": ("Request a Quote on WhatsApp", "اطلب عرض سعر عبر واتساب"),
    "email_us": ("Email us", "راسلنا بالبريد"),
    "menu": ("Menu", "القائمة"),
    "skip": ("Skip to content", "انتقل إلى المحتوى"),
    "lang_switch": ("Language", "اللغة", "Langue"),
    # enquiry form (contact page) + result pages
    "form_eyebrow": ("Enquiry form", "نموذج الاستفسار", "Formulaire de demande"),
    "form_title": ("Send us an enquiry", "أرسل لنا استفسارك", "Envoyez-nous votre demande"),
    "form_intro": ("Fill in the form and we'll reply by email. Fields marked * are required.",
                   "املأ النموذج وسنرد عليك عبر البريد الإلكتروني. الحقول المعلَّمة بـ * إلزامية.",
                   "Remplissez le formulaire, nous vous répondrons par e-mail. Les champs suivis d'un astérisque (*) sont obligatoires."),
    "form_include": ("Helpful details to include", "تفاصيل تساعدنا على الرد بسرعة", "Informations utiles à préciser"),
    "f_name": ("Full name", "الاسم الكامل", "Nom et prénom"),
    "f_company": ("Company", "الشركة", "Société"),
    "f_email": ("Email", "البريد الإلكتروني", "E-mail"),
    "f_phone": ("Phone / WhatsApp", "الهاتف / واتساب", "Téléphone / WhatsApp"),
    "f_country": ("Country", "الدولة", "Pays"),
    "f_product": ("Product", "المنتج", "Produit"),
    "f_choose": ("Select a product", "اختر منتجاً", "Choisissez un produit"),
    "f_other": ("Other / several products", "أخرى / عدة منتجات", "Autre / plusieurs produits"),
    "f_quantity": ("Quantity and packaging", "الكمية والتعبئة", "Quantité et conditionnement"),
    "f_quantity_ph": ("e.g. 500 t in big bags", "مثال: 500 طن في أكياس جامبو", "ex. 500 t en big bags"),
    "f_message": ("Message", "الرسالة", "Message"),
    "f_message_ph": ("Grade, destination port, delivery date, specification requirements…",
                     "الدرجة، ميناء الوصول، موعد التسليم، متطلبات المواصفات…",
                     "Qualité, port de destination, date de livraison, exigences techniques…"),
    "f_privacy": ("We only use your details to reply to your enquiry.", "نستخدم بياناتك فقط للرد على استفسارك.",
                  "Vos coordonnées servent uniquement à répondre à votre demande."),
    "f_submit": ("Send enquiry", "إرسال الاستفسار", "Envoyer la demande"),
    "f_or_wa": ("Prefer WhatsApp?", "تفضّل واتساب؟", f"Vous préférez WhatsApp{NB}?"),
    "required": ("required", "إلزامي", "obligatoire"),
    "thanks_title": ("Thank you", "شكراً لك", "Merci"),
    "thanks_h": ("Your enquiry has been sent", "تم إرسال استفسارك", "Votre demande a bien été envoyée"),
    "thanks_p": ("Thank you for contacting Egyptian Global Export. We've received your message and will reply by email as soon as possible.",
                 "شكراً لتواصلك مع المصرية العالمية للتصدير. استلمنا رسالتك وسنرد عليك عبر البريد الإلكتروني في أقرب وقت ممكن.",
                 "Merci d'avoir contacté Egyptian Global Export. Nous avons bien reçu votre message et vous répondrons par e-mail dans les meilleurs délais."),
    "sorry_title": ("Message not sent", "لم يتم إرسال الرسالة", "Message non envoyé"),
    "sorry_h": ("Sorry, your message could not be sent", "عذراً، تعذّر إرسال رسالتك", "Désolés, votre message n'a pas pu être envoyé"),
    "sorry_p": ("Please check your details and try again, or contact us directly on WhatsApp or by email.",
                "يُرجى التحقق من بياناتك والمحاولة مرة أخرى، أو التواصل معنا مباشرة عبر واتساب أو البريد الإلكتروني.",
                "Vérifiez vos informations et réessayez, ou contactez-nous directement sur WhatsApp ou par e-mail."),
    "back_home": ("Back to home", "العودة إلى الرئيسية", "Retour à l'accueil"),
    "back_form": ("Back to the form", "العودة إلى النموذج", "Retour au formulaire"),
    "tagline": ("Made in Egypt • Exported Worldwide", "صُنع في مصر • يُصدَّر إلى العالم"),
    "wa_float": ("Chat with us on WhatsApp", "تحدث معنا عبر واتساب"),
    "wa_general": ("Hello, I'd like to know more about your salt products.", "مرحباً، أود معرفة المزيد عن منتجات الملح لديكم."),
    "wa_quote_tpl": ("Hello, I'd like a quote for {p}", "مرحباً، أرغب في الحصول على عرض سعر لـ {p}", "Bonjour, je souhaite un devis pour le {p}"),
    "wa_quote_general": ("Hello, I'd like a quote for your salt products.", "مرحباً، أرغب في الحصول على عرض سعر لمنتجات الملح لديكم."),
    "view_product": ("View product", "عرض المنتج"),
    "all_products": ("All products", "جميع المنتجات"),
    "footer_about": ("Egyptian Global Export supplies industrial, food, de-icing and specialty salt from Egypt to buyers around the world.",
                     "تورّد المصرية العالمية للتصدير الملح الصناعي والغذائي وملح إذابة الجليد والأملاح المتخصصة من مصر إلى المشترين حول العالم."),
    "footer_products": ("Products", "المنتجات"), "footer_company": ("Company", "الشركة"), "footer_contact": ("Contact", "تواصل معنا"),
    "rights": ("All rights reserved.", "جميع الحقوق محفوظة."),
    # product page
    "overview": ("Overview", "نظرة عامة"),
    "specs": ("Technical specifications", "المواصفات الفنية"),
    "specs_sub": ("Typical values", "القيم المعتادة"),
    "specs_none": ("Detailed specifications for this product are available on request. Tell us your application and we'll share the right grade and analysis.",
                   "المواصفات التفصيلية لهذا المنتج متاحة عند الطلب. أخبرنا باستخدامك وسنرسل لك الدرجة والتحليل المناسبين."),
    "specs_request": ("Ask for specifications", "اطلب المواصفات"),
    "wa_specs_tpl": ("Hello, could you send the technical specifications for {p}?", "مرحباً، هل يمكنكم إرسال المواصفات الفنية لـ {p}؟",
                     f"Bonjour, pourriez-vous m'envoyer les caractéristiques techniques du {{p}}{NB}?"),
    "grades": ("Grades and types", "الأنواع والدرجات"),
    "grades_sub": ("Choose the type that fits your application.", "اختر النوع المناسب لاستخدامك."),
    "applications": ("Applications", "الاستخدامات"),
    "benefits": ("Key benefits", "أهم المزايا"),
    "packaging": ("Packaging options", "خيارات التعبئة"),
    "packaging_sub": ("Packed to suit your order size and handling.", "تعبئة تناسب حجم طلبك وطريقة تداوله."),
    "packaging_request": ("Packaging options for this product are confirmed with your quote.", "يتم تأكيد خيارات التعبئة لهذا المنتج مع عرض السعر."),
    "packaging_quick": ("Bags, big bags or bulk", "أكياس أو أكياس جامبو أو سائب"),
    "gallery": ("Product photos", "صور المنتج"),
    "related": ("Other products", "منتجات أخرى"),
    "cta_title": ("Ready to order {p}?", "هل ترغب في طلب {p}؟", f"Vous souhaitez commander du {{p}}{NB}?"),
    "cta_text": ("Send us the grade, quantity, packaging and destination port, and we'll come back with a quote.",
                 "أرسل لنا النوع والكمية وطريقة التعبئة وميناء الوصول، وسنرد عليك بعرض سعر."),
    "cta_title_general": ("Let's talk about your next shipment", "لنتحدث عن شحنتك القادمة"),
    "cta_text_general": ("Tell us what you need, how much and where it's going. We'll reply with options and a quote.",
                         "أخبرنا بما تحتاجه والكمية ووجهة الشحن، وسنرد عليك بالخيارات وعرض السعر."),
}


# ---------------------------------------------------------------- icons
def icon(name):
    paths = {
        "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
        "close": '<path d="M6 6l12 12M18 6L6 18"/>',
        "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
        "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
        "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
        "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
        "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
        "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
        "bag": '<path d="M6 7h12l1 14H5L6 7z"/><path d="M9 7V5a3 3 0 0 1 6 0v2"/>',
        "bigbag": '<path d="M5 8h14v12a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V8z"/><path d="M7 8l1-4M17 8l-1-4M8 4h8"/>',
        "truck": '<path d="M3 6h11v10H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
        "ship": '<path d="M3 17l2 3h14l2-3H3z"/><path d="M5 17V11h14v6M9 11V6h6v5M12 3v3"/>',
        "layers": '<path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5"/>',
        "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6l8-3z"/><path d="M8.5 12l2.5 2.5 4.5-4.5"/>',
        "chat": '<path d="M4 5h16v11H8l-4 4V5z"/><path d="M8 10h8M8 13h5"/>',
        "drop": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>',
        "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M18.4 5.6l-2.8 2.8M8.4 15.6l-2.8 2.8"/>',
        "flask": '<path d="M9 3h6M10 3v6L4.5 19a1.5 1.5 0 0 0 1.3 2h12.4a1.5 1.5 0 0 0 1.3-2L14 9V3"/><path d="M7 15h10"/>',
        "gauge": '<path d="M4 18a8 8 0 1 1 16 0"/><path d="M12 18l4-6"/>',
    }
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[name]}</svg>')


WA_SVG = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97'
          '-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.64.07-.3-.15-1.26-.46-2.4-1.48-.88-.79-1.48-1.76-1.65-2.06'
          '-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.6-.92-2.2-.24-.58-.49-.5'
          '-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.08.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49'
          ' 1.7.62.71.23 1.36.2 1.87.12.57-.08 1.76-.72 2-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35M12.04 21.5h-.01a9.45 9.45'
          ' 0 0 1-4.82-1.32l-.35-.2-3.58.93.96-3.49-.23-.36a9.42 9.42 0 0 1-1.45-5.03c0-5.21 4.25-9.45 9.48-9.45 2.53 0 4.9.99 6.7 2.78'
          'a9.38 9.38 0 0 1 2.77 6.68c0 5.21-4.25 9.46-9.47 9.46M20.1 3.9A11.32 11.32 0 0 0 12.04.55C5.76.55.65 5.66.65 11.93c0 2'
          '.52 3.88 1.62 5.68L.54 23.45l5.97-1.57a11.36 11.36 0 0 0 5.53 1.41c6.28 0 11.39-5.11 11.4-11.38 0-3.04-1.18-5.9-3.34-8.01"/></svg>')


def wa(text):
    return f"https://wa.me/{WA_NUMBER}?text={quote(text)}"


# ---------------------------------------------------------------- paths
def prefix(lang):
    return "" if lang == "en" else lang + "/"


def up(lang, cur):
    return "../" * (cur.count("/") + (0 if lang == "en" else 1))


def rel(lang, cur, target):
    """Relative URL from page `cur` (path within a language tree) to `target` in the same language."""
    return up(lang, cur) + prefix(lang) + target


def asset(lang, cur, target):
    return up(lang, cur) + target


def lang_url(lang, cur, to):
    """Relative URL from page `cur` in `lang` to the SAME page in language `to`."""
    return up(lang, cur) + prefix(to) + cur


def abs_url(lang, cur):
    p = prefix(lang) + cur
    return f"{DOMAIN}/{p.replace('index.html', '')}"


def lang_switch(lang, cur):
    items = []
    for to in LANGS:
        if to == lang:
            items.append(f'<span lang="{to}" aria-current="true" title="{LANG_NAME[to]}">{LANG_LABEL[to]}</span>')
        else:
            items.append(f'<a href="{lang_url(lang, cur, to)}" lang="{to}" hreflang="{to}" title="{LANG_NAME[to]}">{LANG_LABEL[to]}</a>')
    return f'<nav class="lang-switch" aria-label="{L(lang, T["lang_switch"])}">' + "".join(items) + "</nav>"


# ---------------------------------------------------------------- layout
NAV = [("index.html", "nav_home"), ("products.html", "nav_products"), ("about.html", "nav_about"),
       ("faq.html", "nav_faq"), ("contact.html", "nav_contact")]


def header(lang, cur, active):
    t = lambda k: L(lang, T[k])
    current = ' aria-current="page"'
    items = "\n".join(
        f'          <li><a href="{rel(lang, cur, href)}"{current if href == active else ""}>{t(key)}</a></li>'
        for href, key in NAV)
    return f'''<a class="skip-link" href="#main">{t("skip")}</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="{rel(lang, cur, "index.html")}" aria-label="{e(t("brand"))} — {t("nav_home")}">
      <img src="{asset(lang, cur, "images/brand/ege-logo.png")}" alt="{e(t("brand"))} (EGE)" width="221" height="100">
    </a>
    <nav class="site-nav" id="site-nav" aria-label="{t("menu")}">
      <ul>
{items}
      </ul>
      <div class="nav-actions">
        <a class="btn btn-primary" href="{quote_href(lang, cur)}">{t("quote")}</a>
      </div>
    </nav>
    {lang_switch(lang, cur)}
    <a class="btn btn-primary header-cta" href="{quote_href(lang, cur)}">{t("quote")}</a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="{t("menu")}">
      <span class="icon-open">{icon("menu")}</span><span class="icon-close">{icon("close")}</span>
    </button>
  </div>
</header>'''


def footer(lang, cur):
    t = lambda k: L(lang, T[k])
    prods = "\n".join(f'          <li><a href="{rel(lang, cur, "products/" + p["slug"] + ".html")}">{e(L(lang, p["name"]))}</a></li>'
                      for p in PRODUCTS)
    company = "\n".join(f'          <li><a href="{rel(lang, cur, h)}">{t(k)}</a></li>' for h, k in NAV)
    return f'''<footer class="site-footer">
  <div class="container footer-top">
    <div class="footer-brand">
      <a class="logo-chip" href="{rel(lang, cur, "index.html")}"><img src="{asset(lang, cur, "images/brand/ege-logo.png")}" alt="{e(t("brand"))} (EGE)" width="221" height="100" loading="lazy"></a>
      <p>{t("footer_about")}</p>
    </div>
    <div>
      <h3>{t("footer_company")}</h3>
      <ul>
{company}
      </ul>
    </div>
    <div>
      <h3>{t("footer_products")}</h3>
      <ul>
{prods}
      </ul>
    </div>
    <div>
      <h3>{t("footer_contact")}</h3>
      <ul class="footer-contact">
        <li>{icon("phone")}<a href="tel:{PHONE_TEL}"><span class="ltr">{PHONE_DISPLAY}</span></a></li>
        <li>{icon("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{icon("pin")}<span>{e(L(lang, ADDRESS))}</span></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>© {YEAR} {t("brand")} (EGE). {t("rights")}</span>
    <span class="footer-tagline">{t("tagline")}</span>
  </div>
</footer>
<a class="wa-float" href="{wa(t("wa_general"))}" target="_blank" rel="noopener" aria-label="{t("wa_float")}" title="{t("wa_float")}">{WA_SVG}</a>
<script src="{asset(lang, cur, "js/main.js")}" defer></script>'''


def page(lang, cur, active, title, desc, body, og_image="images/products/de-icing-salt/de-icing-salt-gallery-2.jpg", noindex=False):
    dir_ = "rtl" if lang in RTL else "ltr"
    fonts = ("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Montserrat:wght@600;700;800&family=Cairo:wght@600;700&display=swap"
             if lang != "ar" else
             "https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800&family=Montserrat:wght@700&display=swap")
    brand = L(lang, T["brand"])
    full_title = f"{title} | {brand} (EGE)" if active != "index.html" or cur != "index.html" else title
    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{dir_}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">{chr(10) + '<meta name="robots" content="noindex">' if noindex else ""}
<link rel="canonical" href="{abs_url(lang, cur)}">
{"".join(f'<link rel="alternate" hreflang="{x}" href="{abs_url(x, cur)}">' + chr(10) for x in LANGS)}<link rel="alternate" hreflang="x-default" href="{abs_url("en", cur)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(brand)} (EGE)">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{abs_url(lang, cur)}">
<meta property="og:image" content="{DOMAIN}/{og_image}">
<meta property="og:locale" content="{OG_LOCALE[lang]}">
<meta name="theme-color" content="#03205b">
<link rel="icon" type="image/png" href="{asset(lang, cur, "images/brand/ege-icon.png")}">
<link rel="apple-touch-icon" href="{asset(lang, cur, "images/brand/ege-icon.png")}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<link rel="stylesheet" href="{asset(lang, cur, "css/style.css")}">
</head>
<body>
{header(lang, cur, active)}
<main id="main">
{body}
</main>
{footer(lang, cur)}
</body>
</html>
'''


# ---------------------------------------------------------------- helpers
def imgs(p):
    hidden = HIDE_IMAGES.get(p["slug"], set())
    return [im for im in SRC[p["src"]]["images"] if im["file"].rsplit("/", 1)[-1] not in hidden]


def main_image(p):
    return PLACEHOLDER if p["slug"] in HIDE_IMAGES else imgs(p)[0]


def img_tag(lang, cur, im, alt, lazy=True, cls=""):
    load = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    klass = ' class="%s"' % cls if cls else ""
    return (f'<img src="{asset(lang, cur, im["file"].lstrip("/"))}" alt="{e(alt)}" width="{im["width"]}" height="{im["height"]}"'
            f'{load}{klass}>')


def card_image(p):
    ims = imgs(p)
    # de-icing hero is a ship-loading shot; use the closer product shot for the card
    if p["slug"] in CARD_IMAGE:
        return next(x for x in ims if x["file"].endswith(CARD_IMAGE[p["slug"]]))
    if p["slug"] in HIDE_IMAGES:
        return PLACEHOLDER
    pref = {"de-icing-salt": 3}.get(p["slug"], 0)
    return ims[pref] if pref < len(ims) else ims[0]


def product_card(lang, cur, p):
    return f'''      <a class="product-card" href="{rel(lang, cur, "products/" + p["slug"] + ".html")}">
        <div class="media">{img_tag(lang, cur, card_image(p), L(lang, p["name"]))}</div>
        <div class="body">
          <span class="tag">{e(L(lang, p["tag"]))}</span>
          <h3>{e(L(lang, p["name"]))}</h3>
          <p>{e(L(lang, p["card"]))}</p>
          <span class="more">{L(lang, T["view_product"])} {icon("arrow")}</span>
        </div>
      </a>'''


def quote_href(lang, cur):
    """Every "Request a Quote" button opens the enquiry form on the contact page."""
    return rel(lang, cur, "contact.html") + "#enquiry"


def cta_band(lang, cur, title, text, label=None):
    return f'''<section class="section-tight">
  <div class="container">
    <div class="cta-band">
      <div>
        <h2>{e(title)}</h2>
        <p>{e(text)}</p>
      </div>
      <div class="btn-row">
        <a class="btn btn-primary" href="{quote_href(lang, cur)}">{icon("mail")}{label or L(lang, T["quote"])}</a>
        <a class="btn btn-ghost-light" href="mailto:{EMAIL}">{icon("mail")}{L(lang, T["email_us"])}</a>
      </div>
    </div>
  </div>
</section>'''


def get_specs(p):
    """Return [(key, value, note)] copied exactly from the imported data."""
    src = SRC[p["src"]]
    how = p.get("specs_from")
    if not how:
        return []
    if how == "product":
        return [(s["key"], s["value"], s["note"]) for s in src["specifications"] if s["key"] not in HIDE_SPEC_KEYS]
    if how.startswith("variant:"):
        v = next(v for v in src["grades_and_variants"] if v["name"] == how.split(":", 1)[1])
        out = []
        for s in v["specifications"]:
            val = s["value"].split(" for ")[0].split(" to ")[0]   # "Exceeding 99% NaCl for maximum efficiency" -> "Exceeding 99% NaCl"
            out.append((s["key"], val, ""))
        return out
    if how.startswith("stat:"):
        label = how.split(":", 1)[1]
        st = next(s for s in src["headline_stats"] if s["label"] == label)
        return [(label, st["value"], "")]
    raise ValueError(how)


# ---------------------------------------------------------------- product page
def product_page(lang, p, idx):
    cur = f"products/{p['slug']}.html"
    t = lambda k: L(lang, T[k])
    name = L(lang, p["name"])
    ims = imgs(p)
    hero_im = main_image(p)
    quote_text = L(lang, T["wa_quote_tpl"]).format(p=name)

    facts = []
    if p["pack"]:
        facts.append(f'<li>{icon("bag")}{t("packaging_quick")}</li>')
    for s in get_specs(p)[:2]:
        k = spec_text(lang, "key", s[0])
        v = spec_text(lang, "value", s[1])
        facts.append(f'<li>{icon("check")}{e(k)}{NB if lang == "fr" else ""}: <bdi dir="ltr">{e(v)}</bdi></li>')
    facts_html = f'<ul class="quick-facts">{"".join(facts)}</ul>' if facts else ""

    # specs card
    specs = get_specs(p)
    if specs:
        rows = []
        for k, v, n in specs:
            kk = spec_text(lang, "key", k)
            nn = spec_text(lang, "note", n)
            vv = spec_text(lang, "value", v)
            rows.append(f'<tr><th scope="row">{e(kk)}{f"<small>{e(nn)}</small>" if nn else ""}</th><td><bdi dir="ltr">{e(vv)}</bdi></td></tr>')
        scope = f'<div class="spec-foot">{e(L(lang, p["spec_scope"]))}</div>' if p.get("spec_scope") else ""
        spec_html = f'''<aside class="spec-card" aria-labelledby="specs-title">
        <header><h2 id="specs-title">{t("specs")}</h2><p>{t("specs_sub")}</p></header>
        <table class="spec-table"><tbody>{"".join(rows)}</tbody></table>
        {scope}
      </aside>'''
    else:
        spec_html = f'''<aside class="spec-card" aria-labelledby="specs-title">
        <header><h2 id="specs-title">{t("specs")}</h2></header>
        <div class="spec-empty">
          <p>{t("specs_none")}</p>
          <a class="btn btn-outline" href="{wa(L(lang, T["wa_specs_tpl"]).format(p=name))}" target="_blank" rel="noopener">{t("specs_request")}</a>
        </div>
      </aside>'''

    overview = "\n".join(f"        <p>{e(L(lang, para))}</p>" for para in p["overview"])

    # variants
    variants_html = ""
    if p["variants"]:
        vs = []
        src_variants = SRC[p["src"]]["grades_and_variants"]
        for i, v in enumerate(p["variants"]):
            media = ""
            if v.get("img"):
                im = next(x for x in ims if x["file"].endswith(v["img"] + ".jpg"))
                media = f'<div class="media">{img_tag(lang, cur, im, L(lang, v["name"]))}</div>'
            hl = ""
            if v["hl"]:
                hl = '<ul class="check-list">' + "".join(f"<li>{e(L(lang, h))}</li>" for h in v["hl"]) + "</ul>"
            vs.append(f'''        <article class="variant">
          {media}
          <h3>{e(L(lang, v["name"]))}</h3>
          <p>{e(L(lang, v["desc"]))}</p>
          {hl}
        </article>''')
        many = " many" if len(vs) >= 4 else ""
        variants_html = f'''<section class="section section-alt" aria-labelledby="grades-title">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">{e(name)}</span>
      <h2 id="grades-title">{t("grades")}</h2>
      <p>{t("grades_sub")}</p>
    </div>
    <div class="variant-grid{many}">
{chr(10).join(vs)}
    </div>
  </div>
</section>'''

    # applications
    apps = []
    for i, a in enumerate(p["apps"], 1):
        sub = ""
        if len(a) == 4:
            sub = f"<span>{e(tr(lang, a[2], a[3]))}</span>"
        apps.append(f'<div class="app"><span class="num">{i:02d}</span><div><strong>{e(L(lang, a[:2]))}</strong>{sub}</div></div>')
    apps_html = f'''<section class="section" aria-labelledby="apps-title">
  <div class="container">
    <div class="section-head">
      <h2 id="apps-title">{t("applications")}</h2>
    </div>
    <div class="app-grid">
      {"".join(apps)}
    </div>
  </div>
</section>'''

    # benefits
    feat_icons = ["spark", "shield", "layers", "gauge"]
    feats = "".join(
        f'<div class="feature"><span class="icon">{icon(feat_icons[i % 4])}</span><h3>{e(tr(lang, f[0], f[1]))}</h3><p>{e(tr(lang, f[2], f[3]))}</p></div>'
        for i, f in enumerate(p["feats"]))
    cols = "cols-4" if len(p["feats"]) == 4 else "cols-3"
    feats_html = f'''<section class="section section-alt" aria-labelledby="benefits-title">
  <div class="container">
    <div class="section-head">
      <h2 id="benefits-title">{t("benefits")}</h2>
    </div>
    <div class="feature-grid {cols}">{feats}</div>
  </div>
</section>'''

    # packaging
    if p["pack"]:
        pk_icons = {"25": "bag", "50": "bag", "big": "bigbag", "bulk": "ship"}
        packs = "".join(
            f'<div class="pack">{icon(pk_icons[k])}<strong>{e(L(lang, PACK[k][0]))}</strong><span>{e(L(lang, PACK[k][1]))}</span></div>'
            for k in p["pack"])
        pack_html = f'''<section class="section" aria-labelledby="pack-title">
  <div class="container">
    <div class="section-head">
      <h2 id="pack-title">{t("packaging")}</h2>
      <p>{t("packaging_sub")}</p>
    </div>
    <div class="pack-grid">{packs}</div>
  </div>
</section>'''
    else:
        pack_html = f'''<section class="section-tight" aria-labelledby="pack-title">
  <div class="container">
    <h2 id="pack-title" class="visually-hidden">{t("packaging")}</h2>
    <p class="note">{t("packaging_request")}</p>
  </div>
</section>'''

    # gallery: any images not already used in hero or variants
    used = {hero_im["file"]} | {x["file"] for x in ims if any(x["file"].endswith((v.get("img") or "@@") + ".jpg") for v in p["variants"])}
    rest = [x for x in ims if x["file"] not in used]
    gallery_html = ""
    if rest:
        figs = "".join(f'<figure>{img_tag(lang, cur, x, f"{name} — {i}")}</figure>' for i, x in enumerate(rest, 1))
        gallery_html = f'''<section class="section-tight" aria-labelledby="gallery-title">
  <div class="container">
    <h2 id="gallery-title">{t("gallery")}</h2>
    <div class="gallery">{figs}</div>
  </div>
</section>'''

    # related: next three products in order
    related = [PRODUCTS[(idx + k) % len(PRODUCTS)] for k in (1, 2, 3)]
    related_html = f'''<section class="section section-alt" aria-labelledby="related-title">
  <div class="container">
    <div class="section-head">
      <h2 id="related-title">{t("related")}</h2>
    </div>
    <div class="card-grid">
{chr(10).join(product_card(lang, cur, r) for r in related)}
    </div>
  </div>
</section>'''

    body = f'''<section class="product-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <ol>
        <li><a href="{rel(lang, cur, "index.html")}">{t("nav_home")}</a></li>
        <li><a href="{rel(lang, cur, "products.html")}">{t("nav_products")}</a></li>
        <li aria-current="page">{e(name)}</li>
      </ol>
    </nav>
    <div class="product-hero-grid">
      <div>
        <span class="badge">{e(L(lang, p["tag"]))}</span>
        <h1>{e(name)}</h1>
        <p class="lead">{e(L(lang, p["short"]))}</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="{quote_href(lang, cur)}">{icon("mail")}{t("quote")}</a>
          <a class="btn btn-outline" href="mailto:{EMAIL}?subject={quote(L(lang, T["quote"]) + " — " + name)}">{icon("mail")}{t("email_us")}</a>
        </div>
        {facts_html}
      </div>
      <div class="media">{img_tag(lang, cur, hero_im, name, lazy=False)}</div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="overview-title">
  <div class="container overview-grid">
    <div class="prose">
      <h2 id="overview-title">{t("overview")}</h2>
{overview}
    </div>
    {spec_html}
  </div>
</section>

{variants_html}
{apps_html}
{feats_html}
{pack_html}
{gallery_html}
{cta_band(lang, cur, L(lang, T["cta_title"]).format(p=name), t("cta_text"))}
{related_html}'''
    og = (ims[-1] if hero_im is PLACEHOLDER else hero_im)["file"].lstrip("/")
    return cur, page(lang, cur, "products.html", name, L(lang, p["short"]), body, og_image=og)


# ---------------------------------------------------------------- home
def home(lang):
    cur = "index.html"
    t = lambda k: L(lang, T[k])
    S = {
        "eyebrow": ("Salt exporter from Egypt", "مُصدِّر ملح من مصر"),
        "h1a": ("Egyptian salt,", "ملح مصري"),
        "h1b": ("exported worldwide.", "يصل إلى العالم."),
        "lead": ("Egyptian Global Export supplies de-icing, food grade, industrial and specialty salt to buyers around the world — in bags, big bags or bulk.",
                 "تورّد المصرية العالمية للتصدير ملح إذابة الجليد والملح الغذائي والصناعي والأملاح المتخصصة إلى المشترين حول العالم، معبأً في أكياس أو أكياس جامبو أو سائباً."),
        "browse": ("Browse products", "تصفح المنتجات"),
        "s1": ("9", "9"), "s1l": ("Product categories", "فئات منتجات"),
        "s2": ("99.5%+", "99.5%+"), "s2l": ("NaCl on pool and softener salt", "كلوريد صوديوم لملح المسابح والتيسير"),
        "s3": ("25 kg → bulk", "25 كجم ← سائب"), "s3l": ("Flexible packaging", "تعبئة مرنة"),
        "s4": ("Suez Canal", "قناة السويس"), "s4l": ("Based in El Qantara West, Ismailia", "مقرنا في القنطرة غرب، الإسماعيلية"),
        "prod_eyebrow": ("Our products", "منتجاتنا"),
        "prod_h": ("Salt for every industry", "ملح لكل صناعة"),
        "prod_p": ("From winter roads to food production, water treatment and oil drilling — one supplier for your salt requirements.",
                   "من طرق الشتاء إلى إنتاج الغذاء ومعالجة المياه وحفر آبار النفط، مورد واحد لكل احتياجاتك من الملح."),
        "why_eyebrow": ("Why EGE", "لماذا EGE"),
        "why_h": ("A straightforward export partner", "شريك تصدير واضح وموثوق"),
        "why_p": ("We keep things simple: the right product, clear specifications and direct communication from enquiry to shipment.",
                  "نجعل الأمور بسيطة: المنتج المناسب، ومواصفات واضحة، وتواصل مباشر من الاستفسار حتى الشحن."),
    }
    s = lambda k: L(lang, S[k])
    why = [
        ("layers", ("Wide product range", "تشكيلة واسعة من المنتجات"), ("Nine salt categories for food, industry, agriculture, water treatment, pools, drilling and de-icing.", "تسع فئات من الملح للغذاء والصناعة والزراعة ومعالجة المياه والمسابح والحفر وإذابة الجليد.")),
        ("bag", ("Flexible packaging", "تعبئة مرنة"), ("25 kg and 50 kg bags, big bags or loose bulk, depending on the product and your order.", "أكياس 25 و50 كجم، أو أكياس جامبو، أو سائب، حسب المنتج وطلبك.")),
        ("shield", ("Quality focus", "تركيز على الجودة"), ("High-purity products with published specifications, and analysis shared on request.", "منتجات عالية النقاوة بمواصفات منشورة، وتحاليل نرسلها عند الطلب.")),
        ("chat", ("Easy to reach", "تواصل سهل"), ("Talk directly with our team on WhatsApp, phone or email — in English or Arabic.", "تحدث مباشرة مع فريقنا عبر واتساب أو الهاتف أو البريد الإلكتروني، بالعربية أو الإنجليزية.")),
    ]
    why_html = "".join(f'<div class="feature"><span class="icon">{icon(i)}</span><h3>{e(L(lang, h))}</h3><p>{e(L(lang, d))}</p></div>' for i, h, d in why)
    hero_img = SRC["de-icing-rock-salt"]["images"][2]   # ship loading
    cards = "\n".join(product_card(lang, cur, p) for p in PRODUCTS)
    body = f'''<section class="hero">
  <div class="hero-media">{img_tag(lang, cur, hero_img, "", lazy=False)}</div>
  <div class="container">
    <div class="hero-inner">
      <span class="eyebrow">{s("eyebrow")}</span>
      <h1>{s("h1a")} <span class="accent">{s("h1b")}</span></h1>
      <p class="lead">{s("lead")}</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="{rel(lang, cur, "products.html")}">{s("browse")}</a>
        <a class="btn btn-ghost-light" href="{quote_href(lang, cur)}">{t("quote")}</a>
      </div>
      <div class="ribbon"><span>{t("tagline").split(" • ")[0]}</span><span class="dot"></span><span>{t("tagline").split(" • ")[1]}</span><span class="stripes"><i></i><i></i></span></div>
    </div>
  </div>
</section>

<div class="container">
  <div class="stat-strip">
    <div><strong><bdi>{s("s1")}</bdi></strong><span>{s("s1l")}</span></div>
    <div><strong><bdi dir="ltr">{s("s2")}</bdi></strong><span>{s("s2l")}</span></div>
    <div><strong><bdi>{s("s3")}</bdi></strong><span>{s("s3l")}</span></div>
    <div><strong><bdi>{s("s4")}</bdi></strong><span>{s("s4l")}</span></div>
  </div>
</div>

<section class="section" aria-labelledby="products-title">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">{s("prod_eyebrow")}</span>
      <h2 id="products-title">{s("prod_h")}</h2>
      <p>{s("prod_p")}</p>
    </div>
    <div class="card-grid">
{cards}
    </div>
  </div>
</section>

<section class="section section-alt" aria-labelledby="why-title">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">{s("why_eyebrow")}</span>
      <h2 id="why-title">{s("why_h")}</h2>
      <p>{s("why_p")}</p>
    </div>
    <div class="feature-grid cols-4">{why_html}</div>
  </div>
</section>

{cta_band(lang, cur, t("cta_title_general"), t("cta_text_general"))}'''
    title = L(lang, ("Egyptian Global Export (EGE) | Salt Exporter from Egypt", "المصرية العالمية للتصدير (EGE) | مُصدِّر ملح من مصر"))
    return cur, page(lang, cur, "index.html", title, s("lead"), body, og_image=hero_img["file"].lstrip("/"))


# ---------------------------------------------------------------- products index
def products_index(lang):
    cur = "products.html"
    t = lambda k: L(lang, T[k])
    h = L(lang, ("Our salt products", "منتجاتنا من الملح"))
    sub = L(lang, ("Nine salt categories for food, industry, agriculture, water treatment, pools, drilling and winter road safety. Select a product for specifications, packaging and applications.",
                   "تسع فئات من الملح للغذاء والصناعة والزراعة ومعالجة المياه والمسابح والحفر وسلامة الطرق في الشتاء. اختر منتجاً للاطلاع على المواصفات والتعبئة والاستخدامات."))
    cards = "\n".join(product_card(lang, cur, p) for p in PRODUCTS)
    body = f'''<section class="page-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="{rel(lang, cur, "index.html")}">{t("nav_home")}</a></li><li aria-current="page">{t("nav_products")}</li></ol></nav>
    <span class="eyebrow">{t("nav_products")}</span>
    <h1>{h}</h1>
    <p>{sub}</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="card-grid">
{cards}
    </div>
  </div>
</section>
{cta_band(lang, cur, t("cta_title_general"), t("cta_text_general"))}'''
    return cur, page(lang, cur, "products.html", h, sub, body)


# ---------------------------------------------------------------- about
def about(lang):
    cur = "about.html"
    t = lambda k: L(lang, T[k])
    A = {
        "h": ("About Egyptian Global Export", "عن المصرية العالمية للتصدير"),
        "sub": ("An Egyptian export company supplying quality salt products to buyers around the world.",
                "شركة تصدير مصرية تورّد منتجات الملح عالية الجودة إلى المشترين حول العالم."),
        "who_h": ("Who we are", "من نحن"),
        "who": [("Egyptian Global Export (EGE) is an export company based in El Qantara West, Ismailia, on the Suez Canal. We supply salt products from Egypt to importers, distributors and industrial buyers worldwide.",
                 "المصرية العالمية للتصدير (EGE) شركة تصدير مقرها القنطرة غرب بمحافظة الإسماعيلية على قناة السويس. نورّد منتجات الملح من مصر إلى المستوردين والموزعين والمشترين الصناعيين حول العالم."),
                ("Our range covers de-icing salt, food grade salt, water softening and tablet salt, pool salt, agriculture salt, drilling salt, triple washed and solar salt, chemical and industrial salt, and textile salt.",
                 "تشمل منتجاتنا ملح إذابة الجليد، والملح الغذائي، وملح تيسير المياه وأقراص الملح، وملح حمامات السباحة، وملح الأعلاف، وملح الحفر، والملح المغسول ثلاثياً والملح الشمسي، والملح الكيميائي والصناعي، وملح النسيج.")],
        "mission_h": ("What we stand for", "ما نلتزم به"),
        "values": [
            ("shield", ("Quality", "الجودة"), ("Products matched to the specification your application needs.", "منتجات مطابقة للمواصفات التي يحتاجها استخدامك.")),
            ("chat", ("Clear communication", "تواصل واضح"), ("Fast, direct answers in English and Arabic.", "ردود سريعة ومباشرة بالعربية والإنجليزية.")),
            ("ship", ("Export focus", "تركيز على التصدير"), ("Packing and documentation prepared for international shipment.", "تعبئة ومستندات مُعدّة للشحن الدولي.")),
        ],
        "how_h": ("How we work", "كيف نعمل"),
        "how_p": ("From your first message to delivery, in four steps.", "من رسالتك الأولى حتى التسليم، في أربع خطوات."),
        "steps": [
            (("Tell us what you need", "أخبرنا باحتياجك"), ("Product, grade, quantity, packaging and destination.", "المنتج والدرجة والكمية والتعبئة والوجهة.")),
            (("Specifications and quote", "المواصفات وعرض السعر"), ("We confirm the right grade and send our offer.", "نؤكد الدرجة المناسبة ونرسل عرضنا.")),
            (("Packing", "التعبئة"), ("Bags, big bags or bulk, packed for your order.", "أكياس أو أكياس جامبو أو سائب حسب طلبك.")),
            (("Shipment", "الشحن"), ("Your order is shipped to your destination.", "يتم شحن طلبك إلى وجهتك.")),
        ],
    }
    a = lambda k: L(lang, A[k])
    who = "".join(f"<p>{e(L(lang, x))}</p>" for x in A["who"])
    vals = "".join(f'<div class="feature"><span class="icon">{icon(i)}</span><h3>{e(L(lang, h))}</h3><p>{e(L(lang, d))}</p></div>' for i, h, d in A["values"])
    steps = "".join(f"<li><h3>{e(L(lang, h))}</h3><p>{e(L(lang, d))}</p></li>" for h, d in A["steps"])
    im = SRC["de-icing-rock-salt"]["images"][1]   # bulk loading at port
    body = f'''<section class="page-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="{rel(lang, cur, "index.html")}">{t("nav_home")}</a></li><li aria-current="page">{t("nav_about")}</li></ol></nav>
    <span class="eyebrow">{t("nav_about")}</span>
    <h1>{a("h")}</h1>
    <p>{a("sub")}</p>
  </div>
</section>
<section class="section">
  <div class="container split">
    <div>
      <h2>{a("who_h")}</h2>
      {who}
      <div class="btn-row"><a class="btn btn-navy" href="{rel(lang, cur, "products.html")}">{t("all_products")}</a></div>
    </div>
    <div class="media">{img_tag(lang, cur, im, a("h"))}</div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head"><h2>{a("mission_h")}</h2></div>
    <div class="feature-grid cols-3">{vals}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head"><h2>{a("how_h")}</h2><p>{a("how_p")}</p></div>
    <ol class="steps">{steps}</ol>
  </div>
</section>
{cta_band(lang, cur, t("cta_title_general"), t("cta_text_general"))}'''
    return cur, page(lang, cur, "about.html", L(lang, ("About us", "من نحن")), a("sub"), body)


# ---------------------------------------------------------------- faq
def faq(lang):
    cur = "faq.html"
    t = lambda k: L(lang, T[k])
    names_en = ", ".join(p["name"][0] for p in PRODUCTS)
    names_ar = "، ".join(p["name"][1] for p in PRODUCTS)
    names_fr = ", ".join(L("fr", p["name"]).lower() for p in PRODUCTS)
    Q = [
        (("What products do you export?", "ما المنتجات التي تصدّرونها؟"),
         (f"We export nine salt categories: {names_en}. See the products page for details on each.",
          f"نصدّر تسع فئات من الملح: {names_ar}. راجع صفحة المنتجات لمعرفة تفاصيل كل منتج.",
          f"Nous exportons neuf catégories de sel{NB}: {names_fr}. Chaque produit est détaillé sur la page Produits.")),
        (("What packaging options are available?", "ما خيارات التعبئة المتاحة؟"),
         ("Most products are available in 25 kg bags, 50 kg bags, big bags and loose bulk. Available options vary by product, so we confirm them with your quote.",
          "تتوفر معظم المنتجات في أكياس 25 كجم و50 كجم وأكياس جامبو وسائبة. تختلف الخيارات المتاحة حسب المنتج، لذلك نؤكدها مع عرض السعر.")),
        (("Can I get technical specifications or an analysis?", "هل يمكنني الحصول على المواصفات الفنية أو التحليل؟"),
         ("Yes. Published specifications are shown on each product page. For other products, or for a detailed analysis, contact us and tell us your application.",
          "نعم. المواصفات المنشورة موجودة في صفحة كل منتج. للمنتجات الأخرى أو لتحليل تفصيلي، تواصل معنا وأخبرنا باستخدامك.")),
        (("Which grain sizes are available?", "ما أحجام الحبيبات المتاحة؟"),
         ("Grain size depends on the product and its use. De-icing salt, for example, comes in several grain sizes. Tell us your application and we'll recommend the right one.",
          "يعتمد حجم الحبيبات على المنتج واستخدامه؛ فملح إذابة الجليد مثلاً متوفر بعدة أحجام. أخبرنا باستخدامك وسنقترح الحجم المناسب.")),
        (("How do I request a quote?", "كيف أطلب عرض سعر؟"),
         (f"Use any \u201cRequest a Quote\u201d button to open our enquiry form, or email {EMAIL}. Include the product, grade, quantity, packaging and destination port so we can price it accurately.",
          f"استخدم أي زر \u201cاطلب عرض سعر\u201d لفتح نموذج الاستفسار، أو راسلنا على {EMAIL}. اذكر المنتج والدرجة والكمية والتعبئة وميناء الوصول حتى نتمكن من التسعير بدقة.",
          f"Cliquez sur l'un des boutons «{NB}Demander un devis{NB}» pour ouvrir notre formulaire de demande, ou écrivez-nous à {EMAIL}. Précisez le produit, la qualité, la quantité, le conditionnement et le port de destination{NB}: nous pourrons ainsi chiffrer votre demande au plus juste.")),
        (("Do you ship internationally?", "هل تشحنون إلى خارج مصر؟"),
         ("Yes. We are an export company and supply buyers outside Egypt. Tell us your destination when you request a quote.",
          "نعم. نحن شركة تصدير ونورّد للمشترين خارج مصر. أخبرنا بوجهتك عند طلب عرض السعر.")),
        (("Is there a minimum order quantity?", "هل يوجد حد أدنى للطلب؟"),
         ("Order quantities depend on the product and packaging. Contact us with your requirements and we'll let you know what's possible.",
          "تعتمد الكميات على المنتج وطريقة التعبئة. تواصل معنا بمتطلباتك وسنخبرك بالخيارات المتاحة.")),
        (("Where are you located?", "أين يقع مقركم؟"),
         (f"Our office is at {ADDRESS[0]}.", f"يقع مكتبنا في {ADDRESS[1]}.", f"Nos bureaux se trouvent au {ADDRESS[2]}.")),
    ]
    items = "\n".join(f'''    <details>
      <summary>{e(L(lang, q))}</summary>
      <div class="answer"><p>{e(L(lang, ans))}</p></div>
    </details>''' for q, ans in Q)
    h = L(lang, ("Frequently asked questions", "الأسئلة الشائعة"))
    sub = L(lang, ("Answers to common questions about our products, packaging and ordering.", "إجابات عن الأسئلة المتكررة حول منتجاتنا والتعبئة وطريقة الطلب."))
    body = f'''<section class="page-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="{rel(lang, cur, "index.html")}">{t("nav_home")}</a></li><li aria-current="page">{t("nav_faq")}</li></ol></nav>
    <span class="eyebrow">{t("nav_faq")}</span>
    <h1>{h}</h1>
    <p>{sub}</p>
  </div>
</section>
<section class="section">
  <div class="faq-list container">
{items}
  </div>
</section>
{cta_band(lang, cur, L(lang, ("Still have a question?", "لديك سؤال آخر؟")), L(lang, ("Send us your question through the enquiry form or by email — we're happy to help.", "أرسل لنا سؤالك عبر نموذج الاستفسار أو البريد الإلكتروني، ويسعدنا مساعدتك.", f"Envoyez-nous votre question via le formulaire ou par e-mail{NB}: nous serons ravis de vous aider.")), label=t("form_title"))}'''
    return cur, page(lang, cur, "faq.html", h, sub, body)


# ---------------------------------------------------------------- contact
def contact(lang):
    cur = "contact.html"
    t = lambda k: L(lang, T[k])
    h = L(lang, ("Contact us", "تواصل معنا"))
    sub = L(lang, ("Message us on WhatsApp for the fastest reply, or reach us by phone or email.", "راسلنا عبر واتساب للحصول على أسرع رد، أو تواصل معنا هاتفياً أو بالبريد الإلكتروني."))
    map_src = f"https://www.google.com/maps/embed?origin=mfe&amp;pb=!1m3!2m1!1s{MAP_LAT},{MAP_LNG}!6i17!3m1!1s{lang}!5m1!1s{lang}"
    map_title = e(L(lang, ("Map: ", "الخريطة: ")) + L(lang, ADDRESS))
    map_html = (MAP_EMBED_HTML.strip() if MAP_EMBED_HTML.strip() else
                f'<iframe src="{map_src}" title="{map_title}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>')
    tips = [
        ("Product and grade", "المنتج والدرجة"), ("Quantity", "الكمية"), ("Packaging (bags, big bags or bulk)", "التعبئة (أكياس أو جامبو أو سائب)"),
        ("Destination port or country", "ميناء أو دولة الوصول"), ("Any specification requirements", "أي متطلبات خاصة بالمواصفات"),
    ]
    tips_html = "".join(f"<li>{e(L(lang, x))}</li>" for x in tips)
    body = f'''<section class="page-hero">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="{rel(lang, cur, "index.html")}">{t("nav_home")}</a></li><li aria-current="page">{t("nav_contact")}</li></ol></nav>
    <span class="eyebrow">{t("nav_contact")}</span>
    <h1>{h}</h1>
    <p>{sub}</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-card wa">
        <span class="icon">{WA_SVG}</span>
        <h3>WhatsApp</h3>
        <a href="{wa(t("wa_general"))}" target="_blank" rel="noopener"><span class="ltr">{PHONE_DISPLAY}</span></a>
      </div>
      <div class="contact-card">
        <span class="icon">{icon("phone")}</span>
        <h3>{L(lang, ("Phone", "الهاتف"))}</h3>
        <a href="tel:{PHONE_TEL}"><span class="ltr">{PHONE_DISPLAY}</span></a>
      </div>
      <div class="contact-card">
        <span class="icon">{icon("mail")}</span>
        <h3>{L(lang, ("Email", "البريد الإلكتروني"))}</h3>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
      <div class="contact-card">
        <span class="icon">{icon("pin")}</span>
        <h3>{L(lang, ("Address", "العنوان"))}</h3>
        <address>{e(L(lang, ADDRESS))}<span lang="{"en" if lang == "ar" else "ar"}" dir="{"ltr" if lang == "ar" else "rtl"}">{e(ADDRESS[0] if lang == "ar" else ADDRESS[1])}</span></address>
      </div>
    </div>
    <div class="map-wrap">
      {map_html}
    </div>
    <p class="map-link"><a class="btn btn-outline" href="{MAP_LINK}" target="_blank" rel="noopener">{icon("pin")}{L(lang, ("Open in Google Maps", "افتح في خرائط Google", "Ouvrir dans Google Maps"))}</a></p>
  </div>
</section>
<section class="section section-alt" id="enquiry">
  <div class="container quote-tips">
    <div>
      <span class="eyebrow">{t("form_eyebrow")}</span>
      <h2>{t("form_title")}</h2>
      <p class="text-muted">{t("form_intro")}</p>
      <h3 class="tips-title">{t("form_include")}</h3>
      <ul class="check-list">{tips_html}</ul>
    </div>
    {enquiry_form(lang, cur)}
  </div>
</section>'''
    return cur, page(lang, cur, "contact.html", h, sub, body)


def enquiry_form(lang, cur):
    t = lambda k: L(lang, T[k])
    req = f'<span class="req" aria-hidden="true">*</span><span class="visually-hidden"> ({t("required")})</span>'
    opts = "".join(f'<option value="{e(p["name"][0])}">{e(L(lang, p["name"]))}</option>' for p in PRODUCTS)
    opts += f'<option value="Other / several products">{e(t("f_other"))}</option>'

    def inp(name, label, typ="text", required=False, ac="", ph="", dir_="", full=False):
        r = " required" if required else ""
        a = f' autocomplete="{ac}"' if ac else ""
        pl = f' placeholder="{e(ph)}"' if ph else ""
        d = f' dir="{dir_}"' if dir_ else ""
        return (f'<div class="field{" full" if full else ""}"><label for="f-{name}">{e(label)}{req if required else ""}</label>'
                f'<input id="f-{name}" name="{name}" type="{typ}"{r}{a}{pl}{d} maxlength="200"></div>')

    return f'''<form class="enquiry-form" action="{asset(lang, cur, "send.php")}" method="post" accept-charset="UTF-8">
      <input type="hidden" name="lang" value="{lang}">
      <div class="hp" aria-hidden="true"><label for="f-website">Website</label><input id="f-website" type="text" name="website" tabindex="-1" autocomplete="off"></div>
      <div class="form-grid">
        {inp("name", t("f_name"), required=True, ac="name")}
        {inp("company", t("f_company"), ac="organization")}
        {inp("email", t("f_email"), typ="email", required=True, ac="email", dir_="ltr")}
        {inp("phone", t("f_phone"), typ="tel", ac="tel", dir_="ltr")}
        {inp("country", t("f_country"), ac="country-name")}
        <div class="field"><label for="f-product">{t("f_product")}{req}</label>
          <select id="f-product" name="product" required><option value="">{e(t("f_choose"))}</option>{opts}</select></div>
        {inp("quantity", t("f_quantity"), ph=t("f_quantity_ph"), full=True)}
        <div class="field full"><label for="f-message">{t("f_message")}{req}</label>
          <textarea id="f-message" name="message" rows="5" required maxlength="5000" placeholder="{e(t("f_message_ph"))}"></textarea></div>
      </div>
      <p class="form-note">{t("f_privacy")}</p>
      <button class="btn btn-primary" type="submit">{icon("mail")}{t("f_submit")}</button>
    </form>'''


def result_page(lang, ok):
    cur = "thanks.html" if ok else "sorry.html"
    t = lambda k: L(lang, T[k])
    key = "thanks" if ok else "sorry"
    buttons = (f'<a class="btn btn-navy" href="{rel(lang, cur, "index.html")}">{t("back_home")}</a>'
               f'<a class="btn btn-outline" href="{rel(lang, cur, "products.html")}">{t("all_products")}</a>') if ok else (
               f'<a class="btn btn-navy" href="{rel(lang, cur, "contact.html")}#enquiry">{t("back_form")}</a>'
               f'<a class="btn btn-whatsapp" href="{wa(t("wa_general"))}" target="_blank" rel="noopener">{WA_SVG}WhatsApp</a>'
               f'<a class="btn btn-outline" href="mailto:{EMAIL}">{icon("mail")}{EMAIL}</a>')
    body = f'''<section class="page-hero">
  <div class="container">
    <span class="eyebrow">{t("nav_contact")}</span>
    <h1>{t(key + "_h")}</h1>
    <p>{t(key + "_p")}</p>
  </div>
</section>
<section class="section">
  <div class="container"><div class="btn-row">{buttons}</div></div>
</section>'''
    return cur, page(lang, cur, "contact.html", t(key + "_title"), t(key + "_p"), body, noindex=True)


# ---------------------------------------------------------------- write
def write(lang, cur, content):
    path = os.path.join(OUT, prefix(lang), cur)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


written = []
no_index = []   # thanks/sorry pages: not in the sitemap
for lang in LANGS:
    for fn in (home, products_index, about, faq, contact):
        written.append(write(lang, *fn(lang)))
    for i, p in enumerate(PRODUCTS):
        written.append(write(lang, *product_page(lang, p, i)))
    for ok in (True, False):
        no_index.append(write(lang, *result_page(lang, ok)))

if MISSING_FR:
    print("Missing French text for:")
    for m in dict.fromkeys(MISSING_FR):
        print("  -", repr(m))
    sys.exit("Build stopped: add these to FR in tools/content.py")

# ege_description: the final page copy, so the JSON matches the site
def copy_for(p, lang):
    L_ = lambda pair: L(lang, pair)
    return {
        "name": L_(p["name"]),
        "category_tag": L_(p["tag"]),
        "card_summary": L_(p["card"]),
        "short_description": L_(p["short"]),
        "overview": [L_(x) for x in p["overview"]],
        "grades_and_variants": [{"name": L_(v["name"]), "description": L_(v["desc"]),
                                 "highlights": [L_(h) for h in v["hl"]]} for v in p["variants"]],
        "applications": [{"title": L_(a[:2]), **({"description": tr(lang, a[2], a[3])} if len(a) == 4 else {})}
                         for a in p["apps"]],
        "benefits": [{"title": tr(lang, f[0], f[1]), "description": tr(lang, f[2], f[3])} for f in p["feats"]],
        "packaging": [f"{L_(PACK[k][0])} — {L_(PACK[k][1])}" for k in p["pack"]],
        "specifications_shown": [
            {"key": spec_text(lang, "key", k), "value": spec_text(lang, "value", v), "note": spec_text(lang, "note", n)}
            for k, v, n in get_specs(p)],
        "page": f"{prefix(lang)}products/{p['slug']}.html",
    }


json_path = os.path.join(ROOT, "data", "products.json")
for p in PRODUCTS:
    SRC[p["src"]]["ege_description"] = {x: copy_for(p, x) for x in LANGS}
    if p["slug"] in HIDE_IMAGES:
        SRC[p["src"]]["site_main_image"] = PLACEHOLDER["file"]
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(DATA, f, ensure_ascii=False, indent=2)

# sitemap + robots
urls = []
for wpath in written:
    relp = os.path.relpath(wpath, OUT).replace(os.sep, "/").replace("index.html", "")
    urls.append(f"  <url><loc>{DOMAIN}/{relp}</loc></url>")
open(os.path.join(OUT, "sitemap.xml"), "w").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
print(len(written) + len(no_index), "pages written")
