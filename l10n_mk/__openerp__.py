# -*- coding: utf-8 -*-
# This file is part of OpenERP. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.
{
    'name': 'Macedonian localization',
    'version': '0.1',
    'author': 'HacBee UAB',
    'category': 'Custom',
    'website': 'http://www.hbee.eu',
    'summary': '',
    'description': """
Macedonian localization
""",
    'depends': [
        'account',
        'account_chart',
    ],
    'data': [
        'data/account.account.type.csv',
        'data/account.tax.code.template.csv',
        'data/account.account.template.csv',
        'data/l10n_mk_chart_template.xml',
        'data/l10n_mk_wizard.xml',
        'data/account.tax.template.csv',
    ],
    'installable': True,
    'application': False,
}
