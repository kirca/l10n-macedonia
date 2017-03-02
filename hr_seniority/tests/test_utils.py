# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.

from openerp.tests import common
from ..models.utils import convert_to_ymd


class TestUtils(common.TransactionCase):
    def test_convert_ymd(self):
        years = 5
        months = 18
        days = 45
        converted_years, converted_months, converted_days = \
            convert_to_ymd(years, months, days)
        self.assertEqual(converted_years, 6)
        self.assertEqual(converted_months, 7)
        self.assertEqual(converted_days, 15)

    def test_no_need_to_convert_ymd(self):
        years = 5
        months = 12
        days = 29
        converted_years, converted_months, converted_days = \
            convert_to_ymd(years, months, days)
        self.assertEqual(converted_years, years)
        self.assertEqual(converted_months, months)
        self.assertEqual(converted_days, days)
