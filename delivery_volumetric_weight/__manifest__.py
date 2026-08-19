# -*- coding: utf-8 -*-
# © 2026 Lógica Consultores 360 — https://www.logicaconsultores.com
{
    'name': 'Delivery Volumetric Weight',
    'version': '19.0.1.1.0',
    'summary': 'Charge shipping on the weight carriers actually bill: the greater of real and volumetric weight',
    'description': """
Delivery Volumetric Weight
==========================
Carriers do not bill the weight of a parcel, they bill the **chargeable
weight**: whichever is greater between the real weight and the volumetric
weight derived from its dimensions. A box of cushions weighs almost nothing
and still takes a full pallet slot — and you get invoiced for the slot.

Odoo price rules only know about real weight, so light-but-bulky orders are
systematically undercharged. This module closes that gap.

What it adds
------------
* **Length / Width / Height** (cm) on the product, plus a per-product
  **Volumetric Divisor** (5000 by default, 6000 for air freight, and so on)
* A stored **Volumetric Weight** field, recomputed whenever a dimension changes
* A new **Effective Weight** variable available in delivery price rules —
  the sum, over the order lines, of `max(real weight, volumetric weight) × qty`

Set up your carrier's price rules on *Effective Weight* instead of *Weight*
and shipping is quoted exactly the way your carrier will invoice it.
    """,
    'author': 'Lógica Consultores 360',
    'website': 'https://www.logicaconsultores.com',
    'support': 'info@logicaconsultores.com',
    'category': 'Inventory/Delivery',
    'sequence': 10,
    'depends': ['delivery'],
    'data': [
        'views/product_template_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'auto_install': False,
}
