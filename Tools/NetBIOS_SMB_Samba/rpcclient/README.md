# Enumerate Users with Bash Script
```bash
# Bash for loop
for u in $(cat users.txt); do rpcclient -U "" <Target Host> -N 	--command="lookupnames $u"; done | grep "User: 1"
```

# Enumerate Domains
```bash
# Connect to Host
enumdomains
```

# Enumerate Users
```bash
# Connect to Host
enumdomusers
```

# Enumerate Groups
```bash
# Connect to Host
enumdomgroups
```

# Query User
```bash
# Connect to Host
queryuser <Username>
```

# Connect to Host
```bash
rpcclient -U <Username> <Target Host>
# -N = Don't ask for password
rpcclient -U <Username> -N <Target Host>
```