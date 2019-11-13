# Network Class 
# network-class.py

import netmiko

class Network(object):
    def __init__(self, ip_addr):
            self.ip_addr = ip_addr
            self.hostname = None
            