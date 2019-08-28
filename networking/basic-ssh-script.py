import paramiko
import netmiko
import xlsxwriter
from netmiko import ConnectHandler
from paramiko.ssh_exception import SSHException 
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException

workbook = xlsxwriter.Workbook('config.xlsx')
worksheet = workbook.add_worksheet()
ip =  open("ipaddress.txt", "r").read()
ip = ip.split("\n")
row = 1
col = 0

print (ip)
for x in ip:
	try:
		net_connect = ConnectHandler(device_type='cisco_ios', ip=x, username="[OBFUSCATED]", password='[OBFUSCATED]',global_delay_factor=.5)
		#
		print("\n", x)
		worksheet.write_string(row, col, x)
		col += 1
		#
		sh1 = net_connect.send_command("show run | i hostname")
		worksheet.write_string(row, col, sh1)s
		col += 1
		#
		sh1 = net_connect.send_command("show run | i ip tacacs source-interface")
		worksheet.write_string(row, col, sh1)
		col += 1
		net_connect.disconnect()
		row += 1
		col = 0 
	except(EOFError, SSHException, NetMikoTimeoutException, NetMikoAuthenticationException):
		print('Exception error: ' + x )
workbook.close()
