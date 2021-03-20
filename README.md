# PYTHON
Python tools

INSTALL PYTHON:
------------------------------------------------------------
Install python 3.7 на CentOS7:

```sh
# yum update
# yum install openssl-devel zlib-devel libffi-devel gcc -y
# cd /usr/src 
# wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz
# tar xzf Python-3.7.5.tgz
# cd Python-3.7.5 
# ./configure --enable-optimizations 
# make altinstall
# rm /usr/src/Python-3.7.5.tgz
# pip3.7 install --upgrade pip
```

Sometimes you have to reinstall pip yourself (it happens for example when you can't install modul netmiko because of stupid error you don't know, as fast resolve it is good, one time it helps me :)):

```sh
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python3 get-pip.py --force-reinstall
# pip install netmiko
```
RUN it on 3-00 AM: 
```sh
# crontab -e

00 03 * * * /usr/local/bin/python3.7 /home/parse_example.py
```

LOGIN AND PASSWORD in ENV store:
------------------------------------------------------------
```sh
# echo "export FIRE_U_U="admin"" >> ~/.bashrc && source ~/.bashrc
# echo "export FIRE_P_U="Pasw00rD"" >> ~/.bashrc && source ~/.bashrc
# echo $FIRE_U_U
```
or

```sh
# env
```

HOW USE IT IN PYTHON CODE:

```py
import os
U_user = os.getenv('FIRE_U_U')
U_password = os.getenv('FIRE_P_U')
```
