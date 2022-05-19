# List Resources Shared By A Computer
```bash
net view <Target Host>
```

# Connect to a Share on a Remote Computer
```bash
net use Z: \\<Target Host>\<Share Name>\
```

# NULL Session
```bash
# Connect to IPC$ with null password and empty username.
net use \\<Target Host>\IPC$ "" /u:""
```