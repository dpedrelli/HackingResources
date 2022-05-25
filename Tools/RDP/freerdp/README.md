# Freerdp

Freerdp [supports newer protocols than rdesktop](https://www.syskit.com/blog/credssp-required-by-server-solutions/).

```bash
xfreerdp /dynamic-resolution +clipboard /cert:ignore /v:<IP Address> /u:<User Name> /p:<Password>
# Do not use /workspace
```

# Pass The Hash
```bash
xfreerdp /v:<IP Address> /u:<User Name> /d:<Domain> /pth:<NTLM Hash>
```