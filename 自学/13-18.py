import re
m = re.match(r"(\w+) (\w+)","We are family")
print(m.group(0))
print(m.group(1))
print(m.group(0,1))
