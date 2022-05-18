# Host Discovery

# ICMP Ping Host
```bash
sudo hping3 -1 <Host>
```

# ICMP Ping Range
```bash
sudo hping3 -1 192.16.1.x --rand-dest
```

# Timestamp ICMP Ping
```bash
sudo hping3 --icmp-ts -1 <Host>
```

# UDP Ping
```bash
# Default port is zero.  
sudo hping3 -2 <Host>
# Capture packets in Wireshark.  "Port Unreachable" means host is live.
```

# TCP SYN Ping
```bash
# Default port is zero.  
sudo hping3 -S <Host>
# If command line returns flags=RA, host is live.

# Specify port.
sudo hping3 -S <Host> -p <Port #>
```

# Specify Flags
```bash
# FIN
sudo hping3 -F <Host>

# URG
sudo hping3 -U <Host>

# XMAS
sudo hping3 -X <Host>

# YMAS
sudo hping3 -Y <Host>

# Specify Multiple Flags (XMAS)
sudo hping3 -F -P -U <Host>
```

# Specify Ping count
```bash
sudo hping3 -1 <Host> -c <# of Pings>
```

# Specify Interface
```bash
sudo hping3 -1 <Host> -I <Interface Name>
```

# Verbose
```bash
sudo hping3 -1 <Host> -V
```
