import re
s = "Python is a very easy to use programming language"
p = re.compile(r'to')   #查找'to'
print(p.match(s))
print(p.search(s))