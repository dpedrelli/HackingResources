# [Nmap / Zenmap](https://nmap.org/)

# [Host Discovery](https://nmap.org/book/host-discovery.html)
* [Host Discovery](https://nmap.org/book/man-host-discovery.html)
##### ARP Ping Scan
```bash
ifconfig
# Get Subnet

nmap -PR -sn [Target Host]/[Network ID]

nmap -PR -sn 172.16.5.0/24
nmap -PR -sn 172.16.5.*
```

##### Ping Sweep
```bash
# Invidiual Host
nmap -sn [Target Host]
# IP Range
nmap -sn [Target Host]/[Network ID]
# If target is on same network as attack machine, nmap uses and ARP ping, rather than ICMP.

# Save To File
nmap -sn [Target Host]/[Network ID] | grep "Nmap scan report for" | cut -d ' ' -f5 > hosts

# Force Ping
sudo nmap -sn [Target Host] --disable-arp-ping
sudo nmap -sn [Target Host] --send-ip
# 1) Sends ICMP Echo to target.
# 2) Sends TCP SYN packet on port 443.
# 3) Sends TCP ACK packet on port 80.
# 4) Sends ICMP Timestamp.

# Include Probe Option - SYN Flag
sudo nmap -sn -PS [Target Host] --disable-arp-ping
# 1) Sends SYN Flag
# 2) If target is live and port is open, target will respond with SYN/ACK, for three-way handshake.
# 3) Attack machine sends RST.

# Include Probe Option - SYN Flag and Specify Port #
sudo nmap -sn -PS53 [Target Host] --disable-arp-ping

# Include Probe Option - ACK Flag
sudo nmap -sn -PA [Target Host] --disable-arp-ping
# Default port 80.

# Include Probe Option - UDP
sudo nmap -sn -PU [Target Host] --disable-arp-ping
# Default port 40125.

# Include Probe Option - SCTP INIT
sudo nmap -sn -PY [Target Host] --disable-arp-ping
# Default port 80.

# Include Probe Option - ICMP Echo
sudo nmap -sn -PE [Target Host] --disable-arp-ping

# Include Probe Option - ICMP Netmask
sudo nmap -sn -PM [Target Host] --disable-arp-ping

# Include Probe Option - ICMP Timestamp
sudo nmap -sn -PP [Target Host] --disable-arp-ping
```

##### No Ping
```bash
nmap -n -sn -PS22,80,135,443,445 [Target Host]/[Network ID]
```

##### Host Discovery Options
| Parameter                          | Description                                                 |
|------------------------------------|-------------------------------------------------------------|
| -sL:                               | List Scan - simply list targets to scan                     |
| -sn:                               | Ping Scan - disable port scan                               |
| -Pn:                               | Treat all hosts as online -- skip host discovery            |
| -PS/PA/PU/PY[portlist]:            | TCP SYN/ACK, UDP or SCTP discovery to given ports           |
| -PE/PP/PM:                         | ICMP echo, timestamp, and netmask request discovery probes  |
| -PO[protocol list]:                | IP Protocol Ping                                            |
| -n/-R:                             | Never do DNS resolution/Always resolve [default: sometimes] |
| --dns-servers <serv1[,serv2],...>: | Specify custom DNS servers                                  |
| --system-dns:                      | Use OS's DNS resolver                                       |
| --traceroute:                      | Trace hop path to each host                                 |

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

### Host Discovery References
[Nmap Ping Sweep](https://linuxhint.com/nmap_ping_sweep/)


# Port Scan
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

##### Scan Multiple Hosts
```bash
sudo nmap [Target Host 1] [Target Host 2] [Target Host 3]

# With File
sudo nmap -iL [Filename]
```

##### Scan Techniques
| Parameter                      | Description                               |
|--------------------------------|-------------------------------------------|
| -sS/sT/sA/sW/sM:               | TCP SYN/Connect()/ACK/Window/Maimon scans |
| -sU:                           | UDP Scan                                  |
| -sN/sF/sX:                     | TCP Null, FIN, and Xmas scans             |
| --scanflags [flags]:           | Customize TCP scan flags                  |
| -sI <zombie host[:probeport]>: | Idle scan                                 |
| -sY/sZ:                        | SCTP INIT/COOKIE-ECHO scans               |
| -sO:                           | IP protocol scan                          |
| -b [FTP relay host]:           | FTP bounce scan                           |


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
| -T<0-5>               | -T0 being the slowest and T5 the fastest |
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

# Routing
##### Routing Trough ProxyChains
```bash
# ProxyChains provide anonymity, but can also work with routes to access hosts on other subnets.
# Run nmap scan to find open ports that can be used with port forwarding
# [Target Host] is not reachable by [Attack Host]
proxychains nmap -sT -Pn -p 21-25,80,139,445,8080 [Target Host]
```


# Evasion

##### Never Do DNS Resolution
```bash
# Use whenever possible.
# Faster and more stealthy, when hostnames are not required.
nmap -n
```

##### FTP Bounce
```bash
nmap -b
```

##### Fragmented Packets and Data Length
By default, nmap adds zero data to the IP header, for fragmented packets.  Combining fragments with ```--data-length``` with add random data to the header and increase the number of fragments, because nmap splits the header into 8 byte fragments.  The default packet size is 24 bytes.  16 of those bytes make-up the IP header and the remaining 8 bytes make-up the TCP SYN packet.  Add 24 to the number of bytes specified with ```--data-length``` and divide by the fragmentation size and divide by the fragment size, to get the number of packets sent.

| Flag  | Packet Size |
|-------|-------------|
| none  | 24 bytes    |
| -f    | 8 bytes     |
| -f -f | 16 bytes    |

```bash
# Fragment packet into 8 bytes
nmap -f

# Fragment packet into 16 bytes
nmap -f -f

# Specify Size of Datagram / Add Random Data
nmap --data-length <size>

# Combine Fragments with Data Length
nmap -f --data-length 48 -sS [Target Host] -p <Port #>
# Default packet size of 24 bytes + 56 bytes (--data-length) = 80 bytes / 8 bytes (-f) = 10 packets
```

##### MTU 
```bash
# Like -f, but can specify packet size.
# Without --send-eth, packet size will be 4 bytes, as with -f.
nmap -sS --mtu <Size in bytes 8, 16, 24, 32...> --send-eth
```

##### Decoy / Spoof IP
```bash
# Random IPs
nmap -sS -D RND:<# of IPs> nmap.scanme.org
# nmap includes the Attacker's address, among the random addresses.

# Specified IP
nmap -sS -D <Spoofed IP Address 1,Spoofed IP Address 2> nmap.scanme.org
sudo nmap -D 192.168.1.5,ME,192.168.1.25 [Target Host]

# Decoys do not work with -sT or -sV, because they require full connections.
```
##### Idle / Zombie Scan
```bash
# Check zombie prospect for incremental IP ID
nmap -O -v -n <Zombie IP> -p <Open Port>
# Use NSE to check for candidate
nmap --script ipidseq <Zombie IP> -p <Open Port>

nmap -Pn -v -sI <Zombie IP>:<Port> <Target IP> -p<ports>
```

##### Spoofed, Decoy, and Idle (Zombie) Scanning
```bash
nmap -e NET_INTERFACE -Pn -S SPOOFED_IP 10.10.67.92 --spoof-mac SPOOFED_MAC
nmap -D 10.10.0.1,10.10.0.2,RND,RND,ME 10.10.67.92
nmap -sI 10.10.5.5
```

##### Specify Source Port
```bash
# May evade detection by performing port scan, while specifying port 53 (DNS) as the source port.
nmap --source-port 53
nmap -g 53
```

##### Disable ARP Ping
```bash
nmap --disable-arp-ping
```

##### Use Decoys
```bash
nmap -D <IP 1>,<IP 2>,ME,<IP 3>...

# Random Decoys
nmap -D RND:10
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
# hosts.txt contains list of IP addresses of hosts that are alive and some that are not.
nmap -iL hosts.txt --randomize-hosts
```

##### Check Firewalls / ACK Scan
```bash
# Not for determining open ports, but filtered/unfiltered ports.
nmap -sA
```

| Flag                                          | Evasion & Spoofing         |
|-----------------------------------------------|----------------------------|
| -f; --mtu [val]:                              | fragment packets (optionally w/given MTU) |
| -D <decoy1,decoy2[,ME],...>:                  | Cloak a scan with decoys |
| -S <IP_Address>:                              | Spoof source address |
| -e [iface>:                                   | Use specified interface |
| -g/--source-port [portnum]:                   | Use given port number |
| --proxies <url1,[url2],...>:                  | Relay connections through HTTP/SOCKS4 proxies |
| --data [hex string]:                          | Append a custom payload to sent packets |
| --data-string [string]:                       | Append a custom ASCII string to sent packets |
| --data-length [num]:                          | Append random data to sent packets |
| --ip-options [options]:                       | Send packets with specified ip options |
| --ttl [val]:                                  | Set IP time-to-live field |
| --spoof-mac <mac address/prefix/vendor name>: | Spoof your MAC address |
| --badsum:                                     | Send packets with a bogus TCP/UDP/SCTP checksum |


| Flag     | Timing                                 |
|----------|----------------------------------------| 
| -T<0-5>: | Set timing template (higher is faster) |
| --min-hostgroup/max-hostgroup [size]: | Parallel host scan group sizes |
| --min-parallelism/max-parallelism [numprobes]: | Probe parallelization |
| --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout [time]: | Specifies probe round trip time. |
| --max-retries [tries]: | Caps number of port scan probe retransmissions. |
| --host-timeout [time]: | Give up on target after this long |
| --scan-delay/--max-scan-delay [time]: | Adjust delay between probes |
| --min-rate [number]: | Send packets no slower than [number] per second |
| --max-rate [number]: | Send packets no faster than [number] per second |
| |  Options which take [time] are in seconds, or append 'ms' (milliseconds), 's' (seconds), 'm' (minutes), or 'h' (hours) to the value (e.g. 30m).|

| Flag | Template   | Time        |
|------|------------|-------------|
| -T0  | Paranoid   | 5 min       |
| -T1  | Sneaky     | 15 sec      |
| -T2  | Polite     | 0.4 sec     |
| -T3  | Normal     | default     |
| -T4  | Aggressive | 10 millisec |
| -T5  | Insane     | 5 millisec  |

### Evasion References
##### [Firewall/IDS Evasion and Spoofing](https://nmap.org/book/man-bypass-firewalls-ids.html)
##### [TCP Idle Scan (-sI)](https://nmap.org/book/idlescan.html)

# Version Detection / Fingerprinting
##### Get Service Versions
```bash
nmap -sV
nmap -sV --version-all
```

##### IP Protocols
```bash
# Not a port scanner
nmap -sO
```

##### Fingerprint OS
```bash
# Utilizing nmap's aggressive, OS detection.
nmap -n -O --osscan-guess [Target Host]

# Very noisy. OS detection, version detection, script scanning, and traceroute
nmap -n -A [Target Host]

nmap -n --script smb-os-discovery -p445 [Target Host]
```

| Flag | OS Detection |
|------|--------------|
| -O:  | Enable OS detection |
| --osscan-limit: | Limit OS detection to promising targets |
| --osscan-guess: | Guess OS more aggressively |
| -A: | Enable OS detection, version detection, script scanning, and traceroute |

| Flag | Service / Version Detection |
|------|-----------------------------|
| -sV: | Probe open ports to determine service/version info |
| --version-intensity [level]: | Set from 0 (light) to 9 (try all probes) |
| --version-light: | Limit to most likely probes (intensity 2) |
| --version-all: | Try every single probe (intensity 9) |
| --version-trace: | Show detailed version scan activity (for debugging) |

# Scripts
##### Find Scripts
```bash
# Find all scripts that start with SMB and are in the category discovery.
nmap --script-help "smb*" and discovery

# By just name.
nmap --script-help "whois-domain"
```

##### Update NSE Scripts
```bash
nmap --script-updatedb
```

##### Default Category
```bash
# Info related to target OS, workgroup, and NetBIOS
nmap --script default <Target IP>
```

##### Execute All Scripts In Category
```bash
nmap --script auth <Target IP>
```

##### Query WHOIS
```bash
nmap --script whois-domain <Target IP> -sn
```

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
| safe            | Safe scripts that won�t crash the target                               |
| version         | Retrieve service versions                                              |
| vuln            | Checks for vulnerabilities or exploit vulnerable services              |

# Services
### DNS
##### Brute Force DNS
```bash
# Bruteforce DNS
nmap -p 53 --script dns-brute <TargetDomain.com>
```

##### Identify DNS Servers on a LAN
```bash
nmap -sV -p 53 [Target Host]/<Subnet> --open
```

### Finger
##### Enumerate Users with Finger
```bash
nmap --script finger [Target Host] -p 79
```

### NetBIOS, SMB, Samba
##### Determine versions of NetBIOS ports
```bash
nmap -sT -sU -sV [Target Host] -p135,137,138,139,445 --open
```
##### Enumerate SMB Shares
```bash
nmap --script smb-enum-shares -p 445 [Target Host]
```
##### Enumerate SMB Users
```bash
nmap --script smb-enum-users -p 445 [Target Host]
```
##### SMB OS Discovery
```bash
nmap -n --script smb-os-discovery -p445 [Target Host]
nmap -n -O --osscan-guess --script smb-os-discovery -p445 [Target Host]
```
##### SMB Protocols
```bash
nmap -n --script smb-protocols -p445 [Target Host]
```
##### SMB Security Mode
```bash
nmap -n --script smb-security-mode -p445 [Target Host]
```

### SMTP
##### Get SMTP Version
```bash
nmap -sV -p 25 <SMTP Host>
```

##### Enumerate SMTP Verbs
```bash
nmap --script smtp-commands <SMTP Host> -p 25
```

##### Enumerate SMTP Users
```bash
nmap --script smtp-enum-users <SMTP Host> -p 25
```

#### SMTP References
[smtp-enum-users](https://nmap.org/nsedoc/scripts/smtp-enum-users.html)

### SNMP
#### Enumerate SNMP
##### Enumerate Windows User Names
```bash
nmap -sU -p 161 --script snmp-win32-users [Target Host]
```
##### Enumerate SNMP on Windows
```bash
nmap -sU -p 161 --script snmp-win32-services [Target Host]
```
##### Brute Force
```bash
nmap -sU -p 161 --script snmp-brute [Target Host]
# By default, nmap uses wordlist /usr/share/nmap/nselib/data/snmpcommunities.lst

# Specify wordlist
nmap -sU -p 161 --script snmp-brute --script-args snmp-brute.communitiesdb=<wordlist> [Target Host]
# From seclists /usr/share/seclists/Discovery/SNMP/common-snmp-community-strings.txt
```

##### Run All Scripts
```bash
nmap -sU -p 161 --script snmp-* [Target Host] > snmp_output
```

# Scan for Vulneratbilities
```bash
nmap -sV --script vuln -p <Port #> [Target Host]
```

| Port Status     |    |
|-----------------|----|
| open            | An application is actively accepting TCP connections, UDP datagrams, or SCTP associations on this port. |
| closed          | A closed port is accessible (it receives and responds to Nmap probe packets), but there is no application listening on it. |
| filtered        | Nmap cannot determine whether the port is open because packet filtering prevents its probes from reaching the port. |
| unfiltered      | The unfiltered state means that a port is accessible, but Nmap is unable to determine whether it is open or closed. Only the ACK scan, which is used to map firewall rulesets, classifies ports into this state. Scanning unfiltered ports with other scan types such as Window scan, SYN scan, or FIN scan, may help resolve whether the port is open. |
| open/filtered   | Nmap places ports in this state when it is unable to determine whether a port is open or filtered. The UDP, IP protocol, FIN, NULL, and Xmas scans classify ports this way. |
| closed/filtered | This state is used when Nmap is unable to determine whether a port is closed or filtered. It is only used for the IP ID idle scan. |

# Testing
### Host Discovery
* [From the documentation](https://nmap.org/book/host-discovery-controls.html)
The -sn option sends an ICMP echo request, a TCP SYN packet to port 443, a TCP ACK packet to port 80, and an ICMP timestamp request by default. Since unprivileged Unix users (or Windows users without Npcap installed) cannot send these raw packets, only SYN packets are sent instead in those cases. The SYN packet is sent using a TCP connect system call to ports 80 and 443 of the target host. When a privileged user tries to scan targets on a local ethernet network, ARP requests (-PR) are used unless the --send-ip option is specified.
##### nmap -sn 10.0.2.0/24
```bash
nmap -sn 10.0.2.0/24
nmap --disable-arp-ping -sn 10.0.2.0/24

# Both of these commands produce the same 785 packets in Wireshark and the same results:
# They attempted TCP connections to 10.0.2.2, 10.0.2.3, and 10.0.2.4 on both ports 80 and 443.
# With addresses 10.0.2.2, 10.0.2.3, and 10.0.2.4 returning [RST, ACK]

Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-28 15:18 EDT
Nmap scan report for 10.0.2.15
Host is up (0.00012s latency).
Nmap done: 256 IP addresses (1 host up) scanned in 3.47 seconds
```

##### nmap -sn 10.0.2.1-254
```bash
nmap -sn 10.0.2.1-254

# This command generated 782 packets in Wireshark and was no faster than including the full CIDR with subnet and broadcast addresses.
Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-28 15:32 EDT
Nmap scan report for 10.0.2.15
Host is up (0.00015s latency).
Nmap done: 254 IP addresses (1 host up) scanned in 4.22 seconds
```

##### sudo nmap -sn 10.0.2.0/24
```bash
sudo nmap -sn 10.0.2.0/24

# This command generates 528 packets in Wireshark.
# 520 packets are ARP requests.  The remaining 8 requests are DNS.
# It did not produce any TCP packets.

Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-28 15:22 EDT
Nmap scan report for 10.0.2.2
Host is up (0.000090s latency).
MAC Address: 52:54:00:12:35:02 (QEMU virtual NIC)
Nmap scan report for 10.0.2.3
Host is up (0.000085s latency).
MAC Address: 52:54:00:12:35:03 (QEMU virtual NIC)
Nmap scan report for 10.0.2.4
Host is up (0.000096s latency).
MAC Address: 52:54:00:12:35:04 (QEMU virtual NIC)
Nmap scan report for 10.0.2.15
Host is up.
Nmap done: 256 IP addresses (4 hosts up) scanned in 2.08 seconds
```

##### nmap -sn -PE 10.0.2.0/24 ICMP Echo Only
```bash
nmap -sn -PE 10.0.2.0/24

# Generated 773 packets in Wireshark.
# It produced the TCP packets for ports 80 and 443, but no ICMP.
# It attempted TCP connections to 10.0.2.2, 10.0.2.3, and 10.0.2.4 on both ports 80 and 443.
# It addresses 10.0.2.2, 10.0.2.3, and 10.0.2.4 returning [RST, ACK]

Warning:  You are not root -- using TCP pingscan rather than ICMP
Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-28 16:35 EDT
Nmap scan report for 10.0.2.15
Host is up (0.00025s latency).
Nmap done: 256 IP addresses (1 host up) scanned in 3.49 seconds
```
##### sudo nmap -sn -PE 10.0.2.0/24 ICMP Echo Only
```bash
sudo nmap -sn -PE 10.0.2.0/24

# Produced 528 packets in Wireshark.
# Like the previous sudo command, it produced 520 packets of ARP and 8 packets of DNS traffic, not ICMP.

Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-28 16:37 EDT
Nmap scan report for 10.0.2.2
Host is up (0.000068s latency).
MAC Address: 52:54:00:12:35:02 (QEMU virtual NIC)
Nmap scan report for 10.0.2.3
Host is up (0.000063s latency).
MAC Address: 52:54:00:12:35:03 (QEMU virtual NIC)
Nmap scan report for 10.0.2.4
Host is up (0.00049s latency).
MAC Address: 52:54:00:12:35:04 (QEMU virtual NIC)
Nmap scan report for 10.0.2.15
Host is up.
Nmap done: 256 IP addresses (4 hosts up) scanned in 2.10 seconds
```

##### sudo nmap -sn -PU 10.0.2.0/24 UDP (MUST RUN AS SUDO)
```bash
sudo nmap -sn -PU 10.0.2.0/24

# Produced 528 packets in Wireshark.
# Like the previous sudo command, it produced 520 packets of ARP and 8 packets of DNS traffic, not ICMP.

Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-28 16:41 EDT
Nmap scan report for 10.0.2.2
Host is up (0.000077s latency).
MAC Address: 52:54:00:12:35:02 (QEMU virtual NIC)
Nmap scan report for 10.0.2.3
Host is up (0.000073s latency).
MAC Address: 52:54:00:12:35:03 (QEMU virtual NIC)
Nmap scan report for 10.0.2.4
Host is up (0.000095s latency).
MAC Address: 52:54:00:12:35:04 (QEMU virtual NIC)
Nmap scan report for 10.0.2.15
Host is up.
Nmap done: 256 IP addresses (4 hosts up) scanned in 2.07 seconds
```
##### sudo nmap -n -sn --send-ip 10.0.2.0/24 (Must call as sudo or uses TCP)
```bash
sudo nmap -n -sn --send-ip 10.0.2.0/24

# Generated 3149 packets in Wireshark.
# Most packets were ARP broadcast, with some ICMP echo packets to/from 10.0.2.2, 10.0.2.3, and 10.0.2.4.

Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-28 16:52 EDT
Nmap scan report for 10.0.2.2
Host is up (0.00033s latency).
MAC Address: 52:54:00:12:35:02 (QEMU virtual NIC)
Nmap scan report for 10.0.2.3
Host is up (0.00032s latency).
MAC Address: 52:54:00:12:35:02 (QEMU virtual NIC)
Nmap scan report for 10.0.2.4
Host is up (0.00031s latency).
MAC Address: 52:54:00:12:35:02 (QEMU virtual NIC)
Nmap scan report for 10.0.2.255
Host is up (2.0s latency).
MAC Address: 52:54:00:12:35:02 (QEMU virtual NIC)
Nmap scan report for 10.0.2.15
Host is up.
Nmap done: 256 IP addresses (5 hosts up) scanned in 20.42 seconds
```
##### nmap -n -sn -PR --packet-trace --send-eth 10.0.2.0/24 (Must call as sudo or uses TCP)
```bash
sudo nmap -n -sn -PR --packet-trace --send-eth 10.0.2.0/24

# Generated 520 packets in Wireshark.
# Traffic was exclusively ARP broadcasts.

Nmap scan report for 10.0.2.2
Host is up (0.000055s latency).
MAC Address: 52:54:00:12:35:02 (QEMU virtual NIC)
Nmap scan report for 10.0.2.3
Host is up (0.000043s latency).
MAC Address: 52:54:00:12:35:03 (QEMU virtual NIC)
Nmap scan report for 10.0.2.4
Host is up (0.000083s latency).
MAC Address: 52:54:00:12:35:04 (QEMU virtual NIC)
Nmap scan report for 10.0.2.15
Host is up.
Nmap done: 256 IP addresses (4 hosts up) scanned in 2.02 seconds
```

# Grep
##### Grep Result for Hosts
```bash
grep "Nmap scan report for" | cut -d ' ' -f5 > hosts
```
##### Grep gnamp for Hosts
```bash
cat TcpOpenPorts.gnmap | grep Ports: | cut -f1 | cut -d ' ' -f2
```
##### Grep gnmap for Ports
```bash
cat TcpOpenPorts.gnmap | grep Ports: | cut -f2 | cut -f1 | cut -c 8-
```

# Cheatsheets
[Tutorials Point](https://www.tutorialspoint.com/nmap-cheat-sheet)

# References
[NSEDoc Reference Portal](https://nmap.org/nsedoc/)

[Reference Guide](https://nmap.org/book/man.html)

# Zenmap
[How to Install Zenmap in Kali Linux 2022.1 without any Error](https://techdhee.in/install-zenmap-in-kali-linux/)