SSH:
ssh public key file location - /etc/ssh/ssh_host_rsa_key.pub

APACHE2:
service apache2 status - Apache2 service status 

COMMON:
ls -lst - detailed list of items

1. SERVICES:
service --status-all - get status list

2. NETWORK:
if config -a - get list of network adapters
lshw -class network - ----"----
netstat -a - list of ports 

3. INSTALLERS
wget  -O /home/omio/Desktop/ "http://thecanadiantestbox.x10.mx/CC.zip" - download file from internet
tar xvzf file.tar.gz - unzip file

4. SETUP SSH
- sudo apt-get install openssh-server
- sudo ssh service status - must be running
- check port settings
- *sudo lsof -i | grep ssh*
- *netstat -l --numeric-ports | grep 22*