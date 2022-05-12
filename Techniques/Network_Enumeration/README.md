# Local Enumeration
##### List all interfaces
```bash
ifconfig -a
```

##### List network routes
```bash
route -n
```

##### Number of hops
```bash
tracert -n <IP Address>
```

##### DNS Information
```bash
cat /etc/resolv.conf
```

##### ARP Cache
```bash
arp -en
```

##### Connections
```bash
netstat -auntp

ss -twurp
```

##### Check for Open, Outgoing Ports
```bash
nmap -sT -p<ports> portquiz.net
# Avoid IDS and rate limiting on Portquiz.net
nmap -sT -p<ports> -T<lownumber> portquiz.net
```

# References
[netstat without netstat](https://staaldraad.github.io/2017/12/20/netstat-without-netstat/)

[portquiz.net](http://portquiz.net/)