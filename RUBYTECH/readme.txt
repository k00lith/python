Scripts for rubytech switches
==============================================================

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



Запуск по крону в 3-00 ночи: 
crontab -e
00 03 * * * /usr/local/bin/python3.7 /home/parse_example.py
