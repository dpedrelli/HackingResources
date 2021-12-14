##### Get Windows Version
```bash
systeminfo | findstr /b /c:"OS Name" /c:"OS Version"
```

##### Get Installed Services
```bash
wmic service list
```