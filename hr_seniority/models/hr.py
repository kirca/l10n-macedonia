# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.

from datetime import datetime, date
from dateutil.relativedelta import relativedelta

from openerp import fields, models, api, _
from openerp.exceptions import Warning
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    working_experience = fields.One2many(
        comodel_name='hr.working.experience',
        inverse_name='employee_id',
        string='working_experience')

    total_prior_years = fields.Integer(
        string='Total Prior Seniority Years',
        compute='_calc_total_prior_dates',
        default=0,
        readonly=True)

    total_prior_months = fields.Integer(
        string='Total Prior Seniority Months',
        compute='_calc_total_prior_dates',
        default=0,
        readonly=True)

    total_prior_days = fields.Integer(
        string='Total Prior Seniority Days',
        compute='_calc_total_prior_dates',
        default=0,
        readonly=True)

    total_current_years = fields.Integer(
        string='Total Current Company Seniority Years',
        compute='_calc_total_current_dates',
        default=0,
        readonly=True)

    total_current_months = fields.Integer(
        string='Total Current Company Seniority Months',
        compute='_calc_total_current_dates',
        default=0,
        readonly=True)

    total_current_days = fields.Integer(
        string='Total Current Company Seniority Days',
        compute='_calc_total_current_dates',
        default=0,
        readonly=True)

    total_years = fields.Integer(
        string='Total Seniority Years',
        compute='_calc_total_dates',
        default=0,
        readonly=True)

    total_months = fields.Integer(
        string='Total Seniority Months',
        compute='_calc_total_dates',
        default=0,
        readonly=True)

    total_days = fields.Integer(
        string='Total Seniority Days',
        compute='_calc_total_dates',
        default=0,
        readonly=True)

    @api.multi
    @api.depends('working_experience')
    def _calc_total_prior_dates(self):
        for employee in self:
            prior_exp = employee.working_experience.filtered(
                    lambda r: r.experience == 'prior_experience')

            employee.total_prior_years = sum(prior_exp.mapped('years'))
            employee.total_prior_months = sum(prior_exp.mapped('months'))
            employee.total_prior_days = sum(prior_exp.mapped('days'))

    @api.multi
    @api.depends('working_experience')
    def _calc_total_current_dates(self):
        for employee in self:
            current_exp = employee.working_experience.filtered(
                lambda r: r.experience == 'in_this_company')

            employee.total_current_years = sum(current_exp.mapped('years'))
            employee.total_current_months = sum(current_exp.mapped('months'))
            employee.total_current_days = sum(current_exp.mapped('days'))

    @api.multi
    @api.depends('working_experience')
    def _calc_total_dates(self):
        for employee in self:
            employee.total_years = sum(
                employee.working_experience.mapped('years'))
            employee.total_months = sum(
                employee.working_experience.mapped('months'))
            employee.total_days = sum(
                employee.working_experience.mapped('days'))


class HrWorkingExperience(models.Model):
    _name = "hr.working.experience"
    _description = "Working Experience"

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Employee')

    experience = fields.Selection([
        ('in_this_company', 'In this company'),
        ('prior_experience', 'Prior work experience'),
        ],
        string='Experience',
        index=True,
        default='in_this_company')

    job_id = fields.Many2one(
        comodel_name='hr.job',
        string='Job Position')

    start_date = fields.Date(
        string='Start Date')

    end_date = fields.Date(
        string='End Date')

    years = fields.Integer(
        string='Seniority Years',
        default=0)

    months = fields.Integer(
        string='Seniority Months',
        default=0)

    days = fields.Integer(
        string='Seniority Days',
        default=0)

    @api.multi
    @api.constrains('years', 'months', 'days')
    def _check_date_values(self):
        for working_exp in self:
            if working_exp.years < 0:
                raise Warning(_(
                    "The field 'Seniority Years' must have positive value"))
            elif working_exp.months < 0 or working_exp.months > 12:
                raise Warning(_(
                    "The field 'Seniority Months' must be in range from 1 to 12"))
            elif working_exp.days < 0 or working_exp.days > 31:
                raise Warning(_(
                    "The field 'Seniority Days' must be in range from 1 to 31"))

            if (not working_exp.end_date and
                len(working_exp.employee_id.working_experience.filtered(
                    lambda r: not r.end_date))) > 1:
                raise Warning(_(
                    "You can have only one ongoing work position."))

    @api.multi
    @api.onchange('start_date', 'end_date')
    def _calc_dates(self):
        for exp in self:
            end_date = exp.end_date and exp.end_date or fields.date.today()

            if not isinstance(end_date, date):
                end_date = datetime.strptime(end_date, DEFAULT_SERVER_DATE_FORMAT)

            if not exp.start_date:
                return

            start_date = datetime.strptime(
                exp.start_date, DEFAULT_SERVER_DATE_FORMAT)

            res = relativedelta(end_date, start_date)
            exp.years = res.years
            exp.months = res.months
            exp.days = res.days
