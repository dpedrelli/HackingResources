# Verify SMTP Verbs and User
```bash
telnet <SMTP Host> 25
Trying <SMTP Host>...
Connected to <SMTP Host>.
Escape character is '^]'.
220 myhost ESMTP Sendmail 8.9.3
HELO
501 HELO requires domain address
HELO x
250 myhost Hello [<Attack IP>], pleased to meet you
VRFY root # Username, not E-Mail address.
250 Super-User <root@myhost>
VRFY blah # Username, not E-Mail address.
550 blah... User unknown
EXPN root # Username, not E-Mail address.
502 5.5.2 Error: command not recognized
```