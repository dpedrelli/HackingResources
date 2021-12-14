# [RustScan](https://github.com/RustScan/RustScan)

##### [Installation Guide](https://github.com/RustScan/RustScan/wiki/Installation-Guide)

##### Notes
When scanning all ports, I received a false negative, multiple times, in TryHackMe's Advent Of Cyber 3, Day 11.  
Twice, it missed 1433.  
Once, it missed 3389.

##### Install with Docker
```bash
sudo docker pull rustscan/rustscan:<version>
```

##### Run with Docker
```bash
sudo docker run -it --rm --name rustscan rustscan/rustscan:<version> <rustscan arguments here> <ip address to scan>
```

##### Set Alias
```bash
alias rustscan='sudo docker run -it --rm --name rustscan rustscan/rustscan:<version>'
alias rustscan='sudo docker run -it --rm --name rustscan rustscan/rustscan:2.0.1'
```

##### Scan All Ports
```bash
rustscan -a <IP Address> --range 1-65535 --scan-order "Random" -b 200 -t 2000
```

##### Scan All Ports and Pass to Nmap with Nmap Arguments
```bash
rustscan -a <IP Address> --range 1-65535 --scan-order "Random" -- -sC -A
```