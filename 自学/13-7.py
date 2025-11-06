import re
string = "abc 123 def 456"
#带括号和不带括号的区别

#带多个括号
p = re.compile("((\w)\s+\w+)")
print(p.findall(string))

#带一个括号
p1 = re.compile("(\w)\s+\w+")
print(p1.findall(string))

#带一个括号
p2 = re.compile("\w\s+\w+")
print(p2.findall(string))