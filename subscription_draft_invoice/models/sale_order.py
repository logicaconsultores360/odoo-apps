from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _process_auto_invoice(self, invoice):
        """Skip auto-posting when Draft Invoicing is enabled on the plan.

        The native implementation calls invoice.action_post() unconditionally.
        When draft_invoicing is True we simply return without calling super(),
        leaving the invoice in Draft for manual review and confirmation.
        """
        if self.plan_id.draft_invoicing:
            return
        return super()._process_auto_invoice(invoice)
