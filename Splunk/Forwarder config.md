### Install

1. Need minimum 20gb to run it
2. Download .deb Splunk Forwarder from splunk site with wget
3. `sudo dpkg -i filename`
4. Go to `cd /otp` and execute`./splunk/bin/splunk start --accpet-license`
5. Go to Indexer and open port 9997 for Forwarders or any other port

### Configuration

1. Stop splunk Forwarder
`./splunk/bin/splunk stop`
2. Run Forwarder on boot by user
`sudo ./splunk enable boot-start -user [user]`
3. Add Indexer server
`sudo ./splunk add forward-server 192.168.1.100:9997`
5. Add log files from Forwarder to Indexer
`sudo ./splunk add monitor /var/log/[log] -index [index]`
 you can add many logs you want
6. Add this inputs.config file for Indexer
 - `sudo nano /opt/splunkforwarder/etc/system/local/inputs.conf`
 - 
   ```
   [monitor:///var/log/syslog]
   host = UF1
   disabled = 0
   index = security
   sourcetype = syslog
   host_segment = 3
   ```
 - Change monitor with file you want to send, host , index, sourcetype
