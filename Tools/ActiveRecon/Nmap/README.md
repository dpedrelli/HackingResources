# [Nmap](https://nmap.org/)

| Scan Type              | Example Command                           |
|------------------------|-------------------------------------------|
| ARP Scan               | sudo nmap -PR -sn MACHINE_IP/24           |
| ICMP Echo Scan         | sudo nmap -PE -sn MACHINE_IP/24           |
| ICMP Timestamp Scan    | sudo nmap -PP -sn MACHINE_IP/24           |
| ICMP Address Mask Scan | sudo nmap -PM -sn MACHINE_IP/24           |
| TCP SYN Ping Scan      | sudo nmap -PS22,80,443 -sn MACHINE_IP/30  |
| TCP ACK Ping Scan      | sudo nmap -PA22,80,443 -sn MACHINE_IP/30  |
| UDP Ping Scan          | sudo nmap -PU53,161,162 -sn MACHINE_IP/30 |

| Option | Purpose                          |
|--------|----------------------------------|
| -n     | no DNS lookup                    |
| -R     | reverse-DNS lookup for all hosts |
| -sn    | host discovery only              |

| Port Scan Type   | Example Command             |
|------------------|-----------------------------|
| TCP Connect Scan | nmap -sT MACHINE_IP         |
| TCP SYN Scan     | sudo nmap -sS MACHINE_IP    |
| UDP Scan         | sudo nmap -sU MACHINE_IP    |

| Option                | Purpose                                  |
|-----------------------|------------------------------------------|
| -p-                   | all ports                                |
| -p1-1023              | scan ports 1 to 1023                     |
| -F                    | 100 most common ports                    |
| -r                    | scan ports in consecutive order          |
| -T<0-5>         | -T0 being the slowest and T5 the fastest       |
| --max-rate 50         | rate <= 50 packets/sec                   |
| --min-rate 15         | rate >= 15 packets/sec                   |
| --min-parallelism 100 | at least 100 probes in parallel          |


| Types of Scans | Flags         | Option      | Response           | Closed   |
|----------------|---------------|-------------|--------------------|----------|
| Null Scan      | none          | -sN         | No = Open/Filtered | RST      |
| FIN Scan       | FIN           | -sF         | No = Open/Filtered | RST      |
| Xmas Scan      | FIN, PSH, URG | -sX         | No = Open/Filtered | RST, ACK |
| Maimon Scan    | FIN, ACK      | -sM         |                    |          |
| ACK Scan       | ACK           | -sA         | RST = Open/Closed  |          |
| Window Scan    | ACK           | -sW         | RST = Open/Closed  |          |
| Custom Scan    |               | --scanflags |                    |          |

Spoofed, Decoy, and Idle (Zombie) Scanning
```bash
nmap -e NET_INTERFACE -Pn -S SPOOFED_IP 10.10.67.92 --spoof-mac SPOOFED_MAC
nmap -D 10.10.0.1,10.10.0.2,RND,RND,ME 10.10.67.92
nmap -sI 10.10.5.5
```

| Port Scan Type                 | Example Command                                     |
|--------------------------------|-----------------------------------------------------|
| TCP Null Scan                  | sudo nmap -sN MACHINE_IP                            |
| TCP FIN Scan                   | sudo nmap -sF MACHINE_IP                            |
| TCP Xmas Scan                  | sudo nmap -sX MACHINE_IP                            |
| TCP Maimon Scan                | sudo nmap -sM MACHINE_IP                            |
| TCP ACK Scan                   | sudo nmap -sA MACHINE_IP                            |
| TCP Window Scan                | sudo nmap -sW MACHINE_IP                            |
| Custom TCP Scan                | sudo nmap --scanflags URGACKPSHRSTSYNFIN MACHINE_IP |
| Spoofed Source IP              | sudo nmap -S SPOOFED_IP MACHINE_IP                  |
| Spoofed MAC Address            | --spoof-mac SPOOFED_MAC                             |
| Decoy Scan                     | nmap -D DECOY_IP,ME MACHINE_IP                      |
| Idle (Zombie) Scan             | sudo nmap -sI ZOMBIE_IP MACHINE_IP                  |
| Fragment IP data into 8 bytes  | -f                                                  |
| Fragment IP data into 16 bytes | -ff                                                 |

| Option                 | Purpose                                  |
|------------------------|------------------------------------------|
| --source-port PORT_NUM | specify source port number               |
| --data-length NUM      | append random data to reach given length |

| Option   | Purpose                               |
|----------|---------------------------------------|
| --reason | explains how Nmap made its conclusion |
| -v       | verbose                               |
| -vv      | very verbose                          |
| -d       | debugging                             |
| -dd      | more details for debugging            |


| Script Category | Description                                                            |
|-----------------|------------------------------------------------------------------------|
| auth            | Authentication related scripts                                         |
| broadcast       | Discover hosts by sending broadcast messages                           |
| brute           | Performs brute-force password auditing against logins                  |
| default         | Default scripts, same as -sC                                           |
| discovery       | Retrieve accessible information, such as database tables and DNS names |
| dos             | Detects servers vulnerable to Denial of Service (DoS)                  |
| exploit         | Attempts to exploit various vulnerable services                        |
| external        | Checks using a third-party service, such as Geoplugin and Virustotal   |
| fuzzer          | Launch fuzzing attacks                                                 |
| intrusive       | Intrusive scripts such as brute-force attacks and exploitation         |
| malware         | Scans for backdoors                                                    |
| safe            | Safe scripts that won’t crash the target                               |
| version         | Retrieve service versions                                              |
| vuln            | Checks for vulnerabilities or exploit vulnerable services              |


| Option                  | Meaning                                         |
|-------------------------|-------------------------------------------------|
| -sV                     | determine service/version info on open ports    |
| -sV --version-light     | try the most likely probes (2)                  |
| -sV --version-all       | try all available probes (9)                    |
| -O                      | detect OS                                       |
| --traceroute            | run traceroute to target                        |
| --script=SCRIPTS        | Nmap scripts to run                             |
| -sC or --script=default | run default scripts                             |
| -A                      | equivalent to -sV -O -sC --traceroute           |
| -oN                     | save output in normal format                    |
| -oG                     | save output in grepable format                  |
| -oX                     | save output in XML format                       |
| -oA                     | save output in normal, XML and Grepable formats |


##### Scan Network For Hosts
```bash
nmap -sn <IP Address>/<Network ID>
```

##### Scan Network For Hosts And Save To File
```bash
nmap -sn <IP Address>/<Network ID> | grep "Nmap scan report for" | cut -d ' ' -f5 > hosts
```

##### Scan All Ports with Hosts File
```bash
sudo nmap -sS -sU -p- -iL <Filename>
```

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

# SMTP
### Enumerate SMTP Verbs
```bash
nmap --script smtp-commands <SMTP Host> -p 25
```

### Enumerate SMTP Users
```bash
nmap --script smtp-enum-users <SMTP Host> -p 25
```

## SMTP References
[smtp-enum-users](https://nmap.org/nsedoc/scripts/smtp-enum-users.html)