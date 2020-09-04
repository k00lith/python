#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import paramiko
from scp import SCPClient
from datetime import datetime


def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client




if __name__ == '__main__':

    dev_ip = ['10.10.1.1',
              '10.10.2.1',
              '10.10.3.1',
              '10.10.4.1',
              '10.10.5.1',
              '10.10.6.1',
              '10.10.7.1']
    
    today = datetime.now()
    os.mkdir("/var/local/zip_config_" + today.strftime('%Y%m%d'))
    for ip in dev_ip:
        ssh = createSSHClient(ip, 22, 'admin', 'passw00rd')
        scp = SCPClient(ssh.get_transport())
        scp.get('/config/juniper.conf.gz', "/var/local/zip_config_" + today.strftime('%Y%m%d') + "/" + ip + "_juniper.conf.gz")
