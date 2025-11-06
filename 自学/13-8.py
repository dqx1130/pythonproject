##提取所有的号码和邮箱类型
import re
content ='''
email:12345678@163.com
email:2345678@163.com
email:345678@163.com
'''

#re.finditer正则匹配
result_finditer = re.finditer(r"\d+@\w+.com",content)
print(result_finditer)
#由于返回的为MatchObjective的iterator，所以需要迭代并通过MatchObjective的方法输出
#否则就会输出 <callable_iterator object at 0x00000***********>
for i in result_finditer :
    print(i.group())

#re.findall正则匹配
result_findall = re.findall(r"\d+@\w+.com",content)
print(result_findall)
for i in result_findall :
    print(i)