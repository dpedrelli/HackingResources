#!/usr/bin/env python3

import argparse;

parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, dest="file", required=True, help="Name of gnmap file to parse.")
parser.add_argument("-o", type=str, dest="options", required=False, help="Options for Nmap port scan.")
# parser.add_argument("-s", type=bool, action="store_true", dest="sudo", required=False, help="Run as sudo.")
args = parser.parse_args()
print(args)

def parse_input():
	with open(args.file, "r") as f:
		lines = f.readlines()
		for line in lines:
			host = ""
			ports = ""
			if line.__contains__("Ports: "):
				elements = line.split()
				host = elements[1]
				for i in range(4, len(elements)):
					element = elements[i]
					if len(ports) > 0:
						ports = ports + ","
					port = elements[i].split("/")
					ports = ports + port[0]
				print("sudo nmap " + args.options + " " + host + " -p" + ports)


if __name__ == "__main__":
	parse_input()
