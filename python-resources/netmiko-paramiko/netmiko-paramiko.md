# Paramiko & Netmiko

Paramiko is the standard Python SSH Library

Netmiko is a multi-vendor networking libraray based on Paramiko

* pExpect
* Trigger

## Netmiko Vendor Support

![List of Vendors](https://github.com/gil-ryan/grs-python-private/blob/master/python-resources/netmiko-paramiko/2018-support.PNG)

## Device Types

The easiest way to find out device types would be entering an improper 'device_type', Netmiko's output should provide you a list of supported devices.

send.command looks for trailing responses. it automatically strips the echos. It tries to give the direct command response.