{
    'name': "Report Extended",
    'summary': """Efris Report Extended""",
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Accounting/Accounting',
    'version': '0.2.4',
    # 'efris_integration'
    'depends': ['account'],
    'data': [
        # 'views/report_invoice_extended_css.xml',
        'views/res_company_inherit_view.xml',
        'views/report_invoice_extended.xml',
        'views/report_invoice_extended_template.xml',
        'views/res_config_settings_views.xml',
    ],
    'images': ['/static/src/img/bg.png'],
    'assets': {
        'web.report_assets_common': [
            'report_efris/static/src/css/report_invoice_extended.css',
        ],
    },
}
