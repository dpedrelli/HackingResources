# Enumerate
##### With nmap
```bash
nmap --script nfs-showmount, nfs-ls, nfs-statfs <IP Address>
```

##### With showmount
```bash
showmount -e <IP Address>
```

# Mount
```bash
mkdir -p /mnt/<Share Name>
mount -t nfs <NFS IP Address>:/<Share Name> /mnt/<Share Name> -o nolock
```

# Check Mounted Shares
```bash
mount
```