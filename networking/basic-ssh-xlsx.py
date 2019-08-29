Write to a spreadsheet
import paramiko
import netmiko
import xlsxwriter

from datetime import datetime
from netmiko import ConnectHandler
from paramiko.ssh_exception import SSHException 
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException

# Create workbook & add sheet
workbook = xlsxwriter.Workbook('config.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': 1})

# Write Headers 
worksheet.write('A1', 'IP', bold)
worksheet.write('B1', 'Hostname', bold)
worksheet.write('C1', 'Access List', bold)

row = 1
col = 0

ip =  open("ipaddress.txt", "r").read()
ip = ip.split("\n")

print(ip)
for x in ip:
	try:
		net_connect = ConnectHandler(device_type='cisco_ios', ip=x, username="[]", password='[]',global_delay_factor=.5)
		print("\n############| Connected to host:  " + x + "  |############")
		print("\n", x)
		worksheet.write_string(row, col, x)
		col += 1
		#
		sh2 = net_connect.send_command("show run | i hostname")
		print(sh2)
		worksheet.write_string  (row, col,  sh2)      
		col += 1
		#
		sh3 = net_connect.send_command("show access-list")
		print(sh3)
		worksheet.write_string  (row, col,  sh3)        
		col += 1		     
		#
		net_connect.disconnect()
		row += 1
		#
		col = 0
		print("\n############| Disconnected from host: " + x + " |############")
	except (EOFError, SSHException, NetMikoTimeoutException, NetMikoAuthenticationException):
		print('Exception error: ' + x )
		row +=1
		col = 0
workbook.close()