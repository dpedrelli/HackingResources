# Search Engine
##### [Bing](https://www.bing.com)
##### [Freespoke](https://freespoke.com/)
##### [Google](https://www.google.com/)
##### [Shodan.io](https://www.shodan.io/)
###### [Yandex](https://yandex.com/)

# Social Networks
##### [Facebook](https://www.facebook.com)
##### [LinkedIn](https://www.linkedin.com)
##### [theHarvester](https://pypi.org/project/theHarvester/)
theHarvester is used to gather open source intelligence (OSINT) on a company or domain.
It supports Google Dorks and Shodan.
```bash
# Search the target domain, with Gooogle.
theHarvester -d targetdomain.com -b google
```

# Whois
```bash
whois targetdomain.com > whois.txt
```

# Website Footprinting
##### [HTTrack](https://www.httrack.com/)
##### [Archive.org](https://archive.org/)

# Web Technology Footprinting
##### [WhatWeb](https://github.com/urbanadventurer/WhatWeb)
##### [BuiltWith](https://builtwith.com/)

# Domain Recon
##### [Sublist3r](https://github.com/aboul3la/Sublist3r)
Enumerate subdomains.
##### dig
##### dnsenum
##### dnsmap
```bash
# Bruteforce DNS
dnsmap domain.com -w /usr/share/wordlists/SecLists/Discovery/DNS/dns-Jhaddix.txt
```
##### fierce
```bash
# Bruteforce DNS
fierce -dns domain.com -wordlist /usr/share/wordlists/SecLists/Discovery/DNS/fierce-hostlist.txt
```
##### host
```bash
host domain.com
```
##### [Nmap](../IPandPortScanners/Nmap/README.md)
```bash
# Bruteforce DNS
nmap -p 53 dns-brute domain.com
```
##### [ZoneTransfer.me](https://digi.ninja/projects/zonetransferme.php)

# Cloud Recon

# Metadata
##### [Metagoofil](https://github.com/laramies/metagoofil)



##### [Recon-ng](https://github.com/lanmaster53/recon-ng)
##### [Maltego](https://www.maltego.com/)
##### [Netcraft](https://www.netcraft.com/)
##### [OSRFramework](https://github.com/i3visio/osrframework)