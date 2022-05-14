
##### Continue a command across multiple lines.
```bash
\
```

##### Find printable characters in files
```bash
strings
```

##### Identify shells on Linux
```bash
cat /etc/shells
```

##### Dump passwords
```bash
hashdump
```

##### Check for sudo permission
```bash
sudo -l
```

##### Get IP Address
```bash
ip a s tun0
```

##### Change Terminal Prompt
```bash
export PS1='$ '
```

##### Display directories in tree format
```bash
tree
```

##### Recover Files in PCAP
```bash
# Extract files based on IP addressing conversation.
tcpflow -r file.pcap
```

##### Search binary images for embedded files and executable code. - binwalk
```bash
binwalk -e file.ext
```

##### Recover files using their headers, footers, and data structures. - foremost
```bash
foremost file.ext
```

##### Shift letters.
```bash
pax$ echo 'hello there' | tr '[a-z]' '[n-za-m]' | tr '[a-z]' '[n-za-m]'
```

##### Get unique lines from text file.
```bash
sort file.txt | uniq -i | tee file.txt.uniq
```

##### Get SUID/SGID binaries
```bash
find / -perm -u=s -type f 2>/dev/null
find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
find / -type f -perm -04000 -ls 2>/dev/null
```

##### Get Binary Capabilities
```bash
# Find binaries that may have escalated privileges that the user does not have.
getcap -r / 2>/dev/null
```