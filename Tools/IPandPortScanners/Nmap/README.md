# [Nmap](https://nmap.org/)

##### Bruteforce DNS
```bash
nmap -p 53 dns-brute domain.com
```

### Avoid Detection
##### Decoy / Spoof IP (Avoid Detection)
```bash
# Random IPs
nmap -sS -D RND:<# of IPs> nmap.scanme.org

# Specified IP
nmap -sS -D <Spoofed IP Address 1,Spoofed IP Address 1> nmap.scanme.org
```
##### Fragment Packets (Avoid Detection)
```bash
# -f defaults to 4 bytes. --send-eth makes it 8 bytes.
nmap -sS -f --send-eth
```
##### MTU (Avoid Detection)
```bash
# Like -f, but can specify packet size.
# Without --send-eth, packet size will be 4 bytes, as with -f.
nmap -sS --mtu <Size in bytes 8, 16, 24, 32...> --send-eth
```

##### [Reference Guide](https://nmap.org/book/man.html)