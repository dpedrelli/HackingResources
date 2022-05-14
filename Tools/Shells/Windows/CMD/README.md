##### Get Windows Version
```bash
systeminfo | findstr /b /c:"OS Name" /c:"OS Version"
```

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

##### Display file contents
```bash
type <file.ext>
```

##### Get List of Running Services
```bash
netstart
```

##### Get list of processes running, sorted by name.
```bash
tasklist /NH | sort
```