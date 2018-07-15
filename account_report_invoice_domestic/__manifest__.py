# Copyright (C) 2018 by Lambda IS <https://www.lambda-is.com>
{
    'name': 'Domestic Invoice',
    'category': 'Accounting',
    'author': 'Lambda IS DOOEL',
    'website': 'https://www.lambda-is.com',
    'license': 'AGPL-3',
    'summary': 'Print invoices in domestic language / currency',
    'version': '11.0.0.1.0',
    'description': '',
    'depends': [
        'account',
        'currency_rate_update_nbrm',
    ],
    'data': [
        'views/report_invoice_domestic.xml',
    ],
    'installable': True,
    'application': True,
}
