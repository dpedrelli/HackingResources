# Enumerate
##### With nmap scripts
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

# View Configured Exports
```bash
/etc/exports
```

# References
[Network File System (NFS)](https://en.wikipedia.org/wiki/Network_File_System)

[Sun RPC](https://en.wikipedia.org/wiki/Sun_RPC)

