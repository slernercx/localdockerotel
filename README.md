Example of running Otel collector in an Ubuntu container with a Python app generating logs only.  
Logs are sent directly via Otel to Coralogix.  
The deployment script reads the `config.yaml` file when the docker container launches so you can configure it and relaunch the container without having to rebuild it.  

1. Configure `config.yaml` with your domain and key  
2. Build the container:  
```
source buildcontainer.sh  
```
3. Deploy container to generate logs:  
```
source deploy.sh  
```
4. Delete running container instance:  
```
source delete.sh
```

Experiment with various log configs in the `config.yaml` file and then re-deploy container.  
