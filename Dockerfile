# Copyright (C) 2016 by HBEE <https://hbee.eu/>
# Copyright (C) 2018 by Lambda IS <https://www.lambda-is.com/>
FROM debian:stretch
LABEL odoo_version="11.0"

# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf
RUN set -x; \
        apt-get update \
        && apt-get install -y --no-install-recommends \
            build-essential \
            ca-certificates \
            curl \
            gnupg \
            node-less \
            python3-dev\
            python3-pip \
            python3-setuptools \
            python3-renderpm \
            python3-lxml \
            procps \
            libssl1.0-dev \
            libffi-dev \
            libsasl2-dev \
            libldap2-dev \
            libxtst6 libfontconfig1 libxrender1 \
            postgresql-client-9.6 \
            xz-utils \
            unzip \
            wget \
        && curl -o wkhtmltox.tar.xz -SL https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
        && echo '3f923f425d345940089e44c1466f6408b9619562 wkhtmltox.tar.xz' | sha1sum -c - \
        && tar xvf wkhtmltox.tar.xz \
        && cp wkhtmltox/lib/* /usr/local/lib/ \
        && cp wkhtmltox/bin/* /usr/local/bin/ \
        && cp -r wkhtmltox/share/man/man1 /usr/local/share/man/

# Install Odoo
ENV HOME=/home/odoo \
    ODOO_COMMIT=7d34f0218bf4ee04939e30c6101fb85323fccb71 \
    ODOO_GID=111
RUN groupadd -g $ODOO_GID odoo && \
    useradd --system --create-home -g $ODOO_GID odoo && \
    echo "odoo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

COPY ./requirements.txt /tmp/
RUN chown odoo:odoo /tmp/requirements.txt

USER odoo
WORKDIR $HOME
RUN wget -O odoo.zip https://github.com/odoo/odoo/archive/$ODOO_COMMIT.zip && \
    unzip -q odoo.zip && \
    mv odoo-$ODOO_COMMIT odoo && \
    rm odoo.zip

# Can't get correct dependencies to build lxml from source.
# Remove and install as system package (python3-lxml).
RUN grep -v lxml odoo/requirements.txt >> /tmp/requirements.txt && \
    pip3 install -r /tmp/requirements.txt
USER root

RUN ln -s $HOME/odoo/odoo-bin /usr/bin/odoo

# Install gosu to have a simple way of executing the server as a non-root user in the
# entrypoint script
RUN wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-architecture)" \
    && chmod +x /usr/local/bin/gosu

# Copy entrypoint script and Odoo configuration file
COPY ./entrypoint.sh /
COPY ./odoo.conf /etc/odoo/
RUN chown odoo:odoo /etc/odoo/odoo.conf

# Mount /var/lib/odoo to allow restoring filestore and /mnt/extra-addons for users addons
RUN mkdir -p /mnt/extra-addons /var/lib/odoo && \
    chown -R odoo:odoo /var/lib/odoo
VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]

# Expose Odoo services
EXPOSE 8069 8072

# Set the default config file
ENV ODOO_RC /etc/odoo/odoo.conf

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]
