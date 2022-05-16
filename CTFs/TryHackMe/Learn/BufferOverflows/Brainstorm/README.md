# Try Hack Me - [Brainstorm](https://tryhackme.com/room/brainstorm)
##### Reverse engineer a chat program and write a script to exploit a Windows machine.

## Task 1 - Deploy Machine and Scan Network 

Deploy the machine and scan the network to start enumeration!

Please note that this machine does not respond to ping (ICMP) and may take a few minutes to boot up.
```
Deploy the machine
> No answer needed
```

```
How many ports are open?
> 6
```

## Task 2 - Accessing Files 

Let's continue with the enumeration!
```
What is the name of the exe file you found?
> chatserver.exe
```

## Task 3 - Access 

After enumeration, you now must have noticed that the service interacting on the strange port is some how related to the files you found! Is there anyway you can exploit that strange service to gain access to the system?

It is worth using a Python script to try out different payloads to gain access! You can even use the files to locally try the exploit.

If you've not done buffer overflows before, check [this](https://tryhackme.com/room/bof1) room out!
```
Read the description.
> No answer needed
```

```
After testing for overflow, by entering a large number of characters, determine the EIP offset.
> No answer needed
```

```
Now you know that you can overflow a buffer and potentially control execution, you need to find a function where ASLR/DEP is not enabled. Why not check the DLL file.
> No answer needed
```

```
Since this would work, you can try generate some shellcode - use msfvenom to generate shellcode for windows.
> No answer needed
```

```
After gaining access, what is the content of the root.txt file?
> 5b1001de5a44eca47eee71e7942a8f8a
```

## Additional Resources