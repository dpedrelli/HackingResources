# Port Scan
* ##### IP Fragmentation

  Splits datagrams into chunks.  If an IDS does not reassemble all of the chunks into the whole packet, the fragmented scan may not be identified.

* ##### Decoys / Spoof Source Addresses

  Decoys involve performing port scans that spoof other machines' addresses as the source address.  This is useful to fill IDS logs with useless data.  It is important to include the Attack machine's address, among the spoofed addresses, or the Attacker will not receive the results of the port scan.  Embedding the Attacker's address in the middle of the spoofed addresses, may help to prevent the Target from identifying the Attacker's true address.  **This scan will not work with a TCP scan or any scan that requires a full, three-way handshake.**

* ##### Spoof Source Port
  
  DNS traffic may be allowed on the network and not filtered.  Setting source port to 53 may evade detection.

* ##### Append Random Data to Packet Header
  
  

* ##### Spoof MAC address
  
  This helps in situations in which the firewall either filters the Attacker's MAC addresses or only allows packets from specific MAC addresses.

* ##### Randomize Hosts 
  
  Rather than scan IP addresses in sequence, scan hosts in random order.  Use both live hosts and non-live hosts.

* ##### Timing
  
  Running a slower than normal scan may evade detection.
  
  ### [With hping](../../Tools/NetworkDiscovery/hping/README.md#Evasion)

  ### [With Nmap](../../Tools/NetworkDiscovery/Nmap/README.md#Evasion)