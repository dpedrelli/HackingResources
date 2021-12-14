##### List Shares
```bash
showmount -e <IP Address>
```

##### Mount Share
```bash
# Make directory and mount share to that directory.
mkdir tmp1
mount <IP Address>:/<Share Name> tmp1
```