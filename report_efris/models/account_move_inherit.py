from odoo import api, fields, models


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'


class ReportInvoiceWithPaymentExtended(models.AbstractModel):
    _name = 'report.report_efris.report_invoice_with_payment_extended'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['account.move'].browse(docids)
        loop = [item for item in range(0, 9)]
        parent_lines = [[]]
        is_line = True
        if docs.invoice_line_ids:
            parent_lines = [docs.invoice_line_ids[i * 10: (i + 1) * 10] for i in
                            range((len(docs.invoice_line_ids) + 9) // 10)]
            loop_int = 10 - len(parent_lines[-1])
            loop = [item for item in range(0, loop_int)]
            is_line = False
        return {
            'doc_ids': docs.ids,
            'doc_model': 'invoice.with.payment.extended',
            'docs': docs,
            'inv_lines': parent_lines,
            'loop': loop,
            'is_line': is_line,
        }
