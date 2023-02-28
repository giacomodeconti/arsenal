# Configuration of an Deployment Server
![](https://github.com/giacomodeconti/arsenal/blob/main/Splunk/Deployment%20Server%20intro.jpg)
![](https://github.com/giacomodeconti/arsenal/blob/main/Splunk/Deployment%20Server.jpg)

# Step 1
## Configuration of Deployment Server on Indexer 
### Indexer Configuration
1. Add an random app in 
`/opt/splunk/etc/deployment-apps/`
2. Indexer home page, go to setting, Forwarder Management

# Step 2
## Configuration of Forwarder to comminucate with Deployment Server
### Forwarder Configuration
1. Download the app from [here](https://github.com/giacomodeconti/arsenal/tree/main/Splunk/Splunk%20APPs/deployment_client_1min "app"), or make it from zero
2. Go to local and edit `deploymentclient.conf` IP with your Indexer server IP or Deplyment Server IP
3. Also you can change the `phoneHomeIntervalInSecs` with more or less seconds. **In real case scenario up to 10 minutes**
4. Restart Splunk Forwarder and wait the time you have configured

# Step 3
## Management of all Forwarder
### Usege of Deployment Server
1. Create and modify an App and move it under `/opt/splunk/etc/deployment-apps/`
2. Create New Server Class under Server Class option
3. Select the app you want to deploy and select the forwarders
4. Deploy it and wait some minutes
5. Check in a Forwarder if the app persist under `/opt/splunkforwarder/etc/apps/`
6. Done
