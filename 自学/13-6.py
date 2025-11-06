import re
s = "abc123def456"
print(re.findall('[a-z]+',s))
print(re.findall('[0-9]+',s))