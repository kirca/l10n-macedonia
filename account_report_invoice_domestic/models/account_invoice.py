# Copyright (C) 2018 by Lambda IS <https://www.lambda-is.com/>

from odoo import api, models, fields
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo.addons.currency_rate_update_nbrm.services.update_service_MK_NBRM import MK_NBRMGetter
from datetime import datetime


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def get_currency_rate(self):
        self.ensure_one()
        currency_getter = MK_NBRMGetter()
        date_invoice = self.date_invoice or fields.Date.today()
        date_invoice_fmt = datetime.strptime(
            date_invoice, DEFAULT_SERVER_DATE_FORMAT).strftime('%d.%m.%Y')
        return (self
                .currency_id
                .rate_ids
                .filtered(
                    lambda rate: rate.name == date_invoice)[:1].rate
                or
                currency_getter.get_updated_currency(
                    [self.currency_id.name], 'MKD',
                    999, date_invoice_fmt)[0][self.currency_id.name])
