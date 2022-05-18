# Query Name Servers
```bash
# One liner
nslookup -query=NS <DomainToQuery.com>


# Enter interactive shell
nslookup
# Optionally set DNS server to query
server <NameServerToQuery>
# Set query type
set q=NS
<DomainToQuery.com>
```

# Query Mail Servers
```bash
# One liner
nslookup -query=MX <DomainToQuery.com>


# Enter interactive shell
nslookup
# Optionally set DNS server to query
server <NameServerToQuery>
# Set query type
set q=MX
<DomainToQuery.com>
```

# Output All Available DNS Records
```bash
# One liner
nslookup -query=ANY <DomainToQuery.com>


# Enter interactive shell
nslookup
# Optionally set DNS server to query
server <NameServerToQuery>
# Set query type
set q=ANY
<DomainToQuery.com>
```

# Query and Host (A)
```bash
# One liner
nslookup -query=A <HostToQuery.com>
```

# Query and Alias (CNAME)
```bash
# One liner
nslookup -query=CNAME <HostToQuery.com>
```

# Get IP Address of Server
```bash
# Enter interactive shell
nslookup
# Optionally set DNS server to query
server <NameServerToQuery>
<ServerToQuery.com>
```