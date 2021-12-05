#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass
import sys
from netmiko import ConnectHandler


command = 'request system autorecovery state save'
user = 'admin'
password = 'passwadmin'
#enable_pass = getpass.getpass(prompt='Enter enable password: ')

devices_ip = ['10.0.1.1',
              '10.0.2.1',
              '10.0.3.1',
              '10.0.4.1',
              '10.0.5.1',
              '10.0.6.1',
              '10.0.7.1']


for ip in devices_ip:
    print('connection to device {}'.format(ip))
    device_params = {
        'device_type': 'juniper_junos',
        'ip': ip,
        'username': user,
        'password': password,
        #'secret': enable_pass
    }

    with ConnectHandler(**device_params) as ssh:
        #ssh.enable()
        #result = ssh.send_command(command)
        #print(result)
        ssh.send_command(command)
        #print('DONE!')
        ssh.disconnect()
