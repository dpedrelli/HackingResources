# Enumerate
##### [Determine versions of NetBIOS ports with nmap](../../Tools/ActiveRecon/Nmap/README.md#Determine-versions-of-NetBIOS-ports)
##### [Enumerate with nmap](../../Tools/ActiveRecon/Nmap/README.md#Enumerate-SMB-Shares)

##### [Enumerate Shares with smbclient](../../Tools/NetBIOS_SMB_Samba/smbclient/README.md#Enumerate-Shares)

##### [Enumerate Shares with smbmap](../../Tools/NetBIOS_SMB_Samba/smbmap/README.md#Enumerate-Shares)

##### [Enumerate Users With rpcclient](../../Tools/NetBIOS_SMB_Samba/rpcclient/README.md#Enumerate-Users)

##### [Enumerate with enum4linux](../../Tools/NetBIOS_SMB_Samba/enum4linux/README.md)

# Interact / Mount

##### With smbclient
```bash
smbclient \\\\<IP Address>\\<Share Name>
```

##### [Mount with cifs](../../Tools/NetBIOS_SMB_Samba/cifs/README.md#Mount-SMB-Share)

# Linux with Windows Active Directory Trust
##### Pass-The-Hash
```bash
# Assuming root access on Linux
tdbdump /var/lib/samba/private/secrets.tdb

# Assuming target hash trust with Active Directory, decode UTF-8 encoded "data" to get NTLM hashes

# Use pth-smbclient, from pth-toolkit, to pass-the-hash.
```

# References
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