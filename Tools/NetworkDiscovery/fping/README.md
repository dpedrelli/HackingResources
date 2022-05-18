# Host Discovery

##### ICMP Ping, Report Status on All Hosts
```bash
fping -A <Host>
```

##### ICMP Ping, Only Show Live Hosts
```bash
fping -a <Host>
```

##### Specify Number of Retries
```bash
fping -a <Host> -r <# of Retries>
```

##### Show elapsed time on return packets
```bash
fping -a <Host> -e
```

##### Ping IP Range or CIDR
```bash
fping -a -g 192.168.1.0/24 -r 0 -q -e
```

##### Quiet
```bash
fping -a <Host> -q
```