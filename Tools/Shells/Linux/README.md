# Network Commands
##### Get IP address.
```bash
ip a

# Show specific interface.
ip a show eth0

ifconfig
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