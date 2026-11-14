# Platinum Law Firm website

Static website for **Platinum Law Firm** (Markham, Ontario), served by GitHub Pages at https://www.platinumlawfirm.ca.

- No WordPress, database, plugins or login page, so there is very little to attack.
- No cookies, trackers or forms. Bookings go to the firm's Clio Grow page; chat goes to WhatsApp.
- A strict Content Security Policy is set in every page.

## Editing

The pages are generated from one file, `tools/build.py`, which holds all the text (practice areas, biography, contact details).
Change the text there, then run:

```
python3 tools/build.py           # rebuilds the pages in this folder
PREVIEW=1 python3 tools/build.py # optional: builds preview/ with links that work when opened as plain files
```

Commit the result. GitHub Pages publishes `main` automatically.

## Domain and email

`CNAME` points GitHub Pages at `www.platinumlawfirm.ca`. Email for the domain runs on Google Workspace: when DNS moves, the MX, SPF and DKIM records must be copied exactly.
