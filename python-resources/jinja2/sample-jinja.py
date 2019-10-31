#!/usr/bin/env/python
from __future__ import print_function, unicode_literals
import jinja2 

# initialize empty dictionary
bgp_vars = {}

bgp_template = '''
feature bgp
router bgp 10
    address-family ipv4 unicast
        network 10.10.200.0/24
    neighbor 10.255.255.2 remote-as 20
        update-source loopback1
        ebgp-multihop 2
        address-family ipv4 unicast
'''
t = jinja2.Template(bgp_template)
print(t.render(bgp_vars))
