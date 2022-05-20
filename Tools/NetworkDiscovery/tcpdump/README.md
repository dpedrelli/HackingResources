##### tcpdump must be run as sudo, when capturing traffic, but not for other operations.

# Dump Traffic
```bash
sudo tcpdump -i <Interface Name> 
```

# Dump Traffic with Detail
```bash
sudo tcpdump -i <Interface Name> -xxAXXSs 0

sudo tcpdump -i <Interface Name> -vvvASs 0
```

# List Available Interfaces
```bash
tcpdump -D
```

# Prevent Reverse DNS of IP Address to Names
```bash
sudo tcpdump -i <Interface Name> -n
```

# Quiet
```bash
sudo tcpdump -i <Interface Name> -q
```

# Limit Traffic to Host
```bash
sudo tcpdump -i <Interface Name> host <HostName>
```

# Limit Traffic by Source and Destination
```bash
sudo tcpdump -i <Interface Name> src <Source IP> and dst <Destination IP>
```

# Limit Number of Packets Captured
```bash
sudo tcpdump -i <Interface Name> -c <Number of Packets>
```

# Import Filters from File
```bash
# Create file filters.txt with filter, such as:
# Port 80
sudo tcpdump -i <Interface Name> -F filters.txt
```

# Output to File
```bash
sudo tcpdump -i <Interface Name> -w output.txt

# To read the captured file
sudo tcpdump -i <Interface Name> -r output.txt
```

# Filter Output with Grep
```bash
sudo tcpdump -i <Interface Name> | grep 192.168.1.1
```

| Flag | Description |
|------|-------------|
| -dst | Only display packets with specified destination |
| -A   | Print each packet (minus its link level header) in ASCII.  Handy for capturing web pages. |
| -S   | Print absolute, rather than relative, TCP sequence numbers. |
| -s   | Snarf snaplen bytes of data from each packet rather than the default of 262144 bytes.  Packets truncated because of a limited snapshot are in‐dicated in the output with ```[|proto]```, where proto is the name of the protocol level at which the truncation has occurred. |
| -xx  | When parsing and printing, in addition to printing the headers of each packet, print the data of each packet, including its link level header, in hex.
| -XX  | When parsing and printing, in addition to printing the headers of each packet, print the data of each packet, including its link level header, in hex and ASCII.
| -v   | When parsing and printing, produce (slightly more) verbose output.  For example, the time to live, identification, total length and options in an IP packet are printed.  Also enables additional packet integrity checks such as verifying the IP and ICMP header checksum. |
| -vv  | Even more verbose output.  For example, additional fields are printed from NFS reply packets, and SMB packets are fully decoded. |
| -vvv | Even more verbose output.  For example, telnet SB ... SE options are printed in full.  With -X Telnet options are printed in hex as well. |
