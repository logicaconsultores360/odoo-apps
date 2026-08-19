# -*- coding: utf-8 -*-
# © 2026 Lógica Consultores 360 — https://www.logicaconsultores.com
from odoo import fields, models


class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'

    website_visible = fields.Boolean(
        string='Visible in eCommerce',
        default=True,
        help='When unchecked, this value is hidden from the shop filters. '
             'Products carrying it are still sold normally and the value is '
             'still shown on the product page and in the back office.',
    )
