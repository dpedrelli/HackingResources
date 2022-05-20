# Sniffing
* ### Passive
  * ##### [with dsniff](../../Tools/NetworkDiscovery/dsniff/README.md)
  * ##### [with tcpdump](../../Tools/NetworkDiscovery/tcpdump/README.md)
  * ##### [With Wireshark](../../Tools/NetworkDiscovery/Wireshark/README.md)
* ### Active
  * ##### MAC Flooding
    This technique fills a switch's CAM (content addressable memory) table of MAC addresses, causing the switch to fail open and operate as a hub.
    * [Flood MAC with Macof (part of dsniff suite)](../../Tools/NetworkDiscovery/dsniff/README.md)
    
# Man-in-the-Middle
  * ##### ARP Poisoning
    In ARP Poisoning, the attacker sends a gratuitous ARP Response to host A, with host B's IP address and the MAC address of the attacker.  Host B can be a computer on the LAN or a gateway.  At this point, the attacker can intercept all traffic flowing from A to B, but not from B to A.  If the attacker duplicates this process with host B, the attacker can intercept all traffic between A and B.  It is important that the attacker forward intercepted packets.  This requires enabling IP forwarding, on Linux.
    * ##### [Enable IP forwarding to make attack machine operate as a proxy, between the victims](../../Tools/Shells/Linux/README.md#Enable-IP-Forwarding)
    * ##### [Establish with arpspoof](../../Tools/MitM/arpspoof/README.md#Establish-MitM)
    * ##### [Sniff with Wireshark](../../Tools/NetworkDiscovery/Wireshark/README.md#Sniff-ARP-Spoof-MitM)
    * ##### [Sniff with dsniff](../../Tools/NetworkDiscovery/dsniff/README.md#Sniff-ARP-Spoof-MitM)
    * ##### [Establish and Sniff with Ettercap](../../Tools/MitM/Ettercap/README.md#Establish-MitM)
    * ##### [Establish and Sniff with Bettercap](../../Tools/MitM/Bettercap/README.md#Establish-MitM)
  * ##### Intercept SSL
    * ##### [Intercept SSL](../../Tools/MitM/Ettercap/README.md#Intercept-SSL) and [Establish MitM](../../Tools/MitM/Ettercap/README.md#Establish-MitM) with Ettercap
    * ##### [Strip SSL with SSLstrip](../../Tools/MitM/SSLstrip/README.md#Strip-SSL) and [Establish MitM with Ettercap](../../Tools/MitM/Ettercap/README.md#Establish-MitM)
    * ##### [Strip SSL and Establish MitM with Bettercap](../../Tools/MitM/Bettercap/README.md#Establish-MitM-and-Strip-SSL)
    * ##### [Strip SSL and Establish MitM with MITMf](../../Tools/MitM/MITMf/README.md#Establish-MitM-with-HSTS-Bypass)
  * ##### DHCP Spoofing
  * ##### DNS Poisoning
  * ##### LLMNR and NBT-NS Spoofing
    * ##### [With Responder](https://github.com/lgandx/Responder)
  


# References
[ARP Poisoning: What it is & How to Prevent ARP Spoofing Attacks](https://www.varonis.com/blog/arp-poisoning)