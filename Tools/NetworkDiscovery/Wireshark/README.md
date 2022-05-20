# Sniff ARP Spoof MitM
```bash
# Filter out ARP packets.
!arp

# Look for HTTP Authentication
!arp && http.authbasic
```