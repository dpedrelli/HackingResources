##### Install polenum to use with enum4linux.

# Enumerate All
```bash
enum4linux -a <IP Address>
```

# Enumerate OS
```bash
enum4linux -o <IP Address>
```

# Enumerate Shares
```bash
enum4linux -S <IP Address>
```

# Enumerate Users
```bash
enum4linux -U <IP Address>
```

# Enumerate Users with RID Cycling
```bash
enum4linux -r <IP Address> | grep "Local User"
```

# Cheat Sheets
[HighOn.Coffee Cheat Sheet](https://highon.coffee/blog/enum4linux-cheat-sheet/)

# References
[enum4linux](https://github.com/CiscoCXSecurity/enum4linux)