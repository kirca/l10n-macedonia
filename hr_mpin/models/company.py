# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.

from openerp import fields, models, api, _
from openerp.exceptions import Warning
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT


class ResCompany(models.Model):
    _inherit = 'res.company'

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Authorized signer')

    regional_unit = fields.Char(
        string='Regional Unit',
        size=4)
