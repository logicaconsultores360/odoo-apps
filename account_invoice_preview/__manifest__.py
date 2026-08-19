# -*- coding: utf-8 -*-
# © 2026 Lógica Consultores 360 — https://www.logicaconsultores.com
# License LGPL-3 or later (https://www.gnu.org/licenses/lgpl-3.0)
{
    'name': 'Invoice PDF Live Preview',
    'version': '19.0.1.0.0',
    'summary': 'See the invoice PDF while you edit it, in a side panel, without printing',
    'description': """
Invoice PDF Live Preview
========================
Adds a **PDF Preview** button to invoices, bills, credit notes and receipts.
The report is rendered on the fly and displayed in a side panel next to the
form, so you can check the layout, the customer data and the totals **before**
posting or sending anything.

Features
--------
* Works on draft documents — no need to post the invoice first
* One-click **Refresh** to re-render the PDF after any change
* Nothing is stored on the record: no stray attachments in the chatter
* Uses the invoice report configured in your database, so your custom layout
  is what you see
* Respects record access rights: users only preview what they may read
    """,
    'author': 'Lógica Consultores 360',
    'website': 'https://www.logicaconsultores.com',
    'support': 'info@logicaconsultores.com',
    'category': 'Accounting/Accounting',
    'sequence': 10,
    'depends': ['account', 'mail', 'web'],
    'data': [
        'views/account_move_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'account_invoice_preview/static/src/css/invoice_preview.css',
            'account_invoice_preview/static/src/components/invoice_preview_panel/invoice_preview_panel.js',
            'account_invoice_preview/static/src/components/invoice_preview_panel/invoice_preview_panel.xml',
        ],
    },
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
