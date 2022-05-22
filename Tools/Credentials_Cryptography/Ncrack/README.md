Ncrack is a brute forcing tool, developed by the Nmap team.  Protocols supported are: SSH, RDP, FTP, Telnet, HTTP(S), Wordpress, POP3(S), IMAP, CVS, SMB, VNC, SIP, Redis, PostgreSQL, MQTT, MySQL, MSSQL, MongoDB, Cassandra, WinRM, OWA, DICOM.

**_Note:_** Ncrack may produce false positives. Further, it may not successfully enumerate all accounts (on FTP at least).

##### Crack
```bash
ncrack -U <Username List> -P <Password List> <Service Name>://<Target Host>:<Port Number>
```

##### Multiple Hosts and Services
```bash
ncrack -U <Username List> -P <Password List> <Target Host>,<Host 2> -p <Service Name>:<Port Number>,<Service Name>:<Port Number>
```

# [Manual](https://nmap.org/ncrack/man.html)