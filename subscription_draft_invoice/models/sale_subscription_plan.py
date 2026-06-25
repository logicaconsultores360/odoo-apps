from odoo import fields, models


class SaleSubscriptionPlan(models.Model):
    _inherit = 'sale.subscription.plan'

    draft_invoicing = fields.Boolean(
        string='Draft Invoicing',
        help='When enabled, invoices generated automatically by the subscription '
             'scheduler will remain in Draft state instead of being posted immediately.',
    )
