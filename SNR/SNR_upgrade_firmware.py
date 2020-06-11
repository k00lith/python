import getpass
import sys
from netmiko import ConnectHandler


command = 'show ip interface brief'
user = 'admin'
password = 'admin'
#enable_pass = getpass.getpass(prompt='Enter enable password: ')

devices_ip = ['192.168.70.228']

for ip in devices_ip:
    print('connection to device {}'.format(ip))
    device_params = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': user,
        'password': password,
        #'secret': enable_pass
    }

    with ConnectHandler(**device_params) as ssh:
        #ssh.enable()

        result = ssh.send_command(command)
        print(result)
