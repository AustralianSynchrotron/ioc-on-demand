Development
===========

While developing it is helpful to be able to modify the ioc code on the host
without restarting the container. This can be achieved by starting the container
with the `src` folder volume mapped as follows::

    docker run -it --rm --network pyepics-workshop --entrypoint=bash \
               --hostname APPLIANCE-12A -v $PWD/src:/ioc pyepics-workshop-ioc
