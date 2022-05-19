# Ports, Protocols, and Services

* Following the Information Gathering phase, scanning seeks to gain more detailed information about the devices on the network.  This will help determine the neworks composition and how to, effectively, mount an attack.
* It is important to run scans, with multiple techniques, to circumvent protective measures that network administrators may have in place.
* It is best to perform scans in individual jobs of small numbers of ports, to prevent detection.

* # Host Discovery
  * ### [With fping](../../Tools/NetworkDiscovery/fping/README.md#Host-Discovery)
  * ### [With hping](../../Tools/NetworkDiscovery/hping/README.md#Host-Discovery)
  * ### [With Nmap](../../Tools/NetworkDiscovery/Nmap/README.md#Host-Discovery)
* # Grab Banners
* # Scan Ports
  * ### [With Angry IP Scanner](../../Tools/NetworkDiscovery/AngryIPScanner/README.md)
  * ### [With hping](../../Tools/NetworkDiscovery/hping/README.md#Port-Scan)
  * ### [With Masscan](../../Tools/NetworkDiscovery/Masscan/README.md)
  * ### [With Nmap](../../Tools/NetworkDiscovery/Nmap/README.md#Port-Scan)
  * ### [With RustScan](../../Tools/NetworkDiscovery/RustScan/README.md#Scan)
  * ### Zombie Scan using both hping and Nmap
```bash
# Hping tracks IP ID increment.
sudo hping3 -S -r <Zombie Host> -p 135

# Nmap performs scan.
sudo nmap -S <Zombie Host> <Target Host> -p <Port #> -Pn -n -e <Interface Name> --disable-arp-ping

1) Start hping tracking IP ID.
2) Run scan with nmap.
3) Check hping for incrementing IP ID, to confirm that port is open.
```  
* # OS Fingerprinting
  * ### [Actively with Nmap](../../Tools/NetworkDiscovery/Nmap/README.md#Fingerprint-OS)
    ### [Passively with p0f](../../Tools/NetworkDiscovery/p0f/README.md)

# References
[IANA](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)

[Nmap - Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html)