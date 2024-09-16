# f = open(r'flag.txt','w')
str="0123456789"
print("字符串：",str)
print("字符串长度为：",len(str))
ss=''
for i in range(len(str),0,-2):
    s=str[i-2:i]
    ss=ss+s
print(ss)
# print(ss,file=f)
# f.close()

import requests