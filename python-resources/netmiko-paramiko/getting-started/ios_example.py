#ConnectHandler
from netmiko import Netmiko
from getpass import getpass
# x = your host
# y = you username
# Getpass takes care of  of pw prompt
my_device = {
'host': x,
'username': y,
'password': getpass(),
'device_type':'cisco_ios'
}

my_dist_device = {
'host': x1,
'username': y,
'password': getpass(),
'device_type':'cisco_ios'
}
for device in (my_device, my_dist_device):
    net_conn = Netmiko(**device)
    output = net_conn.send_command("show ip arp")
    print(output)

net_conn = Netmiko(**my_device)
print(net_conn.find_prompt())
print(net_conn.find_prompt())
output = net_conn.send_command("show arp",expect_string=r"#")
print(output)
net_connect.disconnect()
