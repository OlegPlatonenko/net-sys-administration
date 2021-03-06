#!/usr/bin/env python

import getpass
import sys
import telnetlib

#HOST = raw_input("Enter IP address in format X.X.X.X ")
HOST = "10.0.0.1"
print(HOST)
#AS = raw_input("Enter AS number: ")
user = raw_input("Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("int loop 0\n")
tn.write("ip addr 2.2.2.2 255.255.255.255\n")
tn.write("no shut")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
