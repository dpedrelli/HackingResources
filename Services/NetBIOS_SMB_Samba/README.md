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