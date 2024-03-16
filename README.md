Example of running Otel collector in an Ubuntu container with a Python app generating logs only.  
Logs are sent directly via Otel to Coralogix.  

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