# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.
{
    'name': 'MPIN',
    'version': '9.0.1.0.0',
    'author': 'HBEE',
    'category': 'Human Resources',
    'website': 'https://hbee.eu/',
    'licence': 'AGPL-3',
    'summary': 'This module extend hr module with data required for the MPIN application.',
    'depends': [
        'hr_payroll',
        'hr_holidays',
        'hr_contract',
    ],
    'data': [
        'data/hr.types.seniority.insurance.csv',
        'data/hr.types.contribution.csv',
        'data/hr.designated.paying.authority.csv',
        'security/ir.model.access.csv',
        'views/hr.xml',
        'views/company.xml',
    ],
    'installable': True,
    'application': False,
}
