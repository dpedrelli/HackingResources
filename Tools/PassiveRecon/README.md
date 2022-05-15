# Search Engine / Web Presence
##### [Bing](https://www.bing.com)
##### [Board Reader](https://boardreader.com/)
##### [Freespoke](https://freespoke.com/)
##### [Google](https://www.google.com/)
##### [Internet Archive](https://archive.org/search.php)
##### [Shodan.io](https://www.shodan.io/)
##### [Yandex](https://yandex.com/)

##### Display Sites with Links to a Specific Site
```bash
link:www.website.com
```

##### Search a Specific Site
```bash
site:www.website.com
```

##### Search for Documents of a Specific Type
```bash
filetype:pdf
```

# Government
##### [DUNS & CAGE Codes](https://sam.gov/content/home)
##### [SEC](https://www.sec.gov/edgar.shtml)

# Job Related
##### [Indeed](https://www.indeed.com/)
##### [LinkedIn](https://www.linkedin.com)
##### [Monster](https://www.monster.com/)
##### [CareerBuilder](https://www.careerbuilder.com/)
##### [Glassdoor](https://www.glassdoor.com/index.htm)
##### [Simply Hired](https://www.simplyhired.com/)
##### [Dice](https://www.dice.com/)
##### [Zip Recruiter](https://www.ziprecruiter.com/)

# Financial
##### [CrunchBase](https://www.crunchbase.com/)
##### [Inc](https://www.inc.com/)

# Metadata
##### [FOCA](https://www.elevenpaths.com/innovation-labs/technologies/foca)

# Cache & Archives
##### [Internet Archive](https://archive.org/)

##### Google Dork to Display Cache
```bash
cache:www.website.com
```

# Social Networks
##### [Facebook](https://www.facebook.com)
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
##### [Nmap](../ActiveRecon/Nmap/README.md)
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

# Mind Mapping
[FreeMind](http://freemind.sourceforge.net/wiki/index.php/Main_Page)

[Xmind](https://www.xmind.net/)

# Miscellaneous
[Dradis](https://dradisframework.com/ce/)

[Faraday](https://github.com/infobyte/faraday)

[Magictree](https://www.gremwell.com/what_is_magictree)