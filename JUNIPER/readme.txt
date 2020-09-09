Scripts for JUNOS
==============================================================

Установка python 3.7 на CentOS7:

yum update

yum install zlib-devel
yum install openssl-devel

cd /usr/src 
wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz
tar xzf Python-3.7.5.tgz
cd Python-3.7.5 
./configure --enable-optimizations 
make altinstall
rm /usr/src/Python-3.7.5.tgz
pip3.7 install --upgrade pip

Sometimes you have to reinstall pip yourself (it happens for example when you can't install modul netmiko because of stupid error you don't know, as fast resolve it is good, one time it helps me :)):

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py --force-reinstall
pip install netmiko

RUN it on 3-00 AM: 
crontab -e
00 03 * * * /usr/local/bin/python3.7 /home/parse_example.py
