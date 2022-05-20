# Run with GUI
```bash
sudo ettercap -G
```

# Establish MitM
### Establish MitM Between Two Hosts, with ARP Poisoning, in GUI
1) [Run ettercap](#Run-with-GUI).
2) Select type of sniffing and interface.
   * Menu -> Sniff -> Unified sniffing <Ctrl + U>
   * Select Interface
3) Select hosts.
   * Menu -> Hosts -> Scan for hosts <Ctrl + S>
   * Menu -> Hosts -> Hosts list <Ctrl + H>
   * Select Victim A and Click Add To Target 1
   * Select Victim B and Click Add To Target 2
4) Start attack.
   * Menu -> Mitm -> ARP poisoning
   * Enable Sniff remote connections
   * Click OK
5) Monitor captured packets.
   * Menu -> View -> Connections

# Intercept SSL
1) Send Fake SSL Certificate to Victim
2) Edit /etc/ettercap/etter.conf
   * Change ec_uid = 65534 to ec_uid = 0
   * Change ec_gid = 65534 to ec_gid = 0
   * Uncomment redir_command_on and redir_command_off lines, under # if you use iptables (the appropriate section may vary by OS)
   * [Establish MitM](#Establish-MitM) and Ettercap will the fake SSL certficate to the victim.
   * The victim will receive a warning that the certificate is invalid.