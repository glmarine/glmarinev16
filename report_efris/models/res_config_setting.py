# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    tax_exempted = fields.Boolean(
        string="Withholding Tax Exempted",
        related="company_id.tax_exempted",
        store=True,
        readonly=False,
    )

    vat_withholding_tax_exempted = fields.Boolean(string="Vat Withholding Tax Exempted",
                                                  related="company_id.vat_withholding_tax_exempted",
                                                  store=True,
                                                  readonly=False, )
