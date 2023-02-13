from odoo import fields, models


class ResCompanyInherit(models.Model):
    _inherit = 'res.company'

    report_header_layout_img = fields.Image(string='Report Header Layout Image')
    tax_exempted = fields.Boolean(string="Tax Exempted")

    vat_withholding_tax_exempted = fields.Boolean(string="Vat Withholding Tax Exempted")
    is_watermark = fields.Boolean("Watermark")
