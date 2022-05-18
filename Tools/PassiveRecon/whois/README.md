# whois

|                      |                                              |
|----------------------|----------------------------------------------|
| -h HOST, --host HOST | connect to server HOST                       |
| -p PORT, --port PORT | connect to PORT                              |
| -I                   | query whois.iana.org and follow its referral |
| -H                   | hide legal disclaimers                       |

These flags are supported by whois.ripe.net and some RIPE-like servers:

|                            |                                                                            |
|----------------------------|----------------------------------------------------------------------------|
| -l                         | find the one level less specific match                                     |
| -L                         | find all levels less specific matches                                      |
| -m                         | find all one level more specific matches                                   |
| -M                         | find all levels of more specific matches                                   |
| -c                         | find the smallest match containing a mnt-irt attribute                     |
| -x                         | exact match                                                                |
| -b                         | return brief IP address ranges with abuse contact                          |
| -B                         | turn off object filtering (show email addresses)                           |
| -G                         | turn off grouping of associated objects                                    |
| -d                         | return DNS reverse delegation objects too                                  |
| -i ATTR[,ATTR]...          | do an inverse look-up for specified ATTRibutes                             |
| -T TYPE[,TYPE]...          | only look for objects of TYPE                                              |
| -K                         | only primary keys are returned                                             |
| -r                         | turn off recursive look-ups for contact information                        |
| -R                         | force to show local copy of the domain object even if it contains referral |
| -a                         | also search all the mirrored databases                                     |
| -s SOURCE[,SOURCE]...      | search the database mirrored from SOURCE                                   |
| -g SOURCE:FIRST-LAST       | find updates from SOURCE from serial FIRST to LAST                         |
| -t TYPE                    | request template for object of TYPE                                        |
| -v TYPE                    | request verbose template for object of TYPE                                |
| -q [version|sources|types] | query specified server info                                             |

### Specify Server to Query
```bash
whois -h whois.godaddy.com <targetdomain.com>
```

### Output to File
```bash
whois <targetdomain.com> > whois.txt
```