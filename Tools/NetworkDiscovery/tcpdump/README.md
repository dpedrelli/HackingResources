# Dump Traffic
```bash
sudo tcpdump -i <Interface Name> 
```

# Dump Traffic with Detail
```bash
sudo tcpdump -i <Interface Name> -xxAXXSs 0

sudo tcpdump -i <Interface Name> -vvvASs 0
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
