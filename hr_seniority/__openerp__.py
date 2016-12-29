# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.
{
    'name': 'Employee Seniority',
    'version': '9.0.1.0.0',
    'author': 'HBEE',
    'category': 'Human Resources',
    'website': 'https://hbee.eu/',
    'licence': 'AGPL-3',
    'summary': 'Add new tab in the employee view with information about its seniority',
    'depends': [
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr.xml',
    ],
    'installable': True,
    'application': False,
}
