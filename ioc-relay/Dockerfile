FROM australiansynchrotron/epics:centos7-python3.5.2
WORKDIR /app
COPY setup.py /app/
COPY ioc_relay /app/ioc_relay/
RUN pip3 install -e .
ENTRYPOINT ["ioc-relay"]
