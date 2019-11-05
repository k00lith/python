#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from sys import argv
import os
import re
import glob


path = input('Insert path where logs are ( for example: /var/logs/ ): ')
target = input('Insert security policy name ( for example: default-policy-1 ): ')

#file = open('/home/python/Desktop/test_log.txt', 'r')
#regex = r'.+ session created (\d+\.\d+\.\d+\.\d+)/(\d+)->(\d+\.\d+\.\d+\.\d+)/(\d+) .+ None None (\d+)'
regex = r'.+ (\d+\.\d+\.\d+\.\d+)/(\d+)->(\d+\.\d+\.\d+\.\d+)/(\d+) None None (\d+) .+'
pre_list_ports = []
res_list_ports = []
logs = os.listdir(path)

for file in logs:
    file_path = path+file
    with open(file_path, 'r') as f:
        for line in f:
            if target in line:
                check = 0
                match = re.match(regex, line)
                port = ''
                prot = ''
                if match:
                    port = match.group(4)
                    prot = match.group(5)
                if prot == str(6):
                    prot = 'TCP'
                elif prot == str(17):
                    prot = 'UDP'
                elif prot == str(1):
                    prot = 'icmp'
                else:
                    prot = ''
                    
                port_num = prot+'-'+port
                pre_list_ports.append(port_num)
                if port_num not in res_list_ports:
                    res_list_ports.append(port_num)

result = ', '.join(res_list_ports)
print('Ports in use: ')
print('='*39)
print(result)
print('='*39)
