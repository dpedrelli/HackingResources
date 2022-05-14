# Enumerate Users
```bash
# Bash for loop
for u in $(cat users.txt); do rpcclient -U "" <IP Address> -N 	--command="lookupnames $u"; done | grep "User: 1"
```