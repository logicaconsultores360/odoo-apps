# -*- coding: utf-8 -*-
# © 2026 Lógica Consultores 360 — https://www.logicaconsultores.com
# License LGPL-3 or later (https://www.gnu.org/licenses/lgpl-3.0)
import logging

from odoo import http
from odoo.exceptions import AccessError
from odoo.http import request

_logger = logging.getLogger(__name__)

# Main invoice report shipped by the `account` module in Odoo 19.
INVOICE_REPORT_NAME = 'account.report_invoice'


class InvoicePreviewController(http.Controller):

    @http.route(
        '/account_invoice_preview/get_pdf/<int:move_id>',
        type='http',
        auth='user',
        methods=['GET'],
    )
    def get_invoice_pdf(self, move_id, **kwargs):
        """Render the invoice report as a PDF and stream it inline.

        Works for both draft and posted invoices: the report is rendered
        on the fly and never stored on the record, so the preview always
        reflects the data currently on screen.
        """
        move = request.env['account.move'].browse(move_id)
        if not move.exists():
            return request.make_response('Not found', status=404)

        # The user must be allowed to read the record they are previewing.
        try:
            move.check_access('read')
        except AccessError:
            return request.make_response('Forbidden', status=403)

        report_sudo = request.env['ir.actions.report'].sudo()
        invoice_report = report_sudo.search(
            [('report_name', '=', INVOICE_REPORT_NAME)], limit=1,
        )
        if not invoice_report:
            # Fallback: any PDF report bound to account.move (custom layouts).
            invoice_report = report_sudo.search([
                ('model', '=', 'account.move'),
                ('report_type', '=', 'qweb-pdf'),
            ], limit=1)

        if not invoice_report:
            return request.make_response('No invoice PDF report found.', status=500)

        try:
            pdf_content, _mime = report_sudo._render_qweb_pdf(
                invoice_report.report_name, res_ids=[move_id],
            )
        except Exception:
            _logger.exception('Error rendering invoice preview for move %s', move_id)
            return request.make_response('Error generating preview.', status=500)

        return request.make_response(pdf_content, headers=[
            ('Content-Type', 'application/pdf'),
            ('Content-Length', len(pdf_content)),
            ('Content-Disposition', f'inline; filename="preview_{move_id}.pdf"'),
        ])
