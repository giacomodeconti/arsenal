### how to configure network settings in Linux ( Ubuntu )  

- DHCP

network:
  ethernets:
    enp0s3:
      dhcp4: true
  version: 2

================================================================================= 
#sudo vi /etc/netplan/00-installer-config.yaml



================================================================================= 
================================================================================= 
network: 
    version: 2 
    renderer: networkd 
    ethernets: 
        ens33: 
            addresses: 
                - 10.10.10.131/24 
            nameservers: 
                addresses: [8.8.4.4, 8.8.8.8] 
            routes: 
                - to: default 
                  via: 10.10.10.2
 
================================================================================= 
================================================================================= 
Please replace the above IP with your IP address and then issue the command below: 

#sudo netplan apply


check also, vi /etc/resolv.conf 
