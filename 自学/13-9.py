#提取所有的号码和邮箱类型
import re
content = '''
email:2345678@163.com
email:345678@163.com
'''
result_finditer = re.finditer(r"(\d+)@(\w+).com",content)
#正则有两个分组，需要分别获取分区，分组从0开始，group方法不传递索引默认为0，代表了整个正则的匹配结果
for i in result_finditer :
    print(i.group(1)+' '+i.group(2))
result_findall = re.findall(r"(\d+)@(\w+).com",content)
print(result_findall)
#此时返回的虽然为[]，但不是简单的[]，而是一个tuple类型的list
for i in result_findall:
    print(i[0]+" "+i[1])