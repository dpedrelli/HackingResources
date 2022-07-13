# Install
### [Linux](https://bloodhound.readthedocs.io/en/latest/installation/linux.html)
##### Install Java
```bash
echo "deb http://httpredir.debian.org/debian stretch-backports main" | sudo tee -a /etc/apt/sources.list.d/stretch-backports.list
sudo apt-get update
```
##### Install neo4j
```bash
wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
echo 'deb https://debian.neo4j.com stable 4.0' > /etc/apt/sources.list.d/neo4j.list
sudo apt-get update

sudo apt-get install apt-transport-https
sudo apt-get install neo4j

sudo systemctl stop neo4j

cd /usr/bin
./neo4j console
```

# Collectors
### [AzureHound](https://bloodhound.readthedocs.io/en/latest/data-collection/azurehound.html)
### [BloodHound.py](https://github.com/fox-it/BloodHound.py)
```bash
bloodhound-python -u [Username] -p [Password] -dc [DC Host FQDN] --disable-autogc -d [Domain FQDN] -c all
```
### [SharpHound](https://bloodhound.readthedocs.io/en/latest/data-collection/sharphound.html)

# Referecnes
##### [Github](https://github.com/BloodHoundAD/BloodHound)