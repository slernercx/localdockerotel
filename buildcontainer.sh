# requires dockerhub login
sudo docker build . -f dockerfile -t otelcol
# sudo docker tag otelcolpy public.ecr.aws/w3s4j9x9/otelcolpy && \
# sudo docker push public.ecr.aws/w3s4j9x9/otelcolpy