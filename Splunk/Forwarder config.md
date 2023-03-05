# Universal Forwarder configuration for Linux and Windows
 - If you want you can create an index for every OS
# Linux
### Install

1. Need minimum 20gb to run it
2. Download .deb Splunk Forwarder from splunk site with wget
3. `sudo dpkg -i filename`
4. Go to `cd /otp` and execute`./splunk/bin/splunk start --accpet-license`
5. **If you don't have debian just unpack splunk in /opt**
6. Go to Indexer and open port 9997 for Forwarders or any other port

## Configuration 
### Via app ( *Raccomanded* )
1. Stop splunk Forwarder
`./splunk/bin/splunk stop`
2. Download Unix app from [here](https://splunkbase.splunk.com/app/833 "Unix app")
3. Extract the file in `/opt/splunkforwarder/etc/apps`
4. Open the Unix App folder and go to **default** and inputs.conf
5. Enable the monitor log you want to monitor by replacing the 1 with 0 in disabled option, if you enable it remeber to add index option. 
 - **inputs.conf** example:
    ```
    [monitor:///var/log]   # Stanza 
    whitelist=(\.log|log$|messages|secure|auth|mesg$|cron$|acpid$|\.out)
    blacklist=(lastlog|anaconda\.syslog)
    disabled = 0    # Enable with 0
    index=linux   # Add index
    ```
 - Remeber for **security** add queue configuration in inputs.conf to avoid diconnections and data loss:
   ```
   queueSize = <integer>[KB|MB|GB]
   * The maximum size of the in-memory input queue.
   * Default: 500KB

   persistentQueueSize = <integer>[KB|MB|GB|TB]
   * The maximum size of the persistent queue file.
   * Persistent queues can help prevent loss of transient data. For information on
     persistent queues and how the 'queueSize' and 'persistentQueueSize' settings
     interact, search the online documentation for "persistent queues".
   * If you set this to a value other than 0, then 'persistentQueueSize' must
     be larger than either the in-memory queue size (as defined by the 'queueSize'
     setting in inputs.conf or 'maxSize' settings in [queue] stanzas in
     server.conf).
   * Default: 0 (no persistent queue)
   ```
6. Add also **outputs.conf** in default directory with this config
 - **outputs.conf** example:
   ```
   [tcpout]
   defaultGroup = default-autolb-group

   [tcpout:default-autolb-group]
   server = 192.168.1.100:9997

   [tcpout-server://192.168.1.100:9997]
   ```
   - Change this IP with your index IP
7. Run Forwarder on boot by user
`sudo ./splunk enable boot-start -user [user]`
8. **Done**
### Via command

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


