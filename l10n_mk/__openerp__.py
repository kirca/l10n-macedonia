# -*- coding: utf-8 -*-
# This file is part of OpenERP. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.
{
    'name': 'Macedonian localization',
    'version': '9.0.1.0.0',
    'author': 'HBEE',
    'category': 'Localization',
    'website': 'http://www.hbee.eu',
    'summary': '',
    'description': """
Macedonian localization of accounts and taxes
""",
    'depends': [
        'account',
    ],
    'data': [
        'data/account.account.tag.csv',
        'data/account.account.type.csv',
        'data/account_chart_template.xml',
        'data/account.account.template.csv',
        'data/account_chart_tag.xml',
        'data/account.tax.template.csv',
        'data/fiscal_position_template.xml',
        'data/account_chart_template.yml',
        'views/report_account_invoice.xml',
    ],
    'installable': True,
    'application': False,
}
