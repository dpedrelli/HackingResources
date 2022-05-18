##### Basic Query
```bash
fierce -dns <TargetDomain.com>
```

##### Specify DNS Server
```bash
fierce -dns <TargetDomain.com> -dnsserver <NameServerToQuery>
```

##### Brute Force
```bash
fierce -dns <TargetDomain.com> -f <Hosts.txt>

fierce -dns <TargetDomain.com> -f /usr/share/wordlists/SecLists/Discovery/DNS/fierce-hostlist.txt
```