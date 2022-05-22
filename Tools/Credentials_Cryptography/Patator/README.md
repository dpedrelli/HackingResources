**_Note:_** Documentation is found in source code /usr/bin/patator

##### Get Help
```bash
# Module help
patator <Module_Name> --help
patator ftp_login --help

# Short help
patator <Module_Name>
patator ftp_login
```

##### General Syntax
```bash
# Note that all module options are fuzzable.
patator <Module_Name> host=<Target Host> user=FILE0 password=FILE1 0=<Username List> 1=<Password List> -x <Filter>
```

##### FTP
```bash
patator ftp_login host=<Target Host> user=FILE0 password=FILE1 0=<Username List> 1=<Password List> -x ignore:mesg="Login incorrect."
```

##### SSH
```bash
# Attempt to login with wrong credentials, to determine failed login message returned.
patator ssh_login host=<Target Host> user="user" password="password"
# Assume mesg = Authentication failed.

patator ssh_login host=<Target Host> user=FILE0 password=FILE1 0=<Username List> 1=<Password List> -x ignore:mesg="Authentication failed."
```

##### Telnet
```bash
# From telnet_login --help
patator telnet_login host=<Target Host> inputs="FILE0\nFILE1" 0=<Username List> 1=<Password List> persistent=0 prompt_re="Username:|Password:" -x ignore:egrep="Login incorrect.+Username:"


patator telnet_login host=<Target Host> inputs="FILE0\nFILE1\n" 0=<Username List> 1=<Password List>
# Check returned messages (mesg).  Services like FTP, SSH, Telnet, and others tend to return the date upon successful login.
# Copy the mesg and ignore every message that does not match.
patator telnet_login host=<Target Host> inputs="FILE0\nFILE1\n" 0=<Username List> 1=<Password List> -x ignore:mesg!=<Complete mesg received in previous command, including spaces>
```