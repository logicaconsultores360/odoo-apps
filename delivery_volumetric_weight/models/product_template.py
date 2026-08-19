# -*- coding: utf-8 -*-
# © 2026 Lógica Consultores 360 — https://www.logicaconsultores.com
from odoo import api, fields, models

DEFAULT_VOLUMETRIC_DIVISOR = 5000.0


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # ------------------------------------------------------------------
    # Dimension fields (cm).  Odoo only ships weight & volume on the
    # product template; length / width / height are not native fields.
    # ------------------------------------------------------------------
    product_length = fields.Float(
        string='Length (cm)',
        digits='Stock Weight',
        help='Length of the packed product, in centimetres.',
    )
    product_width = fields.Float(
        string='Width (cm)',
        digits='Stock Weight',
        help='Width of the packed product, in centimetres.',
    )
    product_height = fields.Float(
        string='Height (cm)',
        digits='Stock Weight',
        help='Height of the packed product, in centimetres.',
    )
    volumetric_divisor = fields.Float(
        string='Volumetric Divisor',
        default=DEFAULT_VOLUMETRIC_DIVISOR,
        digits=(16, 2),
        help='Divisor used to convert cm³ into kg. Carriers publish their own '
             'value: 5000 is the most common for road and express freight, '
             '6000 is often used for air freight. Set it to 0 to disable the '
             'volumetric weight for this product.',
    )

    # ------------------------------------------------------------------
    # Volumetric weight — computed & stored
    # ------------------------------------------------------------------
    volumetric_weight = fields.Float(
        string='Volumetric Weight (kg)',
        compute='_compute_volumetric_weight',
        store=True,
        readonly=True,
        digits='Stock Weight',
        help='(Length × Width × Height) / Volumetric Divisor. Dimensions are '
             'expressed in centimetres and the result in kilograms.',
    )

    @api.depends('product_length', 'product_width', 'product_height', 'volumetric_divisor')
    def _compute_volumetric_weight(self):
        for product in self:
            divisor = product.volumetric_divisor or 0.0
            if divisor <= 0.0:
                product.volumetric_weight = 0.0
                continue
            volume_cm3 = (
                (product.product_length or 0.0)
                * (product.product_width or 0.0)
                * (product.product_height or 0.0)
            )
            product.volumetric_weight = volume_cm3 / divisor
