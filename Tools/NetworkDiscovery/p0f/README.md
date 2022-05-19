# p0f3
##### Run
```bash
./p0f -i <Interface Name>
```

# p0f3plus
##### Install
```bash
pip install -r requirements.txt
```

##### Run Against PCAP and Output to Classic Print
```bash
python3 ./pcaprint.py -c capture.pcapng -p
```

##### Run Against PCAP and Output to XML
```bash
python3 ./pcaprint.py -c capture.pcapng -o test.xml
```

##### Call From Python
```bash
from p0f3p.core.p0f3p import *

a = p0f3p()
packet = ''
pktsign = a.pkt2sig(Ether(packet))
matches = a.matchsig(pktsign)
```

# References
##### [p0f3](https://lcamtuf.coredump.cx/p0f3/)
##### [p0f3 ReadMe](https://lcamtuf.coredump.cx/p0f3/README)

##### [p0f3plus](https://github.com/FlUxIuS/p0f3plus)