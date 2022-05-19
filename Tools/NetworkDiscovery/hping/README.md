# Host Discovery
### ICMP Ping Host
```bash
sudo hping3 -1 <TargetHost>
```

### ICMP Ping Range
```bash
sudo hping3 -1 192.16.1.x --rand-dest
```

### Timestamp ICMP Ping
```bash
sudo hping3 --icmp-ts -1 <TargetHost>
```

### UDP Ping
```bash
# Default port is zero.  
sudo hping3 -2 <TargetHost>
# Capture packets in Wireshark.  "Port Unreachable" means host is live.
```

### TCP SYN Ping
```bash
# Default port is zero.  
hping3 -S <TargetHost>
# If command line returns flags=RA, host is live.

# Specify port.
hping3 -S <TargetHost> -p <Port #>
```

### Specify Flags
```bash
# FIN
sudo hping3 -F <TargetHost>

# URG
sudo hping3 -U <TargetHost>

# XMAS
sudo hping3 -X <TargetHost>

# YMAS
sudo hping3 -Y <TargetHost>

# Specify Multiple Flags (XMAS)
sudo hping3 -F -P -U <TargetHost>
```


# Port Scan

### TCP SYN Port Range
```bash
hping3 -S --scan <Port Range> <TargetHost>
hping3 -S --scan 1-1000 <TargetHost>
hping3 -S --scan 22,80,443,8080 <TargetHost>
hping3 -S --scan 1-1000,8888,known <TargetHost>
hping3 -S --scan all <TargetHost>
hping3 -S --scan known <TargetHost> # All ports listed in \etc\services
hping3 -S --scan '1-1024,!known' <TargetHost> # Exclude ports listed in \etc\services
# Must use quotes to negate ports.
# Returns table with listening ports and flags.
```

### UDP Scan
```bash
hping3 -2 --scan 1-1000 <TargetHost>
```

### Christmas Scan
```bash
# Non-responding ports should be open or filtered.
# Resonding ports are closed.

# Single port
sudo hping3 -F -P -U -p <Port #> <TargetHost>

# Port range
sudo hping3 -F -P -U --scan 1-1000 <TargetHost> -V
```

### NULL Scan
```bash
# Non-responding ports should be open or filtered.
# Resonding ports are closed.

sudo hping3 --scan 1-1000 <TargetHost>
```

# Idle / Zombie
### Verify Idle / Zombie Candidate
```bash
sudo hping3 -S -r -p <Port #> <TargetHost>
```

### Idle / Zombie Scan
```bash
sudo hping3 -a <ZombieHost> -S -p <Port #> <TargetHost>
```

# General Options

### Specify Ping count
```bash
sudo hping3 -1 <TargetHost> -c <# of Pings>
```

### Specify Interface
```bash
sudo hping3 -1 <TargetHost> -I <Interface Name>
```

### Verbose
```bash
sudo hping3 -1 <TargetHost> -V
```