FROM python

ADD metric_ingester /opt/metric_ingester

RUN pip install -r /opt/metric_ingester/requirements.txt

WORKDIR /opt/metric_ingester/

CMD python app.py