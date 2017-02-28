# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.


def convert_to_ymd(years, months, days):
    if days > 30:
        months += int(days/30)
        days %= 30

    if months > 12:
        years += int(months/12)
        months %= 12

    return years, months, days
