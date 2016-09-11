#!/bin/bash

chown -R odoo.odoo /home/odoo
gosu odoo /home/odoo/odoo/odoo.py \
    --addons-path=/home/odoo/odoo/openerp/addons,/home/odoo/odoo/addons,/home/odoo/addons_l10n-macedonia \
    $@
