# [Nmap](https://nmap.org/)

##### Bruteforce DNS
```bash
nmap -p 53 dns-brute domain.com
```

##### Do Not Perform Port Scan
```bash
nmap -sn
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

##### Fingerprint OS
```bash
# Utilizing nmap's aggressive, OS detection.
nmap -O --osscan-guess <IP Address>
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
# Use NSE to check for candidate
nmap --script ipidseq <Zombie IP> -p 135

nmap -Pn -v -sI <Zombie IP>:<Port> <Target IP> -p<ports>
```

##### Specify Source Port
```bash
nmap --source-port 53
nmap -g 53
```

##### Disable ARP Ping
```bash
nmap --disable-arp-ping
```

##### Fragment Packet
```bash
# Default packet is 24 bytes

# 8 bytes
nmap -f

# 16 bytes
nmap -f -f
```

##### Use Decoys
```bash
nmap -D <IP 1>,<IP 2>,ME,<IP 3>...

# Random Decoys
nmap -D RND:10
```

##### Specify Size of Datagram (Help to Avoid Port Scan Detection)
```bash
nmap --data-length <size>

# Add an extra 10 bytes
nmap --data-length 10
```

##### Spoof MAC
```bash
# Specify Vendor
nmap --spoof-mac apple

# Random MAC
nmap --spoof-mac 0

# Specify MAC
nmap --spoof-mac <MAC Address>
```

##### Randomize Host
```bash
# hosts.txt contains list of IP addresses.
nmap -iL hosts.txt --randomize-hosts
```

### NSE
##### Find Scripts
```bash
# Find all scripts that start with SMB and are in the category discovery.
nmap --script-help "smb*" and discovery
```

##### Update NSE Scripts
```bash
nmap --script-updatedb
```

##### Execute All Scripts In Category
```bash
nmap --script auth <Target IP>
```

##### [Reference Guide](https://nmap.org/book/man.html)

### NetBIOS, SMB, Samba
##### Determine versions of NetBIOS ports
```bash
nmap -sT -sU -sV <IP Address> -p135,137,138,139,445 --open
```
##### Enumerate SMB Shares
```bash
nmap --script smb-enum-shares <IP Address>
```