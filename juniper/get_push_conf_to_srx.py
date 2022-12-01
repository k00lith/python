#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-


import os
import sys
import time
import getpass
import paramiko
from netmiko import ConnectHandler
from netmiko import juniper
from scp import SCPClient
from datetime import datetime


def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client




if __name__ == '__main__':

    #_EXPORT_CREDENTIALS_======================================================
    U_user=os.getenv('FIRE_U_U')
    U_password=os.getenv('FIRE_P_U')
    R_user=os.getenv('FIRE_R_R')
    R_password=os.getenv('FIRE_R_P')

    #_MAKE_FOLDER_=============================================================
    today = datetime.now()
    os.mkdir("/var/local/zip_config_main_srx" + today.strftime('%Y%m%d'))

    #_MAIN_SRX_|_COPY_ZIP_CONFIG_FROM_MAIN_SRX_TO_TEMP_FOLDER_ON_LINUX_PC======
    main_ip = '10.18.164.1'
    main_ssh = createSSHClient(main_ip, 22, U_user, U_password)
    main_scp = SCPClient(main_ssh.get_transport())
    main_scp.get('/config/juniper.conf.gz', "/var/local/zip_config_main_srx" + today.strftime('%Y%m%d') + "/" + main_ip + "_juniper.conf.gz")

    #_SPARE_SRX_|_COPY_ZIP_CONFIG_FROM_LINUX_PC_TO_SPARE_SRX===================
    spar_ip = '10.18.164.2'
    spar_ssh = createSSHClient(spar_ip, 22, R_user, R_password)
    spar_scp = SCPClient(spar_ssh.get_transport())
    spar_scp.put("/var/local/zip_config_main_srx" + today.strftime('%Y%m%d') + "/" + main_ip + "_juniper.conf.gz", '/config/juniper.conf.gz')

    #_DELAY_FOR_COPY_ZIP
    time.sleep(10)

    #_MODIFY_SPARE_SRX_|_COMMIT_NEW_CONFIG_AND_MODIFY_AS_A_SPARE===============
    device_params = {
        'device_type': 'juniper_junos',
        'ip': spar_ip,
        'username': U_user,
        'password': U_password,
    }

    #with ConnectHandler(**device_params, global_delay_factor=3) as srx_ssh:
    with ConnectHandler(**device_params) as srx_ssh:
        srx_ssh.send_config_set('load override /config/juniper.conf.gz')
        srx_ssh.send_config_set('set interfaces ge-0/0/7 unit 0 family inet address 10.18.164.2/30', cmd_verify=False)
        #srx_ssh.send_config_set('set interfaces ge-0/0/7 description TEST88', delay_factor=1,)
        srx_ssh.send_config_set('delete interfaces ge-0/0/7 unit 0 family inet address 10.18.164.1/30', cmd_verify=False)
        srx_ssh.send_config_set('set routing-options static route 10.20.1.233/32 next-hop 10.18.164.1', cmd_verify=False)
        srx_ssh.commit()
        srx_ssh.send_config_set('run request system autorecovery state save', delay_factor=10)
        srx_ssh.disconnect()
