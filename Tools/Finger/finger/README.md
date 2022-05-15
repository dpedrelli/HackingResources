# Finger Username
```bash
finger <Username>@<Target Host>
```

# Enumerate Users with Wordlist
```bash
for name in $(cat <Wordlist>); do finger $name@<Target Host>; done > valid_users.txt
cat valid_users.txt
```