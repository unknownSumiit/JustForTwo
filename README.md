# Just Two Plates — recipes for two, for US adults 55+ (mobile-first)

Easy recipes that make two servings, designed for reading on iPhone and other phones (and still great on desktop).
Static HTML, AdSense-ready, deploys to **Azure Static Web Apps** from GitHub.

## What's included
- **20 recipes, all for two**, in 6 categories (Breakfast for Two, Fish & Seafood, Chicken Dinners, Beef & Pork,
  Soups & Salads, Desserts for Two), each with a real food photo (Unsplash, free licence). A few photos are close
  matches and are marked in `tools/photos.py`. Replace them with your own photos any time.
- **Dinners This Week** page: 7 dinners for two plus a printable shopping list that readers can check off on screen.
  Checked items are remembered on the reader's computer.
- **5 kitchen guides**: cooking for two tips, right-sized cookware, freezing meals for two,
  safe cooking temperatures, and pantry staples for two
- Policy pages for AdSense: About, Contact, Privacy Policy (Google AdSense cookie wording and US state privacy rights), Terms, Disclaimer
- Recipe + Breadcrumb JSON-LD, sitemap.xml, robots.txt, ads.txt, manifest, favicon/icons

## Features
- 19px base text on large screens, Text size button (3 steps), high contrast
- Recipe card with ingredients and steps side by side; ingredient list stays in view while you scroll
- "On this page" box and Reader favorites in a sticky sidebar
- **Print Recipe Card**: prints only the recipe, usually on a single Letter page, with no ads, photos or menus
- Half / 1× / 2× ingredient scaling, ingredient check-off, share button, recipe search
- Still fully responsive on tablets and phones

## Before publishing
Edit `SETTINGS` at the top of `tools/build.py` (site_url, contact_email, owner_name, adsense_client),
then run `python3 tools/build.py`.

## Photos
Photos load from Unsplash (images.unsplash.com) and are listed in `tools/photos.py`.
To use your own photo, save it as `site/assets/img/recipes/<recipe-slug>.jpg` and rebuild.
A local photo always replaces the Unsplash one.

## Deploy (Azure Static Web Apps + GitHub)
1. Push this folder to a new GitHub repository.
2. Azure Portal → Static Web App (Free) → GitHub source → Build preset **Custom**, App location `site`, Output location blank.
3. Azure adds the deploy token secret, and the included workflow publishes on every push.
4. Add your custom domain, then submit `/sitemap.xml` in Google Search Console.
5. Apply for AdSense once live. When approved, set `adsense_client` and rebuild (ads.txt updates automatically).

## Google Ads (Display) targeting suggestions
- Location: United States; Language: English
- Demographics → Age: **55–64** and **65+**
- Devices: **Mobile phones** (optionally Operating system: iOS); set Computers and Tablets to −100% for phone-only
- Audiences: Cooking Enthusiasts, Food & Dining; custom segments with keywords like
  "recipes for two", "dinner for two", "cooking for two", "small batch dessert"
- Phones show square and landscape images; upload both **1200×1200 and 1200×628** images. Use the recipe photos and the logos in `brand/out/`
  (`brand/gdn/just-two-plates-gdn-logo-square-1200x1200-white.png` and `...-landscape-1200x300-white.png`).

## Folder layout
```
site/            ← published website
tools/build.py   ← generator & settings
tools/content_recipes.py, content_recipes2.py, content_articles.py, photos.py
brand/           ← logo source & PNG/SVG files (including Google Ads logos)
```
