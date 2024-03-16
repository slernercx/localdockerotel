FROM python:slim
RUN apt-get update && apt-get install -y wget && apt-get -y install vim && rm -rf /var/lib/apt/lists/* && apt-get autoclean && apt-get autoremove
WORKDIR /app
RUN wget https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.96.0/otelcol-contrib_0.96.0_linux_amd64.tar.gz

RUN tar -xzf otelcol-contrib_0.96.0_linux_amd64.tar.gz

RUN rm otelcol-contrib_0.96.0_linux_amd64.tar.gz

COPY entrypoint.sh /app/entrypoint.sh
COPY main.py .
COPY config.yaml .
RUN chmod +x /app/*
ENTRYPOINT ["/app/entrypoint.sh"]