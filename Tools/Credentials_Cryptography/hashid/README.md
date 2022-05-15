| Parameter              | Description                                         |
|------------------------|-----------------------------------------------------|
| INPUT                  | input to analyze (default: STDIN)                   |
| -e, –extended          | list all hash algorithms including salted passwords |
| -m, –mode              | show corresponding hashcat mode in output           |
| -j, –john              | show corresponding JohnTheRipper format in output   |
| -o FILE, –outfile FILE | write output to file (default: STDOUT)              |
| –help                  | show help message and exit                          |
| –version               | show program’s version number and exit              |

# Install
```bash
pip install hashid
pip install --upgrade hashid
pip uninstall hashid
```

# Install from Github
```bash
sudo apt-get install python3 git
git clone https://github.com/psypanda/hashid.git
cd hashid
sudo install -g 0 -o 0 -m 0644 doc/man/hashid.7 /usr/share/man/man7/
sudo gzip /usr/share/man/man7/hashid.7
```

# Identify Hash Type.
```bash
./hashid.py [-h] [-e] [-m] [-j] [-o FILE] [--version] INPUT

hashid '$2y$10$0veO/JSFh4389Lluc4Xya.dfy2MF.bZhz0jVMw.V.d3p12kBtZutm'
```

# Examples from Developer
```bash
$ ./hashid.py '$P$8ohUJ.1sdFw09/bMaAQPTGDNi2BIUt1'
Analyzing '$P$8ohUJ.1sdFw09/bMaAQPTGDNi2BIUt1'
[+] Wordpress ≥ v2.6.2
[+] Joomla ≥ v2.5.18
[+] PHPass' Portable Hash

$ ./hashid.py -mj '$racf$*AAAAAAAA*3c44ee7f409c9a9b'
Analyzing '$racf$*AAAAAAAA*3c44ee7f409c9a9b'
[+] RACF [Hashcat Mode: 8500][JtR Format: racf]

$ ./hashid.py hashes.txt
--File 'hashes.txt'--
Analyzing '*85ADE5DDF71E348162894C71D73324C043838751'
[+] MySQL5.x
[+] MySQL4.1
Analyzing '$2a$08$VPzNKPAY60FsAbnq.c.h5.XTCZtC1z.j3hnlDFGImN9FcpfR1QnLq'
[+] Blowfish(OpenBSD)
[+] Woltlab Burning Board 4.x
[+] bcrypt
--End of file 'hashes.txt'--
```