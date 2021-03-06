Odoo локализациски модули за Р. Македонија
====================================================

Целта на овој проект е подобра интеграција на [Odoo](https://github.com/odoo/odoo) со
законските регулативи и практики во македонското стопанство.

Развојна околина
------------------
За развивање и тестирање треба да се користи вклучената Docker
конфигурација. Потребно е [Docker Engine 1.10.0+](https://docs.docker.com/) и [Docker Compose 1.6.0+](https://docs.docker.com/compose/overview/).

        git clone https://github.com/kirca/l10n-macedonia.git
        cd l10n-macedonia
        docker-compose up

Доколку се е успешно Odoo ќе биде достапен на [localhost:8069](http://localhost:8069)

Придонесување
---------------

Придонесите треба го следат **OCA** (Odoo Community Association) [водичот](https://github.com/OCA/maintainer-tools/blob/master/CONTRIBUTING.md). Основен начин на контрибуција е **Pull Request** што решава отворено **Issue**. 

Сите Pull Requests се добредојдени но, најдобро е прво да се искомуницира проблемот кој ќе се решава преку ново или веќе постоечко Issue. Со ова ќе се избегне дуплирање на имплементации, имплементирање на несоодветни барање за проектот итн. Сите промени треба да може да се тестираат со Docker. Така што, доколку имплементацијата користи нешто што не е достапно, на пр. Linux/Python пакети/библиотеки, тоа треба да бидe додаденo во Dockerfile. 
