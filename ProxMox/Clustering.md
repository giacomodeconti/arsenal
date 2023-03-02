# Add new clusters in ProxMox
### Configuration
1. Set up the IP of cluster and hostname

    `/etc/network/interfaces` - 
    `/etc/hostname` -
    `/etc/host`
    
3. Reboot
4. Add in `/etc/hosts` file the IP of all cluster
  - Example this is node 1 console:
    ```
    127.0.0.1 localhost.localdomain localhost
    192.168.1.220 node1.local node1
    192.168.1.230 node2.local node2    # Here we added node2

    # The following lines are desirable for IPv6 capab>

    ::1     ip6-localhost ip6-loopback
    fe00::0 ip6-localnet
    ff00::0 ip6-mcastprefix
    ff02::1 ip6-allnodes
    ff02::2 ip6-allrouters
    ff02::3 ip6-allhosts
    ```
    For example in node2 you'll need to add node1
5. In node1 open CLI and type `pvecm create myclustername` change myclustername with the name you have choose for your cluster
6. In node2 open CLI and type `pvecm add [node1 IP]` here you add the ip of node1 in node2 so the node2 it will be visible on node1
7. Done
