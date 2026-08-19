# -*- coding: utf-8 -*-
# © 2026 Lógica Consultores 360 — https://www.logicaconsultores.com
from odoo import models

# Product types that never ship, and therefore never weigh anything.
NON_SHIPPABLE_TYPES = {'service', 'combo'}


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    def _get_price_available(self, order):
        """Compute the chargeable ("effective") weight of the order and pass it
        down to the price-rule evaluation.

        For every order line the effective weight is the greater of the real
        weight and the volumetric weight of the product, which is how carriers
        actually bill oversized but light parcels.
        """
        self.ensure_one()
        order_sudo = order.sudo()
        effective_weight = 0.0

        for line in order_sudo.order_line:
            if line.state == 'cancel':
                continue
            if not line.product_id or line.is_delivery:
                continue
            if line.product_id.type in NON_SHIPPABLE_TYPES:
                continue

            qty = line.product_uom_id._compute_quantity(
                line.product_uom_qty, line.product_id.uom_id,
            )
            real_weight = line.product_id.weight or 0.0
            volumetric_weight = line.product_id.volumetric_weight or 0.0
            effective_weight += max(real_weight, volumetric_weight) * qty

        # Passed through the context so that _get_price_dict can add it to the
        # dictionary the price rules are evaluated against.
        return super(
            DeliveryCarrier,
            self.with_context(effective_weight=effective_weight),
        )._get_price_available(order)

    def _get_price_dict(self, total, weight, volume, quantity, wv=0.):
        """Extend the price-rule evaluation dictionary with `effective_weight`.

        Odoo documents this method as the hook for adding custom variables to
        delivery price rules. When the effective weight is not in the context —
        for instance when the price is computed from a picking rather than from
        a sale order — it falls back to the plain weight, so existing rules keep
        working unchanged.
        """
        price_dict = super()._get_price_dict(total, weight, volume, quantity, wv=wv)
        price_dict['effective_weight'] = self.env.context.get('effective_weight', weight)
        return price_dict
