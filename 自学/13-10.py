#sub()和subn()函数的区别
import re
p = re.compile(r'(\w+) (\w+)')
s = 'i say. hello world!'

def func(m):
    return m.group(1).title() + ' ' + m.group(2).tilte()
print(p.sub(r'\2 \1',s))
print(p.sub(r'func',s))

print(p.subn(r'\2 \1',s))
print(p.subn(r'func',s))

#   sub()函数用于替换在字符串中符合正则表达式的内容，它返回替换后的字符串。
#   subn()函数除了返回被替换后的字符串，还会返回一个替换次数，它们是以元组的形式返回的。