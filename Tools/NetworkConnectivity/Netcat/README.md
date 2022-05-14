# Transfer Files
##### On Target Machine
```bash
nc -l -p <Port Number> > <Filename>
```
##### On Attack Machine
```bash
nc -w 3 <Target IP Address> -p <Port Number> < <Filename>
```