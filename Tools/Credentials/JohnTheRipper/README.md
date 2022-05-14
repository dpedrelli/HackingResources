# Unshadow for Linux Hashes Cracking
```bash
unshadow passwd shadow > shadow.john
```

# Crack Linux Hashes
```bash
john shadow.john --wordlist=<Wordlist>
```

# Show Cracked Passwords
```bash
john --show shadow.john
```

# Crack a Zip file
```bash
zip2john file.zip > hash.txt
john --format=zip hash.txt
```

# References
[John The Ripper](https://www.openwall.com/john/)
