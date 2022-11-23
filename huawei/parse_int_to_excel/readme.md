Парсит конфиг хуавея, выдергивает интерфейсы в excel. Скрипт не доделан.



```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from sys import argv
import os
import re
import glob
import xlwt

# file_path = input('Insert path where config file are ( for example: /var/logs/conf.cfg ): ')
file_path = "D:\conf\conf1.txt"

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("CAPASITY_SWPRT-01_List_#1")

# add new colour to palette and set RGB colour value
xlwt.add_palette_colour("custom_colour", 0x21)
book.set_colour_RGB(0x21, 251, 228, 228)

# now you can use the colour in styles
style = xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour')


# ОПИСАНИЕ ФИЛЬТРОВ ДЛЯ ПАРСИНГА КОНФИГУРАЦИИ (https://regex101.com/):
FILTER_INTERF_1 = r'interface Eth-Trunk(\d+)'  # интерфейс вида - interface Eth-Trunk37
FILTER_INTERF_2 = r'interface Eth-Trunk(.+)'  # интерфейс вида - interface Eth-Trunk5.400 mode l2
FILTER_INTERF_3 = r'interface Eth-Trunk(.+)'  # интерфейс вида - interface 25GE1/0/5

# ИДЕМ ЦИКЛОМ ПОСТРОЧНО ПО КОНФИГУРАЦИОННОМУ ФАЙЛУ:
with open(file_path, 'r') as f:
    sheet1.write(1, 1, 'PORT', style)
    sheet1.write(2, 1, 'MODE', style)
    sheet1.write(3, 1, 'DESCRIPTION', style)
    sheet1.write(4, 1, 'ETH-TRUNK', style)
    sheet1.write(5, 1, 'ENCAP', style)
    sheet1.write(6, 1, 'BD', style)
    n = 1
    for line in f:
        match = re.match(FILTER_INTERF_1, line)
        if match:
            n = n + 1
            sheet1.write(4, n, match.group(1))




# СОХРАНЯЕМ КНИГУ:
book.save("CAPASITY_SWPRT.xls")
```


Дергает из конфига только строчки с interface Eth-Trunk37, interface Eth-Trunk5.400 mode l2, interface 25GE1/0/5

Пример конфига:

```
interface Eth-Trunk0
 stp edged-port enable
 mode lacp-static
 peer-link 1
#
interface Eth-Trunk1
 stp edged-port enable
#
interface Eth-Trunk1.4 mode l2
 encapsulation dot1q vid 4
 bridge-domain 4
#
interface Eth-Trunk1.21 mode l2
 encapsulation dot1q vid 21
 bridge-domain 21
#
interface 25GE1/0/14
 eth-trunk 14
 device transceiver 10GBASE-FIBER
 port mode 10G
#
interface 25GE1/0/15
 stp edged-port enable
 device transceiver 10GBASE-FIBER
 port mode 10G
#
```
