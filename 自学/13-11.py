#split()函数的应用
import re
s = "We are family"
print(re.split(' ',s)) #使用空格分割字符串，只要有空格就分割
str = re.split(' ',s,1) #使用空格分割字符串，只分割一次
for i in str:
    print(i)
print(re.split('r',s)) #使用r分割字符串