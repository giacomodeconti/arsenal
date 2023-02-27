# Universal Forwarder configuration for Linux and Windows
 - If you want you can create an index for every OS
## Linux
### Install

1. Need minimum 20gb to run it
2. Download .deb Splunk Forwarder from splunk site with wget
3. `sudo dpkg -i filename`
4. Go to `cd /otp` and execute`./splunk/bin/splunk start --accpet-license`
5. **If you don't have debian just unpack splunk in /opt**
6. Go to Indexer and open port 9997 for Forwarders or any other port

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
 
 7. **Done**
 
# Windows

### Install

1. Download .msi Universal Forwarder from splunk.com
2. Open installer and configure it with user:passwd , forwarder IP
3. After install check splunk service if is running

### Configuration

1. Open SplunkForwarder directory and go to apps
`C:\Progam Files\UniversalSplunkForwarder\etc\apps`
2. Download Windows app from [splunkbase.splunk.com](https://splunkbase.splunk.com/app/742 "Windows App")
3. Extract the app in app folder
4. Open the Windows App folder and go to default and inputs.conf
5. Enable the monitor log you want to monitor by replacing the 1 with 0 in disabled option, if you enable it remeber to add index option. 
 - For example:
    ```
    [WinEventLog://Application]
    disabled = 0    # Enable with 0
    start_from = oldest
    current_only = 0
    checkpointInterval = 5
    renderXml=true
    index=windows   # Add index

    ```
6.  Restart splunk service
7.  **Done**


