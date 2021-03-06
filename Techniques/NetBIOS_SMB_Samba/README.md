# Enumerate
### Nmap
##### [Discover OS](../../Tools/NetworkDiscovery/Nmap/README.md#SMB-OS-Discovery)
##### [List supported protocols and dialects](../../Tools/NetworkDiscovery/Nmap/README.md#SMB-Protocols)
##### [Get SMB security level](../../Tools/NetworkDiscovery/Nmap/README.md#SMB-Security-Mode)
##### [Enumerate Shares](../../Tools/NetworkDiscovery/Nmap/README.md#Enumerate-SMB-Shares)
##### [Enumerate Users](../../Tools/NetworkDiscovery/Nmap/README.md#Enumerate-SMB-Users)

##### [Determine versions of NetBIOS ports with nmap](../../Tools/NetworkDiscovery/Nmap/README.md#Determine-versions-of-NetBIOS-ports)

### smbclient
##### [Enumerate Shares](../../Tools/NetBIOS_SMB_Samba/smbclient/README.md#Enumerate-Shares)

### smbmap
##### [Enumerate Shares](../../Tools/NetBIOS_SMB_Samba/smbmap/README.md#Enumerate-Shares)

### rpcclient
##### [Enumerate Users in Bash Script](../../Tools/NetBIOS_SMB_Samba/rpcclient/README.md#Enumerate-Users-with-Bash-Script)

##### [Enumerate Domains](../../Tools/NetBIOS_SMB_Samba/rpcclient/README.md#Enumerate-Domains)

##### [Enumerate Users](../../Tools/NetBIOS_SMB_Samba/rpcclient/README.md#Enumerate-Users)

##### [Enumerate Groups](../../Tools/NetBIOS_SMB_Samba/rpcclient/README.md#Enumerate-Groups)

### enum4linux
##### [Enumerate](../../Tools/NetBIOS_SMB_Samba/enum4linux/README.md)

# Connect

##### [Connect with smbclient](../../Tools/NetBIOS_SMB_Samba/smbclient/README.md#Connect-To-Share)

##### [Connect with rpcclient](../../Tools/NetBIOS_SMB_Samba/rpcclient/README.md#Connect-To-Host)

##### [Mount with cifs](../../Tools/NetBIOS_SMB_Samba/cifs/README.md#Mount-SMB-Share)

# Query

##### [Query User with rpcclient](../../Tools/NetBIOS_SMB_Samba/rpcclient/README.md#Query-User)

# Linux with Windows Active Directory Trust
##### Pass-The-Hash
```bash
# Assuming root access on Linux
tdbdump /var/lib/samba/private/secrets.tdb

# Assuming target hash trust with Active Directory, decode UTF-8 encoded "data" to get NTLM hashes

# Use pth-smbclient, from pth-toolkit, to pass-the-hash.
```

# SMB Relay
1) ##### [SMB Relay with Metasploit](../../Tools/Metasploit/README.md#SMB-Relay)
2) ##### [Spoof DNS with dnsspoof](../../Tools/Domain/dnsspoof/README.md#Spoof-DNS-Server)
3) ##### [Enable IP Forwarding](../../Tools/Shells/Linux/README.md#Enable-IP-Forwarding)
4) ##### [Spoof ARP of DNS Server and SMB Client with arpspoof](../../Tools/NetworkDiscovery/arpspoof/README.md#Spoof-ARP)

# Attacks
##### [Attempt NULL Session with Net](../../Tools/NetBIOS_SMB_Samba/Net/README.md#NULL-Session)
##### [Brute Force User Accounts with Hydra](../../Tools/Credentials_Cryptography/Hydra/README.md#SMB)
##### [Establish Reverse Shell with Metasploit](../../Tools/Metasploit/README.md#Establish-Reverse-Shell-with-SMB)

# References
[SMB and Samba Security Audit Tools](https://miloserdov.org/?p=4066)

[pth-toolkit](https://github.com/byt3bl33d3r/pth-toolkit)

[passing-the-hash](https://code.google.com/archive/p/passing-the-hash/)

[Samba](https://en.wikipedia.org/wiki/Samba_(software))

[Server Message Block (SMB) / CIFS](https://en.wikipedia.org/wiki/Server_Message_Block)

[statistically-likely-usernames](https://github.com/insidetrust/statistically-likely-usernames)

[enum4linux](https://github.com/CiscoCXSecurity/enum4linux)

[smbmap](https://github.com/ShawnDEvans/smbmap)

[smb-os-discovery](https://nmap.org/nsedoc/scripts/smb-os-discovery.html)

# CVEs
[CVE-2017-7494](https://cve.circl.lu/cve/CVE-2017-7494)

[username map script](https://www.rapid7.com/db/modules/exploit/multi/samba/usermap_script/)
[CVE-2007-2447: Remote Command Injection Vulnerability](https://www.samba.org/samba/security/CVE-2007-2447.html)

[Symlink Directory Traversal](https://www.samba.org/samba/news/symlink_attack.html)
[Symlink Directory Traversal](https://www.rapid7.com/db/modules/auxiliary/admin/smb/samba_symlink_traversal/)