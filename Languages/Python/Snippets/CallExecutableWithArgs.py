#!/usr/bin/env python3

import subprocess

# subprocess documentation https://docs.python.org/3.2/library/subprocess.html
# 3.5 subprocess documentation https://docs.python.org/3.5/library/subprocess.html

# Waits for command to complete, then returns the return code.
# subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
# Waits for command to complete. If the return code was zero then returns, otherwise raises CalledProcessError. The CalledProcessError object will have the return code in the return code.
# subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False)

subprocess.check_call([r"C:\Path\Program.exe", "comma", "separated", "arguments"])