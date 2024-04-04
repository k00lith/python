#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import getpass
import sys
from netmiko import ConnectHandler




commands = ['conf t',
            'interf GigabitEthernet 1/0/1',
            'shutdown',
            'end']
user = 'admin'
password = '******'
devices_ip = ['10.187.131.32']


for ip in devices_ip:
    print('connection to device {}'.format(ip))
    device_params = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': user,
        'password': password,
        'secret': password,
    }

    with ConnectHandler(**device_params) as ssh:
        ssh.enable()
        ssh.send_config_set(commands)
        ssh.disconnect()
