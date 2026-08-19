# -*- coding: utf-8 -*-
# © 2026 Lógica Consultores 360 — https://www.logicaconsultores.com
from odoo import fields, models


class ProductAttribute(models.Model):
    _inherit = 'product.attribute'

    website_value_ids = fields.One2many(
        comodel_name='product.attribute.value',
        inverse_name='attribute_id',
        string='Values shown in eCommerce filters',
        domain=[('website_visible', '=', True)],
        help='Subset of the attribute values that the shop filters display.',
    )
