import re
s = 'Python@163.com'
p = r"(\w{4,20})@(163|qq|gmail|outlook)\.(com)"
n = re.match(p,s)
print(n)
print(n.group())
print(n.group(1))