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

Если нужно чтобы python был в директории /usr/bin/ (например /usr/bin/python3.7)
```sh
# ./configure --prefix=/usr  --enable-optimizations
# make
# make install
```

Sometimes you have to reinstall pip yourself (it happens for example when you can't install modul netmiko because of stupid error you don't know, as fast resolve it is good, one time it helps me :)):

```sh
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python3 get-pip.py --force-reinstall
# pip install netmiko
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

---

### TIMER UNIT ###

Описание: создадим службу, которая будет запускать скрипт python по расписанию (альтернатива cron)

Дано: 
- сркипт /var/refresh_spare_srx_config.py 
- скрипт запускаемый chmod +x

Создаем юнит, который будет запускать скрипт
```shell
vim /usr/lib/systemd/system/refresh_srx.service
```
Содержание:
```shell
[Unit]
Description=Refresh combat config of spare SRX

[Service]
Type=simple
ExecStart=/usr/local/bin/python3.7 '/var/refresh_spare_srx_config.py'

[Install]
WantedBy=multi-user.target
```
Создание таймера
```shell
vim /usr/lib/systemd/system/refresh_config.timer
```
Содержание:
```shell
[Unit]
Description=Execute every day at 04:00

[Timer]
OnCalendar=*-*-* 04:00:00
Unit=refresh_srx.service

[Install]
WantedBy=multi-user.target
```

#### Проверка ####
Активируем загрузку и запустим сервис:

```shell
systemctl enable refresh_config.timer
systemctl start refresh_config.timer
```

Для проверки автозапуска:

```shell
systemctl is-enabled refresh_config.timer
enabled
```
Для проверки запуска таймера:

```shell
systemctl is-active refresh_config.timer
active
```
Если необходимо, сервис можно запустить вручную в любое время:

```shell
systemctl start refresh_config
```
Если были внесены какие-то изменение в таймер, например время выполнения, то необходимо произвести обновление сервиса:

```shell
systemctl daemon-reload
```
Просмотр таймеров в системе

```shell
systemctl list-timers refresh_config*
```

---------------------------------------

#### Crone example:

RUN it on 3-00 AM: 
```sh
# crontab -e

00 03 * * * /usr/local/bin/python3.7 /home/parse_example.py
```


