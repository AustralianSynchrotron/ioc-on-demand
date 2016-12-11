FROM python:3.6
WORKDIR /app
COPY setup.py /app/
COPY ioc_launcher /app/ioc_launcher/
RUN pip install -e .
ENTRYPOINT ["ioc-launcher"]
