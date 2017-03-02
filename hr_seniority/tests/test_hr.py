# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.

from datetime import datetime, timedelta
from openerp.tests import common
from openerp.exceptions import ValidationError


class TestHrWorkingExperience(common.TransactionCase):

    def setUp(self):
        super(TestHrWorkingExperience, self).setUp()
        self.work_experience = self.env['hr.working.experience']
        self.user = self.env['res.users']
        self.main_company = self.env.ref('base.main_company')
        res_hr_user = self.env.ref('base.group_user')

        self.hr_user = self.user.create(dict(
            name="Normal User/Employee",
            company_id=self.main_company.id,
            login="emp",
            password="emp",
            email="empuser@yourcompany.example.com",
            groups_id=[(6, 0, [res_hr_user.id])]
        ))
        self.employee = self.env.ref('hr.employee_qdp')
        self.employee.write({'user_id': self.hr_user.id})

        self.job_developer = self.env.ref('hr.job_developer')
        self.job_consultant = self.env.ref('hr.job_consultant')

    def test_check_date_values(self):
        expirience_data = {
            'employee_id': self.employee.id,
            'experience': 'in_this_company',
            'job_id': self.job_developer.id}

        # Case 1: Start Date not entered
        with self.assertRaises(ValidationError) as ex:
            self.work_experience.create(expirience_data)
        self.assertEqual(ex.exception.name, u"Error while validating constraint\n\nYou need to enter 'Start Date' or length of your work experience at this position.\nNone")

        # Case 2: Two ongoing jobs
        expirience_data.update({'start_date': (datetime.today() - timedelta(days=1))})
        self.work_experience.create(expirience_data)
        with self.assertRaises(ValidationError) as ex:
            expirience_data.update({'start_date': (datetime.today()),
                                    'job_id': self.job_consultant.id})
            self.work_experience.create(expirience_data)
        self.assertEqual(ex.exception.name, u"Error while validating constraint\n\nYou can have only one ongoing work position.\nNone")

        # Case 3: Years < 0
        expirience_data.update({'start_date': False})
        with self.assertRaises(ValidationError) as ex:
            expirience_data.update({'years': -1})
            self.work_experience.create(expirience_data)
        self.assertEqual(ex.exception.name, u"Error while validating constraint\n\nThe field 'Seniority Years' must have positive value\nNone")

        # Case 4: Months < 0
        with self.assertRaises(ValidationError) as ex:
            expirience_data.update({'years': 1, 'months': -1})
            self.work_experience.create(expirience_data)
        self.assertEqual(ex.exception.name, u"Error while validating constraint\n\nThe field 'Seniority Months' must be in range from 1 to 12\nNone")

        # Case 5: Months > 12
        with self.assertRaises(ValidationError) as ex:
            expirience_data.update({'years': 1, 'months': 14})
            self.work_experience.create(expirience_data)
        self.assertEqual(ex.exception.name, u"Error while validating constraint\n\nThe field 'Seniority Months' must be in range from 1 to 12\nNone")

        # Case 6: Days < 0
        with self.assertRaises(ValidationError) as ex:
            expirience_data.update({'years': 1, 'months': 12, 'days': -2})
            self.work_experience.create(expirience_data)
        self.assertEqual(ex.exception.name, u"Error while validating constraint\n\nThe field 'Seniority Days' must be in range from 1 to 31\nNone")

        # Case 7: Days > 31
        with self.assertRaises(ValidationError) as ex:
            expirience_data.update({'years': 1, 'months': 12, 'days': 32})
            self.work_experience.create(expirience_data)
        self.assertEqual(ex.exception.name, u"Error while validating constraint\n\nThe field 'Seniority Days' must be in range from 1 to 31\nNone")

    def test_create_work_experience(self):
        expirience_data = {
            'employee_id': self.employee.id,
            'experience': 'prior_experience',
            'job_id': self.job_developer.id,
            'years': 1,
            'months': 12,
            'days': 30}

        work_exp = self.work_experience.create(expirience_data)
        self.assertIsInstance(work_exp, type(self.work_experience))

        self.assertEqual(work_exp.employee_id.id, self.employee.id)
        self.assertEqual(work_exp.job_id.id, self.job_developer.id)
        self.assertEqual(work_exp.experience, 'prior_experience')
        self.assertEqual(work_exp.years, 1)
        self.assertEqual(work_exp.months, 12)
        self.assertEqual(work_exp.days, 30)

    def test_calc_dates(self):
        expirience_data_1 = {
            'employee_id': self.employee.id,
            'experience': 'prior_experience',
            'job_id': self.job_developer.id,
            'years': 3,
            'months': 12,
            'days': 30}

        expirience_data_2 = {
            'employee_id': self.employee.id,
            'experience': 'prior_experience',
            'job_id': self.job_developer.id,
            'years': 1,
            'months': 2,
            'days': 10}

        self.work_experience.create(expirience_data_1)
        self.work_experience.create(expirience_data_2)

        self.assertEqual(self.employee.total_prior_years, 5)
        self.assertEqual(self.employee.total_prior_months, 3)
        self.assertEqual(self.employee.total_prior_days, 10)
        self.assertEqual(self.employee.total_years, 5)
        self.assertEqual(self.employee.total_months, 3)
        self.assertEqual(self.employee.total_days, 10)
