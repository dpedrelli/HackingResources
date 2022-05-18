# Information Gathering
  * ### [Passive](../Tools/PassiveRecon/README.md)
    * ##### Query Domain Registration with WHOIS or RDAP
      * Perform [WHOIS](../Tools/PassiveRecon/Domain/whois/README.md#Query) lookup.
      * Perform another query, specifying the registrar's [WHOIS](../Tools/PassiveRecon/Domain/whois/README.md#Specify-Server-to-Query) server.
    * ##### DNS Enumeration
      * ##### Query name servers with [WHOIS](../Tools/PassiveRecon/Domain/whois/README.md#Query) or [dig](../Tools/PassiveRecon/Domain/dig/README.md#Query-Record-Type) or [nslookup](../Tools/PassiveRecon/Domain/nslookup/README.md#Query-Name-Servers).
      * ##### Query mail servers with [dig](../Tools/PassiveRecon/Domain/dig/README.md#Query-Record-Type) or  [nslookup](../Tools/PassiveRecon/Domain/nslookup/README.md#Query-Mail-Servers).
      * ##### Get server IP Addresses with [nslookup](../Tools/PassiveRecon/Domain/nslookup/README.md#Get-IP-Address-of-Server).
      * ##### Attemp zone transfer with [dig](../Tools/PassiveRecon/Domain/dig/README.md#Host-Transfer) or [host](../Tools/PassiveRecon/Domain/host/README.md#Host-Transfer).
      * ##### Attemp reverse lookup to get domains with [dig](../Tools/PassiveRecon/Domain/dig/README.md#Reverse-Lookup-to-Get-Domains).
      * ##### DNS Scan, Zone Transfer, Brute Force, and Reverse Lookup with [fierce](../Tools/PassiveRecon/Domain/fierce/README.md).
      * ##### DNS Scan, Zone Transfer, Brute Force with [dnsenum](../Tools/PassiveRecon/Domain/dnsenum/README.md).
      * ##### Brute Force with [dnsmap](../Tools/PassiveRecon/Domain/dnsmap/README.md).
      * ##### All-in-One with [dnsrecon](../Tools/PassiveRecon/Domain/dnsrecon/README.md).
  * ### [Active](../Tools/ActiveRecon/README.md)
    * ##### [Host Discovery](../Tools/ActiveRecon/README.md#Host-Discovery)
    * ##### [Scan Ports](../Tools/ActiveRecon/README.md#Scan-Ports)

| Infrastructure    | Business                |
|-------------------|-------------------------|
| Network Maps      | Web Presence (domains)  |
| Network Blocks    | Physical Locations      |
| IP Addresses      | Employees / Departments |
| Ports             | E-Mail Addresses        |
| Services          | Partners & 3rd Parties  |
| DNS               | Press / News Releases   |
| Operating Systems | Documents               |
| Alive Machines    | Financial Information   |
| Systems           | Job Postings            |

##### Web Presence
* Business
* Location
* Projects
* External Links
* Subdomains

# Exploitation

# Post Exploitation
  * ### Enumeration
    * ##### Local Box
      * ##### [Linux](Enumeration/Linux/README.md)
      * ##### [Windows](Enumeration/Windows/README.md)
    * ##### [Network](../Tools/ActiveRecon/README.md)
  * ### Privilege Escalation
      * ##### [Linux](PrivEsc/Linux/README.md)
      * ##### [Windows](PrivEsc/Windows/README.md)
  * ### [Lateral Movement](LateralMovement/README.md)
  * ### [Data Exfiltration](DataExfiltration/README.md)
  * ### [Persistence](Persistence/README.md)
  * ### [Third-Party Guides](PostExploitation/ThirdParty.md)
