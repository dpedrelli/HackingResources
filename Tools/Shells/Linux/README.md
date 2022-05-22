# Network Commands
##### Get IP address
```bash
ip a

# Show specific interface.
ip a show eth0

ifconfig

ip addr
```

##### Identify Reachable Networks
```bash
ip route show dev <Interface Name>
```

##### Check Routing Table
```bash
ip route

netstat -rn

route -n
```

##### Create a Route
```bash
ip route add <network_ip>/<cidr> via <gateway_ip>

# Over specific interface.
ip route add <network_ip>/<cidr> via <gateway_ip> dev <network_card_name>
```

##### Masquerade IP
```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -s <Network>/<Subnet> -o <Interface Name> -j MASQUERADE
iptables -t nat -A POSTROUTING -s 10.100.13.0/255.255.255.0 -o eth1 -j MASQUERADE
```

##### Interactive Sudo Shell
```bash
sudo -i
```

##### Enable IP Forwarding
```bash
sudo -i
echo 1 > /proc/sys/net/ipv4/ip_forward
```

##### Setup Port Redirection Using Tables
```bash
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-ports 8080

```

##### Find
```bash
find / -name <Name To Find> 2>/dev/null
```

# References
[bash(1) — Linux manual page](https://www.man7.org/linux/man-pages/man1/bash.1.html)

[sh(1p) — Linux manual page](https://man7.org/linux/man-pages/man1/sh.1p.html)