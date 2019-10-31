from netmiko import Netmiko
from getpass import getpass
x = input("Enter a host: ")
y = input("Enter a username: ")
my_device = {
'host': x,
'username': y,
'password': getpass(),
'device_type': 'cisco_ios',
}
net_conn = Netmiko(**my_device)
output = net_conn.send_command("show arp", expect_string=r'#')
print(output)