# Lógica Consultores 360 — Odoo Apps

Modules published (or being prepared) on the **Odoo App Store** for **Odoo 19**.

Everything here is extracted from the internal development library
(`rebersasoluciones/biblioteca-logica`), generalised, translated to English as
source language, and packaged with the store assets each listing needs.

## Published / ready to publish

| Module | Category | Depends on | Status |
| --- | --- | --- | --- |
| `subscription_draft_invoice` | Sales / Subscriptions | `sale_subscription` (EE) | Published |
| `account_invoice_preview` | Accounting | `account` | Ready |
| `delivery_volumetric_weight` | Inventory / Delivery | `delivery` | Ready |
| `website_sale_attribute_filter_visibility` | Website / eCommerce | `website_sale` | Ready |
| `attendance_quicklink` | Human Resources | `hr_attendance` | Draft (branch `fichajes`) |

## What "ready to publish" means here

A module is only listed as *Ready* once all of the following hold:

1. **Generic.** No client name, no client-specific field, no dependency on a
   customer's Studio customisation or on a third-party paid module.
2. **Self-contained.** Depends only on standard Odoo modules.
3. **English source language**, with an `i18n/es.po` Spanish translation.
4. **Verified against the Odoo 19 source** — every inherited view, XPath anchor,
   external ID and overridden method checked against the 19.0 codebase, and no
   deprecated ORM API (`check_access_rights`, `odoo.osv.expression`, …).
5. **Store assets complete** — `static/description/index.html`,
   `icon.png` (128×128), `banner.png` (1200×900), plus the `.svg` sources so the
   artwork can be regenerated or restyled.
6. **Manifest complete** — `name`, `version` (`19.0.x.y.z`), `summary`,
   `description`, `author`, `website`, `support`, `category`, `license`,
   `images`.

## Store assets

Listing pages share one house stylesheet (navy `#0f3460` / orange `#e8431a`,
identical section structure). Icons and banners are authored as SVG and
rasterised with `cairosvg`:

```bash
python3 -c "import cairosvg; cairosvg.svg2png(url='icon.svg',   write_to='icon.png',   output_width=128,  output_height=128)"
python3 -c "import cairosvg; cairosvg.svg2png(url='banner.svg', write_to='banner.png', output_width=1200, output_height=900)"
```

## Licensing

Store modules are shipped under **OPL-1**, matching the first published listing.
Their counterparts in the internal library keep the licence they were written
under; relicensing is possible because Lógica Consultores 360 owns the code.
