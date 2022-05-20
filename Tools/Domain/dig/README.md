# Basic Query
```bash
dig <DomainToQuery.com>
```

# Query Record Type
```bash
# Query Name Servers
dig <DomainToQuery.com> NS

# Query Mail Servers
dig <DomainToQuery.com> MX

# Query Host
dig <HostToQuery.com> A
```

# Restrict Output to Answer Only
```bash
dig <DomainToQuery.com> NS +noall +answer +nocmd
```

# Reverse Lookup
```bash
dig @<DnsServerToQuery> -x <IP Address To Resolve> +nocookie
```

# Zone Transfer
```bash
# For zone transfer to work, must specify misconfigured DNS server.
dig @<DnsServerToQuery> <DomainToQuery.com> -t AXFR +nocookie
```

# Reverse Lookup to Get Domains
```bash
# For zone transfer to work, must specify misconfigured DNS server.
dig axfr -x <192.168> @<DnsServerToQuery>
```