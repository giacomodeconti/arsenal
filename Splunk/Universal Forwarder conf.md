# Configuration of an Universal Forwarder on Linux
## An Universal Forwarder can act like a Proxy
![](https://github.com/giacomodeconti/arsenal/blob/main/Splunk/Universal%20Forwarder.jpg)

### Configuration
1. Make a new app in /opt/splunkforwarder/etc/apps/
2. Go to local/default directory 
3. In outputs.conf simply connect to Indexer:
  - **outputs.conf** remeber to change IP
    ```
    [tcpout]
    defaultGroup = default-autolb-group

    [tcpout:default-autolb-group]
    server = 192.168.1.100:9997

    [tcpout-server://192.168.1.100:9997]
    ```
4. In inputs.conf need to use udp protocol to get connections and queue config to avoid diconnections and data loss:
  - **inputs.conf** remember to change this config with your settings:
    ```
    [udp://5555]
    index = security
    sourcetyoe = linux
    source = UF_ubuntu
    connection_host = ip
    queueSize = 10MB
    persistentQueueSize = 1GB
    disabled = 0
    ```
 5. Save and restart Splunk
 6. **Done**
