# Create a tunnel
```bash
# Send local 8080 traffic to host 172.17.0.2
ssh -L 8080:172.17.0.2:8080 aubreanna@10.10.164.248
```

# Connect with RSA Key
```bash
ssh user@host -i id_rsa
```