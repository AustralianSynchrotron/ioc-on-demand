Installation
============

1. Create network::

   docker network create \
      --subnet=172.111.0.0/16 \
      --gateway=172.111.0.1
      pyepics-workshop

2. Start services::

   docker-compose up -d
