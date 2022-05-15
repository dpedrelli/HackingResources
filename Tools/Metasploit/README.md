# Nmap Scan with Metasploit

This will perform a nmap scan and feed the results into Metasploit.
```bash
msfconsole
db_nmap
```

# SMTP
### Enumerate SMTP Users
```bash
msfconsole -q
search smtp_enum

use auxiliary/scanner/smtp/smtp_enum
# or
use 0
show options

set RHOSTS <SMTP Host>
set USER_FILE <Wordlist>
run
```