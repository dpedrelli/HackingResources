# [Nmap](https://nmap.org/)

##### Bruteforce DNS
```bash
nmap -p 53 dns-brute domain.com
```

##### TCP / Three-Way Handshake Scan (Default)
```bash
nmap -sT
```

##### SYN Scan
```bash
# Faster than TCP and offers some stealth.
sudo nmap -sS
```

##### UDP Scan
```bash
nmap -sU
```

##### Check Firewalls / ACK Scan
```bash
# Not for determining open ports, but filtered/unfiltered ports.
nmap -sA
```

##### IP Protocols
```bash
# Not a port scanner
nmap -sO
```

### Avoid Detection
##### Never Do DNS Resolution
```bash
# Faster and more stealthy, when hostnames are not required.
nmap -n
```

##### FTP Bounce
```bash
nmap -b
```

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
##### Idle / Zombie Scan
```bash
# Check zombie prospect for incremental IP ID
nmap -O -v -n <Zombie IP>
nmap -Pn -v -sI <Zombie IP>:<Port> <Target IP> -p<ports>
```

##### [Reference Guide](https://nmap.org/book/man.html)