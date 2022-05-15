# Network Commands
##### Get IP address
```bash
ip a

# Show specific interface.
ip a show eth0

ifconfig

ip addr
```

##### Check Routing Table.
```bash
ip route

netstat -rn

route -n
```

##### Create a Route.
```bash
ip route add <network_ip>/<cidr> via <gateway_ip>

# Over specific interface.
ip route add <network_ip>/<cidr> via <gateway_ip> dev <network_card_name>
```

# References
[bash(1) — Linux manual page](https://www.man7.org/linux/man-pages/man1/bash.1.html)

[sh(1p) — Linux manual page](https://man7.org/linux/man-pages/man1/sh.1p.html)