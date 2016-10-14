# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.
{
    'name': 'Municipalities in R. Macedonia',
    'version': '9.0.1.0.0',
    'author': 'HBEE',
    'category': 'Localization',
    'website': 'https://hbee.eu/',
    'licence': 'AGPL-3',
    'summary': 'imports all municipalities from R. Macedonia',
    'depends': [
        'base',
    ],
    'data': [
        'data/res.country.state.csv',
        'views/res_country_state.xml',
    ],
    'installable': True,
    'application': False,
}
