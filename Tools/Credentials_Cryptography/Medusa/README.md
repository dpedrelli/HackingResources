**_Note:_** Medusa may fail, with valid credentials, if it is unable to understand the login prompt, and inputs the credentials incorrectly (at least for Telnet).

# Brute Force
```bash
medusa -h <Target Host> -M <Protocol> -U <Username List> -P <Password List>
```

# Grep Results
```bash
medusa -h <Target Host> -M <Protocol> -U <Username List> -P <Password List> | grep "ACCOUNT FOUND"
```

# References
##### [Medusa Parallel Network Login Auditor :: Feature Comparison](http://foofus.net/goons/jmk/medusa/medusa-compare.html)

##### [Medusa Parallel Network Login Auditor](http://foofus.net/goons/jmk/medusa/medusa.html)