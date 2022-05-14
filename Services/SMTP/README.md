# Enumerate
##### With nmap
```bash
# Enumerate verbs.
nmap --script smtp-commands <IP Address> -p 25
```

##### With telnet (verbs & users)
```bash
telnet <IP Address> 25

# Enumerate verbs.
help

# Enumerate users with RCPT TO.
HELO <Domain>
<E-Mail address>
# Looking for "Status Code 250," "Recipient ok"

# Enumerate users with EXPN.
EXPN <Username> # Username, not E-Mail address.
# Looking for "Status Code 250 2.1.5"

# Enumerate users with VRFY.
VRFY <Username> # Username, not E-Mail address.
# Looking for "Status Code 250 2.1.5"
```

##### With netcat (verbs)
```bash
nc <IP Address> 25
help
```

##### [With smtp-user-enum (users)](../../Tools/SMTP/smtp-user-enum/README.md)

# References
[VRFY and EXPN verbs](https://cr.yp.to/smtp/vrfy.html)

[MAIL, RCPT, and DATA verbs](https://cr.yp.to/smtp/mail.html)

[smtp-user-enum](https://pentestmonkey.net/tools/user-enumeration/smtp-user-enum)