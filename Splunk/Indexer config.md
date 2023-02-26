### Install

1. Need minimum 20gb to run it
2. Download .deb splunk enterprise from splunk site with wget
3. `sudo dpkg -i filename`
4. Go to `cd /otp` and execute`./splunk/bin/splunk start`
5. Login in Splunk and enable TLS/HTTPS

### Configuration

1. Exec splunk on boot
`[sudo] ./[SPLUNK_HOME]/bin/splunk enable boot-start -user [user]`
2. Set on never THP (Transparent Huge Pages)
	- 	Open file
	`nano /etc/systemd/system/disable-thp.service`
	-	Paste this config file:
		```
		[Unit]
		Description=Disable Transparent Huge Pages (THP)
		DefaultDependencies=no
		After=sysinit.target local-fs.target

		[Service]
		Type=oneshot
		ExecStart=/bin/sh -c 'echo never | tee /sys/kernel/mm/transparent_hugepage/enabled > /dev/null'
		ExecStart=/bin/sh -c 'echo never | tee /sys/kernel/mm/transparent_hugepage/defrag > /dev/null'

		[Install]
		WantedBy=basic.target
	-	Reload the services configuration.
	`systemctl daemon-reload`
	-	Start the created service.
	`systemctl start disable-thp`
	
	-	Verify if the Transparent Huge Pages were disabled.
	`cat /sys/kernel/mm/transparent_hugepage/enabled`
	-	Here is the command output.
	`always madvise [never]`
	
	-	Enable the created service during boot.
	`systemctl enable disable-thp`
	-	Reboot
	
### Backup
- Remeber to backup this directory but before you must stop Splunk
`/opt/splunk/var/lib/splunk/`

### Remove Indexes
- This will remove an entire index
`./splunk clean eventdata -index main -f`
