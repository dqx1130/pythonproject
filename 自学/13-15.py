import re
s = "a1b2 c3d4 ea7f"
p1 = re.compile(r'[a-z]\d[a-z]\d')
print(re.findall(p1,s))

p2 = re.compile(r'[a-z]\d[a-z](\d)')
print(re.findall(p2,s))

p3 = re.compile(r'[a-z](\d)[a-z](\d)')
print(re.findall(p3,s))
