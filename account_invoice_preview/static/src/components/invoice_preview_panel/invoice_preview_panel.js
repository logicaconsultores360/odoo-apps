/** @odoo-module **/

import { Component, useState, onWillStart, onMounted } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";

export class InvoicePreviewPanel extends Component {
    static template = "account_invoice_preview.InvoicePreviewPanel";
    static props = ["*"];

    setup() {
        this.state = useState({
            visible: false,
            loading: false,
            pdfUrl: null,
            error: null,
            ts: 0,
        });
        this.notification = useService("notification");
        this._t = _t
    }

    get moveId() {
        return this.props.record.resId;
    }

    get canPreview() {
        return this.moveId && this.moveId > 0;
    }

    _buildUrl() {
        return `/account_invoice_preview/get_pdf/${this.moveId}?ts=${Date.now()}`;
    }

    togglePreview() {
        if (!this.canPreview) {
            this.notification.add(
                _t("Save the invoice before previewing it."),
                { type: "warning" }
            );
            return;
        }
        if (this.state.visible) {
            this.closePreview();
        } else {
            this.openPreview();
        }
    }

    openPreview() {
        this.state.visible = true;
        this.state.loading = true;
        this.state.error = null;
        this.state.pdfUrl = this._buildUrl();
        this.state.ts = Date.now();
    }

    closePreview() {
        this.state.visible = false;
        this.state.pdfUrl = null;
    }

    refreshPreview() {
        if (!this.canPreview) return;
        this.state.loading = true;
        this.state.error = null;
        this.state.pdfUrl = this._buildUrl();
        this.state.ts = Date.now();
    }

    onIframeLoad() {
        this.state.loading = false;
    }

    onIframeError() {
        this.state.loading = false;
        this.state.error = _t("The PDF preview could not be generated.");
    }
}

registry.category("view_widgets").add("invoice_preview_button", {
    component: InvoicePreviewPanel,
});
