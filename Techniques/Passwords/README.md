# Linux Passwd / Shadow
### [Password Hashes](../../References/LinuxHashes.md#Shadow-File-Password-Hashes)

### John The Ripper
##### [Unshadow Linux Hashes Cracking](../../Tools/Credentials/JohnTheRipper/README.md#Unshadow-for-Linux-Hashes-Cracking)

##### [Crack Linux Hashes](../../Tools/Credentials/JohnTheRipper/README.md#Crack-Linux-Hashes)

### MimiPenguin
##### [Run as Shell Script](../../Tools/Credentials/MimiPenguin/README.md#Run-as-Shell-Script)

##### [Run as Python Script](../../Tools/Credentials/MimiPenguin/README.md#Run-as-Python-Script)

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

# References
[statistically-likely-usernames](https://github.com/insidetrust/statistically-likely-usernames)

[theHarvester](https://github.com/laramies/theHarvester)

[smtp-user-enum](https://pentestmonkey.net/tools/user-enumeration/smtp-user-enum)

[smtp_enum](https://www.rapid7.com/db/modules/auxiliary/scanner/smtp/smtp_enum/)

[thc-hydra](https://github.com/vanhauser-thc/thc-hydra)

[smb_login](https://www.rapid7.com/db/modules/auxiliary/scanner/smb/smb_login/)

[owa_login](https://www.rapid7.com/db/modules/auxiliary/scanner/http/owa_login/)

[Reverse brute-force attack](https://en.wikipedia.org/wiki/Brute-force_attack#Reverse_brute-force_attack)

