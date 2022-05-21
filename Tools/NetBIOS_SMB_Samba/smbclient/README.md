# smbclient

smbclient is a Python library and part of SecureAuth Corporation's [impacket](https://github.com/SecureAuthCorp/impacket) suite of network protocal libraries.

# Enumerate Shares
```bash
smbclient -L <IP Address>
```

# Connect To Share
##### Anonymous / Null
```bash
smbclient //<IP Address>/<Sharename>

smbclient \\\\<IP Address>\\<Sharename>
```
##### Specify Username
```bash
smbclient -U <Username> //<IP Address>/<Sharename>

smbclient -U <Username> \\\\<IP Address>\\<Sharename>
```

# Download File
```bash
get <Filename>
```
