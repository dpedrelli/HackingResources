# Generate SSL Certificate
```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

# Start SSL Listener
```bash
openssl s_server -quiet -key key.pem -cert cert.pem -port 443_
```