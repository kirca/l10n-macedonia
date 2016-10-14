#!/bin/bash

# Set the permissions right if its mounted directory,
# do not fail if it does not exist
chown -f -R odoo.odoo /home/odoo/.local || true

gosu odoo /home/odoo/odoo/odoo.py \
    --addons-path=/home/odoo/odoo/openerp/addons,/home/odoo/odoo/addons,/home/odoo/addons_l10n-macedonia \
    $@
