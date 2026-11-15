#!/usr/bin/env python3
"""Builds the static Platinum Law Firm site into the repository root (published by GitHub Pages).
Run:  python3 tools/build.py
Edit the CONTENT below, then re-run. No other tools needed."""
import os, html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PREVIEW = os.environ.get("PREVIEW") == "1"   # preview build: relative links that work from plain files
OUT = ROOT / "preview" if PREVIEW else ROOT   # the repository root is the published site

# Images live in assets/img/ (copied from the old site on 2026-11-14).
IMAGES = {
    "logo": "/assets/img/logo.webp",
    "icon": "/assets/img/icon.png",
    "titi": "/assets/img/titi.webp",
    "titi2": "/assets/img/titi.webp",
}

FIRM = "Platinum Law Firm"
PHONE = "+1 437-557-0010"
TEL = "+14375570010"
EMAIL = "contact@platinumlawfirm.ca"
ADDRESS = ["500-7030 Woodbine Avenue", "Markham, ON L3R 6G2", "Canada"]
HOURS = "Monday – Friday, 9am – 5pm"
BOOK = "https://platinumlawfirm.cliogrow.com/book"
WHATSAPP = "https://wa.me/14375570010"
LINKEDIN = "https://www.linkedin.com/in/titi-olatunji-b4676b242/"
INSTAGRAM = "https://www.instagram.com/platinum_law_firm/"
DOMAIN = "https://www.platinumlawfirm.ca"

SERVICES = [
    dict(slug="mental-health-law", name="Mental Health Law", long="Mental Health Law",
         summary="We provide respectful and confidential legal advice and representation to people affected by mental health and capacity issues, and to the families who support them.",
         tagline="Protecting your rights, your dignity and your voice in mental health and capacity matters.",
         intro=["Mental health law in Ontario can be complex and stressful, especially when it involves hospital admission, treatment decisions, or questions about a person's capacity to make their own choices. At Platinum Law Firm, we provide respectful, confidential legal advice and representation to help clients understand their rights and have their voice heard.",
                "Whether you or a loved one are facing an involuntary admission, a finding of incapacity, or a disagreement about treatment or a substitute decision-maker, our goal is to protect your rights and your dignity. Contact us today to schedule a consultation and learn how we can assist you with your mental health law needs."],
         items=["Consent and Capacity Board hearings", "Challenges to involuntary hospital admission", "Capacity to consent to treatment", "Community treatment orders", "Substitute decision-makers", "Powers of attorney for personal care", "Guardianship applications", "Advice for families and caregivers"]),
    dict(slug="business-law", name="Business Law", long="Business Law",
         summary="We offer expert legal solutions to meet the unique needs of businesses, from contract review to employment disputes and everything in between. We help our clients achieve their goals and protect their rights.",
         tagline="Expert legal solutions for your business, from contract review to disputes and everything in between.",
         intro=["Business law in Ontario can be complex and challenging, especially for those starting or running a business in the province. At Platinum Law Firm, our experienced business lawyers provide comprehensive legal advice and representation to help clients navigate this landscape with confidence. Whether you are starting a new business, seeking to protect your intellectual property, negotiating contracts, or dealing with disputes, our goal is to help you achieve your business goals and protect your interests.",
                "Our lawyers have a deep understanding of the business environment in Ontario and are well-versed in the laws and regulations that govern this field. With our expertise and commitment to client satisfaction, you can be sure that you are in good hands. Contact us today to schedule a consultation and learn how we can assist you with your business law needs."],
         items=["Incorporation and post-incorporation", "Partnerships", "Business name registration", "Contract negotiation, drafting and review", "Purchase and sale of a business", "Joint ventures", "Business consulting", "Minute book preparation", "Not-for-profit organizations", "Annual returns filing"]),
    dict(slug="real-estate-law", name="Real Estate Law", long="Real Estate Law",
         summary="We provide comprehensive legal advice and representation in real estate law, from residential to commercial transactions, to help clients protect their interests and achieve their real estate goals.",
         tagline="Legal advice and representation from residential to commercial transactions.",
         intro=["Real estate law in Ontario can be complex and confusing, especially when it comes to buying, selling, or leasing property. At Platinum Law Firm, our experienced real estate lawyers provide comprehensive legal advice and representation to help clients navigate this process with confidence. Whether you are buying your first home, selling a commercial property, or leasing a space for your business, our goal is to protect your interests and help you achieve your real estate goals.",
                "Our lawyers have a deep understanding of the real estate market in Ontario and are well-versed in the laws and regulations that govern this industry. With our expertise and commitment to client satisfaction, you can be sure that you are in good hands. Contact us today to schedule a consultation and learn how we can assist you with your real estate needs."],
         items=["Purchase and sale of residential properties", "Purchase and sale of commercial properties", "Mortgage refinancing", "Title search", "Title insurance", "Lease agreements", "Status certificate review", "Independent legal advice"]),
    dict(slug="wills-and-estates", name="Wills and Estates", long="Wills and Estates",
         summary="We provide comprehensive legal advice and representation in wills and estates, to help clients create a solid estate plan that meets their unique needs and protects their loved ones.",
         tagline="Create a solid estate plan that protects your loved ones.",
         intro=["Wills and estates law in Ontario can be complex and confusing, especially when it comes to planning for the future and protecting your assets. At Platinum Law Firm, our experienced wills and estates lawyers provide comprehensive legal advice and representation to help clients navigate this process with confidence. Whether you are creating a will, dealing with the estate of a loved one, or seeking to understand your rights and responsibilities as an executor or beneficiary, our goal is to help you achieve your goals and protect your interests.",
                "Our lawyers have a deep understanding of the laws and regulations that govern wills and estates in Ontario and are well-versed in the probate process. With our expertise and commitment to client satisfaction, you can be sure that you are in good hands. Contact us today to schedule a consultation and learn how we can assist you with your wills and estates needs."],
         items=["Wills", "Probate applications", "Powers of attorney", "Estate planning", "Trusts (testamentary, family)", "Guardianship and capacity disputes", "Will storage services"]),
    dict(slug="notary-public", name="Notary Public", long="Notary Public",
         summary="We offer fast and reliable notary public services to individuals and businesses, to help complete legal documents, affirmations, and declarations.",
         tagline="Fast and reliable notary services for individuals and businesses.",
         intro=["Notary public services in Ontario involve providing legally recognized signatures, stamps, and certificates for important documents. At Platinum Law Firm, our experienced lawyers provide comprehensive legal advice to help clients navigate this process with confidence. Whether you are seeking to have a document notarized, attested, or authenticated, our goal is to help you achieve your goals and protect your interests.",
                "Our lawyers have a deep understanding of the laws and regulations that govern notary public services in Ontario and are well-versed in the procedures and protocols involved. Contact us today to schedule a consultation and learn how we can assist you with your notary needs."],
         items=["Passport declarations", "Statutory declarations", "Affidavits", "Invitation letters", "Consent to travel letters", "Certified copies of original documents"]),
]

ICONS = {  # simple line icons, one per practice area
    "immigration-law": '<path d="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18Zm-9 9h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3Z"/>',
    "family-law": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10Z"/>',
    "mental-health-law": '<path d="M9.5 4a3.5 3.5 0 0 0-3.4 4.3A3.5 3.5 0 0 0 6 15a3 3 0 0 0 3.5 3.5V4ZM14.5 4a3.5 3.5 0 0 1 3.4 4.3A3.5 3.5 0 0 1 18 15a3 3 0 0 1-3.5 3.5V4ZM9.5 4h5M9.5 18.5h5"/>',
    "business-law": '<path d="M4 8h16v11H4zM9 8V5h6v3M4 13h16"/>',
    "real-estate-law": '<path d="M3 11 12 4l9 7M5 10v10h14V10M10 20v-6h4v6"/>',
    "employment-law": '<path d="M8 7a4 4 0 1 0 8 0 4 4 0 0 0-8 0ZM4 21c0-4 3.6-7 8-7s8 3 8 7"/>',
    "wills-and-estates": '<path d="M7 3h7l4 4v14H7zM14 3v4h4M10 12h5M10 16h5"/>',
    "notary-public": '<path d="M12 3 4 7v2h16V7l-8-4ZM6 9v8M10 9v8M14 9v8M18 9v8M4 19h16"/>',
}

def e(s): return html.escape(s, quote=True)

def icon(slug):
    return f'<svg class="icon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS[slug]}</svg>'

CSP = ("default-src 'self'; img-src 'self' data:; style-src 'self' https://fonts.googleapis.com; "
       "font-src https://fonts.gstatic.com; script-src 'self'; frame-src 'none'; object-src 'none'; base-uri 'self'; form-action 'none'")

def page(path, title, desc, body, active=""):
    depth = path.count("/")
    canonical = DOMAIN + "/" + path.replace("index.html", "")
    nav_items = [("", "Home"), ("about/", "About"), ("services/", "Services"), ("attorney/titilope-olatunji/", "Attorney"), ("contact/", "Contact")]
    nav = "".join(f'<a href="/{h}"{" aria-current=\"page\"" if active == h else ""}>{t}</a>' for h, t in nav_items)
    full_title = f"{title} | {FIRM}" if title != FIRM else f"{FIRM} | Lawyers in Markham, Ontario"
    schema = ('{"@context":"https://schema.org","@type":"LegalService","name":"Platinum Law Firm",'
              f'"url":"{DOMAIN}/","telephone":"{TEL}","email":"{EMAIL}",'
              '"address":{"@type":"PostalAddress","streetAddress":"500-7030 Woodbine Avenue","addressLocality":"Markham","addressRegion":"ON","postalCode":"L3R 6G2","addressCountry":"CA"},'
              '"openingHours":"Mo-Fr 09:00-17:00","areaServed":"Ontario"}')
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<link rel="icon" href="{IMAGES['icon']}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Poppins:wght@300;400;500;600&display=swap">
<link rel="stylesheet" href="/css/styles.css">
<script type="application/ld+json">{schema}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap">
  <span><a href="tel:{TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></span>
  <span class="hide-sm">{HOURS}</span>
</div></div>
<header class="site-header"><div class="wrap">
  <a class="brand" href="/"><img src="{IMAGES['logo']}" alt="Platinum Law Firm" width="180" height="70"></a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav id="nav" class="nav">{nav}<a class="btn btn-sm" href="{BOOK}" target="_blank" rel="noopener noreferrer">Book a consultation</a></nav>
</div></header>
<main id="main">
{body}
<section class="cta"><div class="wrap cta-inner">
  <div><p class="eyebrow">Let us help you</p><h2>Looking for legal assistance?</h2>
  <p>Call <a href="tel:{TEL}">{PHONE}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>. {HOURS}.</p></div>
  <a class="btn" href="{BOOK}" target="_blank" rel="noopener noreferrer">Book a consultation</a>
</div></section>
</main>
<footer class="site-footer"><div class="wrap footer-grid">
  <div><img src="{IMAGES['logo']}" alt="Platinum Law Firm" width="160" height="62" loading="lazy">
  <p>Our mission is to provide accessible, affordable, and professional legal services consistently to meet the needs of our clients.</p></div>
  <div><h3>Contact</h3><address>{'<br>'.join(e(a) for a in ADDRESS)}</address>
  <p><a href="tel:{TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>{HOURS}</p></div>
  <div><h3>Practice areas</h3><ul>{''.join(f'<li><a href="/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)}</ul></div>
  <div><h3>Follow</h3><ul><li><a href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn</a></li><li><a href="{INSTAGRAM}" target="_blank" rel="noopener noreferrer">Instagram</a></li><li><a href="{WHATSAPP}" target="_blank" rel="noopener noreferrer">WhatsApp</a></li></ul></div>
</div>
<div class="wrap legal"><p>© <span id="yr">2026</span> Platinum Law Firm. All rights reserved. · <a href="/privacy/">Privacy</a></p>
<p class="disclaimer">The information on this website is general information, not legal advice. Contacting us does not create a lawyer–client relationship.</p></div>
</footer>
<a class="wa" href="{WHATSAPP}" target="_blank" rel="noopener noreferrer" aria-label="Chat with us on WhatsApp"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4a.5.5 0 0 0 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3Z"/></svg><span>Chat with us</span></a>
<script src="/js/site.js" defer></script>
</body>
</html>
"""
    if PREVIEW:
        doc = relativize(doc, depth)
    p = OUT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(doc, encoding="utf-8")

def relativize(doc, depth):
    import re
    pre = "../" * depth
    def fix(m):
        attr, url = m.group(1), m.group(2)
        if url.endswith("/") or url == "":
            url = url + "index.html"
        return f'{attr}="{pre}{url}"'
    return re.sub(r'(href|src)="/(?!/)([^"]*)"', fix, doc)

def hero(eyebrow, h1, lead, small=False, buttons=True):
    b = (f'<div class="hero-actions"><a class="btn" href="{BOOK}" target="_blank" rel="noopener noreferrer">Book a consultation</a>'
         f'<a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a></div>') if buttons else ""
    return f'<section class="hero{" hero-sm" if small else ""}"><div class="wrap"><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p class="lead">{lead}</p>{b}</div></section>'

def service_cards():
    return '<div class="cards">' + "".join(
        f'<a class="card" href="/{s["slug"]}/">{icon(s["slug"])}<h3>{s["long"]}</h3><p>{e(s["summary"])}</p><span class="more">Learn more →</span></a>'
        for s in SERVICES) + "</div>"

def build():
    # Home
    body = hero("Platinum Law Firm · Markham, Ontario", "Want some legal advice?",
                "We are a law firm serving clients across Ontario in mental health, business, real estate, wills &amp; estates, and notary services, with a commitment to excellence and professionalism.")
    body += f'<section class="section"><div class="wrap"><p class="eyebrow">Our services</p><h2>Legal practice areas</h2>{service_cards()}</div></section>'
    body += f"""<section class="section alt"><div class="wrap split">
  <img class="portrait" src="{IMAGES['titi']}" alt="Titilope Olatunji, lawyer" width="440" height="563" loading="lazy">
  <div><p class="eyebrow">Meet your lawyer</p><h2>Titilope (Titi) Olatunji</h2>
  <p>Titi is a member of the Law Society of Ontario with extensive experience in corporate and commercial law, civil litigation, and real estate law since her first bar admission in 2011. Her driving force is to empower individuals in realizing their aspirations, and she goes the extra mile to advocate for her clients.</p>
  <p><a class="link" href="/attorney/titilope-olatunji/">Read Titi's biography →</a></p></div>
</div></section>
<section class="section"><div class="wrap values">
  <div><h3>Our mission</h3><p>To provide accessible, affordable, and professional legal services consistently to meet the needs of our clients.</p></div>
  <div><h3>Our vision</h3><p>To provide excellent legal services that best suit our clients' needs.</p></div>
  <div><h3>Our values</h3><p>Professionalism, integrity and excellence.</p></div>
</div></section>"""
    page("index.html", FIRM, "Platinum Law Firm in Markham, Ontario: mental health, business, real estate, wills and estates, and notary public services. Book a consultation.", body, "")

    # About
    body = hero("About us", "About Platinum Law Firm", "A personalized approach to every case, for individuals and businesses across Ontario.", small=True)
    body += f"""<section class="section"><div class="wrap split">
  <div class="prose"><h2>Our history</h2>
  <p>Platinum Law Firm has been serving the legal needs of clients with a commitment to putting clients first. The firm takes a personalized approach to each case, working closely with clients to understand their unique needs and goals. Whether you are facing a personal legal issue or a business challenge, Platinum Law Firm is dedicated to providing you with the legal guidance and support you need to achieve the best possible outcome.</p>
  <p>We have extensive knowledge of a wide range of legal areas, including corporate law, contract law, real estate law, mental health law, and more. We use this knowledge to develop strategic and effective solutions that meet the individual needs of each client. Our services are available to residents of Toronto and throughout the province of Ontario.</p>
  <p>At Platinum Law Firm, we believe that everyone deserves access to high-quality legal services. That's why we offer a range of payment options and strive to make our services as accessible and affordable as possible. Whether you're dealing with a complex legal matter or a straightforward case, we are here to help you resolve your legal concerns and achieve your goals.</p></div>
  <img class="portrait" src="{IMAGES['titi']}" alt="Titilope Olatunji, lawyer" width="440" height="563" loading="lazy">
</div></section>
<section class="section alt"><div class="wrap values">
  <div><h3>Our mission</h3><p>Our principal mission is to provide accessible, affordable, and professional legal services consistently to meet the needs of our clients.</p></div>
  <div><h3>Our vision</h3><p>Our vision is to provide excellent legal services that best suit our clients' needs.</p></div>
  <div><h3>Our values</h3><p>Professionalism, integrity and excellence.</p></div>
</div></section>
<section class="section"><div class="wrap"><p class="eyebrow">What we do</p><h2>Practice areas</h2>{service_cards()}</div></section>"""
    page("about/index.html", "About", "About Platinum Law Firm: our history, mission, vision and values. Serving Toronto, Markham and all of Ontario.", body, "about/")

    # Services
    body = hero("Our services", "Legal practice areas", "Five areas of law, one dedicated team. Choose a service to learn more.", small=True, buttons=False)
    body += f'<section class="section"><div class="wrap">{service_cards()}</div></section>'
    page("services/index.html", "Services", "Legal services at Platinum Law Firm: mental health, business, real estate, wills and estates, notary public.", body, "services/")

    # Each service
    for s in SERVICES:
        others = "".join(f'<li><a href="/{o["slug"]}/"{" aria-current=\"page\"" if o is s else ""}>{o["name"]}</a></li>' for o in SERVICES)
        body = hero(s["name"], s["long"], e(s["tagline"]), small=True)
        body += f"""<section class="section"><div class="wrap with-aside">
  <div class="prose">{''.join(f'<p>{e(p)}</p>' for p in s['intro'])}
  <h2>Our {s['name'].lower() if s['slug'] != 'notary-public' else 'notary'} services include</h2>
  <ul class="checks">{''.join(f'<li>{e(i)}</li>' for i in s['items'])}</ul>
  <p><a class="btn" href="{BOOK}" target="_blank" rel="noopener noreferrer">Book a consultation</a></p></div>
  <aside class="aside"><h3>Practice areas</h3><ul>{others}</ul>
  <div class="aside-box"><h3>Let us help you</h3><p>If you need legal assistance, contact us. We will get back to you promptly.</p>
  <p><a href="tel:{TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>{HOURS}</p></div></aside>
</div></section>"""
        page(f"{s['slug']}/index.html", s["long"], f"{s['long']} lawyer in Markham, Ontario. {s['summary']}", body, "services/")

    # Attorney
    body = hero("Attorney", "Titilope Olatunji", "Lawyer · Member, Law Society of Ontario", small=True, buttons=False)
    body += f"""<section class="section"><div class="wrap split">
  <img class="portrait" src="{IMAGES['titi2']}" alt="Titilope Olatunji" width="440" height="563" loading="lazy">
  <div class="prose"><h2>Biography</h2>
  <p>Titilope Olatunji, commonly referred to as Titi, holds a Master of Laws degree from the University of Lagos. Her educational journey began with a Bachelor of Laws (LL.B) degree from the University of Ilorin in Nigeria, followed by a Barrister-at-Law degree from the Nigerian Law School.</p>
  <p>Since her admission to the Nigerian bar in 2011, Titi has accrued extensive experience in the practice of law, particularly in corporate/commercial law, civil litigation, and real estate law. In addition to her work in Nigeria, she is a member of the Law Society of Ontario.</p>
  <h3>Passion</h3><p>Titi's driving force is to empower individuals in realizing their aspirations. She goes the extra mile to advocate for her clients.</p>
  <p><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="tel:{TEL}">{PHONE}</a> · <a href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn</a></p></div>
</div></section>
<section class="section alt"><div class="wrap values">
  <div><h3>Practice areas</h3><ul class="checks"><li>Commercial law</li><li>Business and corporate law</li><li>Contract law</li><li>Real estate law</li><li>Civil litigation</li></ul></div>
  <div><h3>Education &amp; bar admission</h3><ul class="checks"><li>Master of Laws (LL.M), University of Lagos, Nigeria</li><li>Barrister-at-Law, Nigerian Law School</li><li>Bachelor of Laws (LL.B), University of Ilorin, Nigeria</li><li>Member, Law Society of Ontario, Canada</li></ul></div>
</div></section>"""
    page("attorney/titilope-olatunji/index.html", "Titilope Olatunji", "Titilope (Titi) Olatunji, lawyer at Platinum Law Firm and member of the Law Society of Ontario.", body, "attorney/titilope-olatunji/")

    # Contact
    body = hero("Contact us", "Get in touch", "Have a question? Call, email, WhatsApp, or book a consultation online. We will respond to your inquiry promptly.", small=True, buttons=False)
    body += f"""<section class="section"><div class="wrap contact-grid">
  <a class="contact-card" href="tel:{TEL}"><h3>Call</h3><p>{PHONE}</p></a>
  <a class="contact-card" href="mailto:{EMAIL}"><h3>Email</h3><p>{EMAIL}</p></a>
  <a class="contact-card" href="{WHATSAPP}" target="_blank" rel="noopener noreferrer"><h3>WhatsApp</h3><p>Chat with us</p></a>
  <a class="contact-card" href="{BOOK}" target="_blank" rel="noopener noreferrer"><h3>Book online</h3><p>Schedule a consultation</p></a>
</div>
<div class="wrap split contact-more">
  <div><h2>Office</h2><address>{'<br>'.join(e(a) for a in ADDRESS)}</address><p>{HOURS}</p>
  <p><a class="link" href="https://www.google.com/maps/search/?api=1&amp;query=500-7030+Woodbine+Avenue+Markham+ON+L3R+6G2" target="_blank" rel="noopener noreferrer">Open in Google Maps →</a></p></div>
  <div><h2>Book a consultation</h2><p>Have questions? Book a consultation to get the right answers.</p>
  <p class="note">If you decide to retain our firm for any file work after your consultation, credit for the consultation fee will be applied towards your file.</p>
  <p><a class="btn" href="{BOOK}" target="_blank" rel="noopener noreferrer">Book now</a></p></div>
</div></section>"""
    page("contact/index.html", "Contact", "Contact Platinum Law Firm in Markham, Ontario: phone, email, WhatsApp, office address, and online booking.", body, "contact/")

    # Book online (keep old URL working)
    body = hero("Book online", "Consultation with a lawyer", "Have questions? Book a consultation to get the right answers.", small=True)
    body += f"""<section class="section"><div class="wrap prose narrow">
  <p>Our lawyers have extensive experience helping clients with mental health, business, real estate, wills and estates, and notary matters.</p>
  <p class="note">If you decide to retain our firm for any file work after your consultation, credit for the consultation fee will be applied towards your file.</p>
  <p><a class="btn" href="{BOOK}" target="_blank" rel="noopener noreferrer">Book now</a></p></div></section>"""
    page("book-online/index.html", "Book Online", "Book a consultation with a lawyer at Platinum Law Firm online.", body, "")

    # Privacy
    body = hero("Privacy", "Privacy notice", "How this website handles your information.", small=True, buttons=False)
    body += f"""<section class="section"><div class="wrap prose narrow">
  <p>This website does not use cookies, advertising trackers, or contact forms, and it does not collect personal information from visitors.</p>
  <p>If you call, email or message us on WhatsApp, we use the information you share only to respond to you and, if you become a client, to provide legal services. Information you share with us is kept confidential.</p>
  <p>Online booking is provided by Clio Grow, and WhatsApp chats are provided by WhatsApp. Information you enter on those services is handled under their own privacy policies.</p>
  <p>Questions about privacy? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></section>"""
    page("privacy/index.html", "Privacy", "Privacy notice for the Platinum Law Firm website.", body, "")

    # 404
    body = hero("Page not found", "Sorry, we couldn't find that page", "It may have moved. Try the home page or our list of services.", small=True, buttons=False)
    body += '<section class="section"><div class="wrap"><p><a class="btn" href="/">Go to the home page</a> <a class="btn btn-ghost-dark" href="/services/">See our services</a></p></div></section>'
    page("404.html", "Page not found", "Page not found.", body, "")

    # Old page that wasn't in the menu: send to business law
    redirect("ecommerce-law/index.html", "/business-law/")
    # Practice areas the firm no longer lists: send old links to the services page
    for old in ["immigration-law", "family-law", "employment-law"]:
        redirect(f"{old}/index.html", "/services/")

    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    urls = ["", "about/", "services/", "contact/", "book-online/", "attorney/titilope-olatunji/", "privacy/"] + [s["slug"] + "/" for s in SERVICES]
    (OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{DOMAIN}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    (OUT / "CNAME").write_text("www.platinumlawfirm.ca\n")
    (OUT / ".nojekyll").write_text("")

def redirect(path, to):
    p = OUT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f'<!doctype html><meta charset="utf-8"><title>Moved</title><meta http-equiv="refresh" content="0; url={to}"><link rel="canonical" href="{DOMAIN}{to}"><a href="{to}">This page has moved.</a>\n')

if __name__ == "__main__":
    import shutil
    if PREVIEW:
        shutil.rmtree(OUT, ignore_errors=True)
        shutil.copytree(ROOT / "css", OUT / "css")
        shutil.copytree(ROOT / "js", OUT / "js")
        shutil.copytree(ROOT / "assets", OUT / "assets")
    build()
    print("Built into", OUT)
