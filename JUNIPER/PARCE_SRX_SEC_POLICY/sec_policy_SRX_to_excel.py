#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from sys import argv
import os
import re
import glob
import xlwt



#file_path = input('Insert path where config file are ( for example: /var/logs/conf.cfg ): ')
file_path = 'D:\TEST_CFG\policy_config.txt'

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("SRX_POLICY_List_#1") 

FILTER_ZONES = r'from-zone (.+) to-zone (.+) .+'
FILTER_POLIC = r'.+ policy (.+) .+'
FILTER_SOURC = r'.+ source-address (.+)'
FILTER_DESTN = r'.+ destination-address (.+)'
FILTER_APPLI = r'.+ application (.+)'

with open(file_path, 'r') as f:
    n = 0
    for line in f:
        match = re.match(FILTER_ZONES, line)
        if match:
            n = n + 1
            sheet1.write(n, 1, match.group(1))
            sheet1.write(n, 2, '---->')
            sheet1.write(n, 3, match.group(2))
        match = re.match(FILTER_POLIC, line)
        if match:
            n = n + 1
            sheet1.write(n, 4, match.group(1))
        match = re.match(FILTER_SOURC, line)
        if match:
            sheet1.write(n, 5, match.group(1))
        match = re.match(FILTER_DESTN, line)
        if match:
            sheet1.write(n, 6, match.group(1))
        match = re.match(FILTER_APPLI, line)
        if match:
            sheet1.write(n, 7, match.group(1))
        if "permit" in line:
            sheet1.write(n, 8, "permit")
        elif "reject" in  line:
            sheet1.write(n, 8, "reject")
        elif "deny" in line:
            sheet1.write(n, 8, "deny")
        elif "log {" in line:
            sheet1.write(n, 9, "log")
        elif "session-init;" in line:
            sheet1.write(n, 10, "session-init")
        elif "session-close;" in line:
            sheet1.write(n, 11, "session-close")

book.save("SRX_POLICY_table1.xls")
