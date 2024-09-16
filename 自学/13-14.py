#分组举例
import re
s = 'a1a b2b a3a'
p = re.compile(r'(\w)(\d)a')
result = re.findall(p,s)
print(result)