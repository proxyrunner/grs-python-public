#ConnectHandler
from netmiko import Netmiko
from getpass import getpass
# x = your host
# y = you username
# Getpass takes care of  of pw prompt
x = input("Enter a host: ")
y = input("Enter a username: ")
my_device = {
'host': x,
'username': y,
'password': getpass(),
'device_type':'linux_ssh'
}
net_conn = Netmiko(**my_device)
print(net_conn.find_prompt())