# [With Angry IP Scanner](../../Tools/NetworkDiscovery/AngryIPScanner/README.md)

# [With hping](../../Tools/NetworkDiscovery/hping/README.md#Port-Scan)

# [With Masscan](../../Tools/NetworkDiscovery/Masscan/README.md)

# [With Nmap](../../Tools/NetworkDiscovery/Nmap/README.md#Port-Scan)

# [With RustScan](../../Tools/NetworkDiscovery/RustScan/README.md#Scan)

# Zombie Scan using both hping and Nmap
```bash
# Hping tracks IP ID increment.
sudo hping3 -S -r <Zombie Host> -p 135

# Nmap performs scan.
sudo nmap -S <Zombie Host> <Target Host> -p <Port #> -Pn -n -e <Interface Name> --disable-arp-ping

1) Start hping tracking IP ID.
2) Run scan with nmap.
3) Check hping for incrementing IP ID, to confirm that port is open.
```