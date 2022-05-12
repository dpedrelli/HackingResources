# Create VPN tunnel to victim, to bypass firewalls
##### Arch Linux
```bash
yaourt -S vpnpivot-git
```

##### Other Linux
```bash
git clone https://github.com/0x36/VPNPivot.git
cd VPNPivot

./autogen.sh
./configure
make && make install
```

# References
[VPNPivot](https://github.com/0x36/VPNPivot)