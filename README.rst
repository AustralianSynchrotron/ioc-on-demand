Installation
============

1. Create network::

    docker network create --subnet=172.111.0.0/16 --gateway=172.111.0.1 pyepics-workshop

2. Configure ``ioc-dashboard``::

    cp ioc-dashboard/development.env ioc-dashboard/.env

3. Start services::

    docker-compose up -d
