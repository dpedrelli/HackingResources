# Enumerate
##### With nmap (shares)
```bash
# Determine versions of NetBIOS ports.
nmap -sT -sU -sV <IP Address> -p135,137,138,139,445 --open

# Enumerate available shares.
nmap --script smb-enum-shares <IP Address>
```

##### With smbclient (shares)
```bash
smbclient -L <IP Address>
```

##### With smbmap (shares)
```bash
smbmap -H <IP Address>
```

##### With rpcclient (users)
```bash
# Bash for loop
for u in $(cat users.txt);
	do rpcclient -U "" <IP Address> -N \
	--command="lookupnames $u";
done | grep "User: 1"
```

##### With enum4linux
```bash
enum4linux <IP Address>
```

# Interact / Mount

##### With smbclient
```bash
smbclient \\\\<IP Address>\\<Share Name>
```

##### With cifs
```bash
mkdir -p /mnt/<Share Name>
mount -t cifs \\\\<IP Address>\\<Share Name> /mnt/<Share Name>
```

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