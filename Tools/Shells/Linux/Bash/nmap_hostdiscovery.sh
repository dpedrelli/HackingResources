#!/bin/bash

if [ $# -lt 1 ]; then
	echo -n "Please enter the interface name: "
	read interface
else	
	interface=$1
fi

subnet=$(ip -4 -o addr show $interface | awk '{print $4}')
ip=$(ip -4 -o addr show $interface | awk '{print $4}' | cut -d "/" -f 1)

echo "sudo nmap -sn -g 53 --data-length 56 $subnet --ttl 2 --randomize-hosts --reason --exclude $ip -oA LanDefaultPing"
sudo nmap -sn -g 53 --data-length 56 $subnet --ttl 2 --randomize-hosts --reason --exclude $ip -oA LanDefaultPing