FROM pollen.hbee.eu/ubuntu_odoo:8.0

# Custom build environment variables
ENV ODOO_DIR=odoo \
	CLONE_DEPTH=1 \
	ODOO_VERSION=8.0 \
	PGDATABASE=l10n-macedonia \
	ODOO_COMMIT=1d269d20f25d29a791bedabc39cdf865215c9887

WORKDIR $ODOO_HOME
RUN wget -O odoo.zip https://github.com/odoo/odoo/archive/$ODOO_COMMIT.zip && \
	unzip -q odoo.zip && \
	mv odoo-$ODOO_COMMIT odoo && \
	rm odoo.zip && \
	chown -R odoo:odoo odoo 

# Specific addons needed for the project
# ======================================
# WORKDIR $ODOO_HOME
# USER odoo
# RUN git clone https://github.com/OCA/web.git $ODOO_HOME/web && cd $ODOO_HOME/web && git checkout -q SPECIFIC_COMMIT
# USER root
#
# Add directories which need to be included
# -----------------------------------------
# ENV CUSTOM_PATH $ODOO_HOME/web
#
# Apply a cache error fix
WORKDIR $ODOO_HOME/$ODOO_DIR

# Keep at end of dockerfile for caching purposes
COPY . $ODOO_HOME/c1
RUN chown -R odoo.odoo $ODOO_HOME

EXPOSE 8069
ENTRYPOINT ["/home/odoo/bootstrap.sh"]
CMD ["/bin/bash"]
