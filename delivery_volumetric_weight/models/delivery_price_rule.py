# -*- coding: utf-8 -*-
# © 2026 Lógica Consultores 360 — https://www.logicaconsultores.com
from odoo import fields, models


class DeliveryPriceRule(models.Model):
    _inherit = 'delivery.price.rule'

    variable = fields.Selection(
        selection_add=[('effective_weight', 'Effective Weight')],
        ondelete={'effective_weight': 'set default'},
    )
    variable_factor = fields.Selection(
        selection_add=[('effective_weight', 'Effective Weight')],
        ondelete={'effective_weight': 'set default'},
    )
