##### Information to Gather
* What does the organization do?
* What is the organization's business purpose?
* Identify the organization's physical locations.
* Identify Web sites, domain names, sub-domains, and alternate Web sites.
* Identify projects on which the organizatin may be working.
* Identify departments within the organization.
* Identify external sites, such as social media or other sites referencing the organization.
* Try to identify E-Mail addresses and contact information of people who work for the organization.
* Find press releases and news articles.
* Find various comments about the company, both from employees and outsiders.  Web sites that post employer reviews may be useful.
* Look for strategic partners, third-parties, mergers, acquisitions, etc.
* Look for job postings and employer reviews.
* Look for financial information.
* Look for documents, files, and metadata on the organization.

##### Methodology
* Start with [OSINT tools](../../Tools/OSINT/README.md) that can make OSINT gathering easier or even automate the process.
* Perform an [Internet search](/README.md#Internet-Search-Engines) of the organization's name.
* Perform advanced searches with [Google Dorks](/README.md#Google-Dorks).
* Search [job related sites](/README.md#Job-Related-Web-Sites), like LinkedIn and GlassDoor, information about the organization, job postings, and employer reviews.
* Business that work with the US government may appear in [government listings](/README.md#Government).
* Search [financial related sites](/README.md#Financial-Related-Web-Sites), for organizational, financial, and stakeholder information.
* Search [social media sites](/README.md#Social-Networks) and [people search sites](/README.md#People-Searches) for information about the organization and employees.  This may provide useful contact information or even information beneficial for social engineering.
* Use tools like [FOCA](../../Tools/OSINT/FOCA/README.md) and [Google Dorks](/README.md#Google-Dorks) to find and harvest files and metadata.
* Search [cache](/README.md#Display-Cache) and [archive sites](/README.md#Archival-Sites).
* Search for Git repositories with [GitTools](https://github.com/internetwache/GitTools).

1) Physical / Social
   1) Location Information
        1) Satellite Images
        2) Drone Recon
        3) Building Layout
           1) Badge Readers
           2) Break Areas
           3) Security
           4) Fencing
    2) Job Information
        1) Employees
           1) Name
           2) Title
           3) Phone #
           4) Manager
           5) LinkedIn -> Company -> People
        2) Pictures
           1) Badge Photos
           2) Desk Photos
           3) Computer Photos (installed software)
           4) LinkedIn -> Company -> Images
2) Web / Host
   1) Target Validation
        1) whois
        2) nslookup
        3) dnsrecon
   2) Find Subdomains
        1) Google
        2) dig
        3) nmap
        4) [sublist3r](https://github.com/aboul3la/Sublist3r)
        5) [Bluto](https://github.com/darryllane/Bluto)
        6) [crt.sh](https://crt.sh/)
        7) [OWASP Amass](https://github.com/OWASP/Amass)
        8) [Httprobe](https://github.com/tomnomnom/httprobe)
   3) Fingerprinting
        1) nmap
        2) Wappalyzer
        3) [WhatWeb](https://github.com/urbanadventurer/WhatWeb)
        4) [BuiltWith](https://builtwith.com/)
        5) netcat
   4) Data Breaches
        1) [HaveIBeenPwned](https://haveibeenpwned.com/)
        2) [Breach-Parse](https://github.com/hmaverickadams/breach-parse)
        3) [WeLeakInfo](https://weleakinfo.to/)
3) Discover E-Mail Addresses
   1) [hunter.io](https://hunter.io/)
   2) [Phonebook.cz](https://phonebook.cz/)
   3) [VoilaNorbert.com](https://www.voilanorbert.com/)
   4) Clearbit Connect (Chrome Plugin)
   5) [E-Mail Hippo](https://tools.emailhippo.com/)
   6) [Email-Checker.net](https://email-checker.net/)
   7) [HaveIBeenPwned](https://haveibeenpwned.com/)
   8) Google E-Mail -> Forgot Password -> Try Another Way
4) Breached Credentials
   1) [Breach-Parse](https://github.com/hmaverickadams/breach-parse)
   2) [DeHashed](https://dehashed.com/)
   3) [hashes.org](http://hashes.org) **Down**
5) Google
   1) [Overview of Google search operators](https://developers.google.com/search/docs/advanced/debug/search-operators/overview)
   2) [Google Search Operators](https://ahrefs.com/blog/google-advanced-search-operators/)
   3) Find files:  **site:domain.com filetype:docx**