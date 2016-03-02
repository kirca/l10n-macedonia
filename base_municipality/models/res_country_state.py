# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.

from openerp import fields, models


class ResCountryState(models.Model):
    _inherit = 'res.country.state'

    zip_code = fields.Char('Zip code', size=4)
