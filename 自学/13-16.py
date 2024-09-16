import re
s = "name:Python,age:10;name:world,age:20"
p = re.compile("(\w),age:(\d+)")
it = re.finditer(p,s)
for m in it:
    print("-------------------------------")
    print(m.group())
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.groups())