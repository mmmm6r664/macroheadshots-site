# Macro Headshots website

Static copy of macroheadshots.com (Home, Appointments, Pricing and 16 local-area pages),
with every image hosted in `assets/`. The appointment form is the live HighLevel form embed,
so submissions still reach the CRM. Deploys on Vercel as a plain static site (no build step).

`tools/build.py` regenerates the site from a browser capture of the original (`python3 tools/build.py capture.json out/`).
