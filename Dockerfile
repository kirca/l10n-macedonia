# Copyright (C) 2016 by HBEE <https://hbee.eu/>

FROM ubuntu:14.04

# All packages needed for running odoo
RUN apt-get update && apt-get -y -q install \
    postgresql-client-9.3 \ 
    build-essential \
    python-dev \
    python-pip \
    libpq-dev \
    libfreetype6-dev \
    libxml2-dev \
    libxslt1-dev \
    libjpeg62-dev \
    liblcms1-dev \
    libpng12-dev \
    libsasl2-dev \
    libssl-dev \
    libldap2-dev \
    fontconfig \
    libfontconfig1 \
    libjpeg-turbo8 \
    libxrender1 \
    xfonts-base \
    xfonts-75dpi \
    ca-certificates \
    git \
    wget \
    curl \
    socat \
    npm \
    unzip \
    vim && rm -rf /var/lib/apt/lists/*

RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture)" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture).asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu

RUN ln -s /usr/bin/nodejs /usr/bin/node && \ 
    npm install -g less less-plugin-clean-css

RUN wget http://download.gna.org/wkhtmltopdf/0.12/0.12.1/wkhtmltox-0.12.1_linux-trusty-amd64.deb && \
    dpkg -i wkhtmltox-0.12.1_linux-trusty-amd64.deb && rm wkhtmltox-0.12.1_linux-trusty-amd64.deb

RUN useradd --system -m -r -U odoo && \
    echo "odoo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

ENV HOME=/home/odoo \
    ODOO_COMMIT=4a0a2794720834a2737259bb1d278d69015ab4c5

WORKDIR $HOME
RUN wget -O odoo.zip https://github.com/odoo/odoo/archive/$ODOO_COMMIT.zip && \
    unzip -q odoo.zip && \
    mv odoo-$ODOO_COMMIT odoo && \
    rm odoo.zip && \
    chown -R odoo:odoo odoo 

RUN pip install --allow-external PyXML --allow-unverified PyXML -r odoo/requirements.txt \ 
    pyinotify \
    ipdb

RUN mkdir -p $HOME/addons_l10n-macedonia
COPY . $HOME/addons_l10n-macedonia
RUN cp $HOME/addons_l10n-macedonia/odoo.sh / && \
    chmod 777 /odoo.sh

ENV PGHOST=db \
    PGPORT=5432 \
    PGDATABASE=odoo \
    PGUSER=odoo \
    DB_TEMPLATE=template1 \
    LOG_LEVEL=critical

RUN chown -R odoo:odoo $HOME

EXPOSE 8069
ENTRYPOINT ["/odoo.sh"]
