# -*- coding: utf-8 -*-
# © 2026 Lógica Consultores 360 — https://www.logicaconsultores.com
{
    'name': 'Hide Attribute Values from eCommerce Filters',
    'version': '19.0.1.0.0',
    'summary': 'Choose, value by value, which attribute values appear in the shop filters',
    'description': """
Hide Attribute Values from eCommerce Filters
============================================
Your product attributes are not only there for customers. Internal sizes,
supplier references, legacy colours, technical grades — they all end up in the
shop's left-hand filter panel, next to the ones that actually help someone buy.

This module adds a single **Visible in eCommerce** toggle on each attribute
value. Untick it and the value disappears from the shop filters, while the
products carrying it keep selling exactly as before.

Features
--------
* One toggle per attribute value, right in the attribute form
* Applies to every filter layout Odoo ships: pills, colours, images, select,
  radio and multi-checkbox
* An attribute left with a single visible value is hidden from the filter
  panel altogether, instead of showing a useless one-option filter
* Nothing else changes: product pages, variants, pricing and the back office
  are untouched
    """,
    'author': 'Lógica Consultores 360',
    'website': 'https://www.logicaconsultores.com',
    'support': 'info@logicaconsultores.com',
    'category': 'Website/eCommerce',
    'sequence': 10,
    'depends': ['website_sale'],
    'data': [
        'views/product_attribute_views.xml',
        'views/website_sale_templates.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'auto_install': False,
}
