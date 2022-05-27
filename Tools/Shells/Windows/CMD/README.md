# [Check Access Control on File or Directory](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/icacls)
|    | Basic Permissions |
|----|-------------------|
| F  | Full access
| M  | Modify access
| RX | Read and execute access
| R  | Read-only access
| W  | Write-only access

```bash
icacls "<File or Directory Name>"
```

# System Information
##### OS Configuration Information
```bash
systeminfo
```
##### Get Windows Version
```bash
systeminfo | findstr /b /c:"OS Name" /c:"OS Version"
```

##### Display file contents
```bash
type <file.ext>
```

##### Get list of processes running, sorted by name.
```bash
tasklist /NH | sort
```

```bash
whoami /priv
```

# Network Information
##### List All Interfaces
```bash
ipconfig
```

# Services
##### Get Installed Services
```bash
wmic service list

wmic service get name,displayname,pathname,startmode

# Get Service by name.
# Note no spaces before and after =
wmic service where name="" get name,displayname,pathname,startmode,state

# Get Auto Start Services
# Note no spaces before and after =
wmic service where StartMode="Auto" get Name, State

# Start service
sc start <service name>

# Stop service
sc stop <service name>

# Get service state
sc query <service name>
wmic service where name="" get state
```

##### Look for Unquoted Service Paths
```bash
wmic service get name, displayname, pathname, startmode | findstr /i "auto" | findstr /i /v "C:\Windows\\" | findstr /i /v """
```
##### Query Service
```bash
sc qc <Service Name>
```

##### Start Service
```bash
sc start <service name>
```

##### Stop Service
```bash
sc stop <service name>
```

### Get List of Running Services
##### With net
```bash
net start
```
##### With wmic
```bash
wmic service where 'started=true' get caption
```
##### With wmic by name
```bash
wmic service where 'Caption like "Remote%" and started=true' get caption
```

# Security
### Users
##### Add User
```bash
net user <Username> <Password> /add
```

### Groups
##### List Local Groups
```bash
net localgroup
```
##### List Members of a Local Group
```bash
net localgroup <Group Name in quotes>
```
##### Add User to a Local Group
```bash
net localgroup <Group Name in quotes> <Username> /add
```

# References
[Windows Command Line cheatsheet (part 2): WMIC](https://andreafortuna.org/2017/08/09/windows-command-line-cheatsheet-part-2-wmic/)