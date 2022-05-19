# Full Scope
Attempt to collect all domain names, host names, DNS server, mail servers, and IP addresses associated with the organization.
* ### DNS
  * ##### [Query Domain Registration with WHOIS or RDAP](DomainRegistration.md)
    1) Perform a lookup with [WHOIS](../../Tools/Domain/whois/README.md#Query), [Nmap](../../Tools/NetworkDiscovery/Nmap/README.md#Query-WHOIS), or an [online tool](../../Tools/OnlineResources/README.md#WHOIS-and-RDAP).
    2) Perform another query, specifying the registrar's [WHOIS](../../Tools/Domain/whois/README.md#Specify-Server-to-Query) server.
    3) A key take away from this phase is to identify the organization's name (DNS) servers.
  * ##### [DNS Enumeration](DnsEnumeration.md)
* ### IP Addresses (Who Owns The IPs and What Domains Do They Host?)
  * ##### Reverse DNS
    1) Retrieve one or more IP addresses from client or [nslookup](../../Tools/Domain/nslookup/README.md#Get-IP-Address-of-Host-Name)
    2) Perform [Reverse DNS](../../Tools/OnlineResources/README.md#Network-Tools) lookup on the IP addresses.
  * ##### Who Owns The IP Address / Netblock
    1) Perform a WHOIS lookup on the address.
    2) Tools like [hostmap](../../Tools/Domain/hostmap/README.md), [Maltego](../../Tools/OSINT/Maltego/README.md), [FOCA](../../Tools/OSINT/FOCA/README.md), [fierce](../../Tools/Domain/fierce/README.md), and Dimitry can automate this task.

# Live Hosts
Now, the attacker must determine the devices and the roles played by each IP address obtained.  The first step is to determine which IP addresses are live.

1) Perform a ping sweep with [fping](../../Tools/NetworkDiscovery/fping/README.md#Host-Discovery), [hping](../../Tools/NetworkDiscovery/hping/README.md#Host-Discovery), or [nmap](../../Tools/NetworkDiscovery/Nmap/README.md#Host-Discovery), to determine which hosts are live.