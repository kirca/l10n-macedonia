# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.

from openerp import fields, models, api, _
from openerp.exceptions import Warning
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT


class TypesSeniorityInsurance(models.Model):
    _name = "hr.types.seniority.insurance"
    _description = "Types of seniority for insurance"

    name = fields.Char(string='Name', size=4)
    description = fields.Char(string='Description', size=256)


class TypesContribution(models.Model):
    _name = "hr.types.contribution"
    _description = "Types of contribution"

    name = fields.Char(string='Name', size=4)
    description = fields.Char(string='Description', size=256)


class DesignatedPayingAuthority(models.Model):
    _name = "hr.designated.paying.authority"
    _description = "Designated paying authority"

    name = fields.Char(string='Name', size=4)
    description = fields.Char(string='Description', size=256)


class HrHolidaysStatus(models.Model):
    _inherit = "hr.holidays.status"

    contribution_id = fields.Many2one(
        comodel_name='hr.types.contribution',
        string='Type of contribution')

    paying_authority_id = fields.Many2one(
        comodel_name='hr.designated.paying.authority',
        string='Designated paying authority')


class HrContract(models.Model):
    _inherit = "hr.contract"

    insurance_seniority_id = fields.Many2one(
        comodel_name='hr.types.seniority.insurance',
        string='Type of seniority for insurance')
