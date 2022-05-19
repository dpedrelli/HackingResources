# Install
##### Install snmp-mibs-downloads.  Comment out the fourth line of /etc/snmp/snmp.conf #mibs:

# Enumerate
```bash
# Specify version 2c
snmpwalk -v 2c <Target Host> -c public

# List only the software installed on the machine
snmpwalk -v 1 -c public <Target Host> hrSWInstalledName
```

# References
[SNMPWalk](http://www.net-snmp.org/docs/man/snmpwalk.html)

[Net-SNMP](http://www.net-snmp.org/)