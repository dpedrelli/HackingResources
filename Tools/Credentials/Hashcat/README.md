# [Hashcat](https://hashcat.net/hashcat/)

### Found Passwords
```bash
/home/kali/.hashcat/hashcat.potfile
```

### Show Cracked Passwords
```bash
--show

hashcat -m 1000 <passwordhash> --show
```

### Show Uncracked Passwords
```bash
--left
```

### Linux Shadow Passwords
```bash
hashcat -m 500 -a 0 -o cracked.txt hashes.txt /usr/share/wordlists/rockyou.txt -O
```

### MD5
```bash
hashcat -m 0 <passwordhash> /usr/share/wordlists/rockyou.txt -O
```

### NTLM
```bash
hashcat -m 1000 -a 0 <passwordhash> /usr/share/wordlists/rockyou.txt -O

pirate:1001:aad3b435b51404eeaad3b435b51404ee:8ce9a3ebd1647fcc5e04025019f4b875:::
hashcat -m 1000 -a 0 8ce9a3ebd1647fcc5e04025019f4b875 /usr/share/wordlists/rockyou.txt -O --show 

echo 8ce9a3ebd1647fcc5e04025019f4b875 > hash.txt
hashcat -m 1000 -a 0 hash.txt /usr/share/wordlists/rockyou.txt -O --show
```

### [Mask Attack](https://blog.codyrichardson.io/2020/06/hashcat-cracking-md5-and-ntlm-hashes.html)
```bash

```

### SHA-512 (Pasword, Salt)
```bash
hashcat -m 1710 -a 0 "<password>:<salt>" /usr/share/wordlists/rockyou.txt -O --show
```