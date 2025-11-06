import re
s = 'abc123abc'
print(re.match('[a-z]+',s))
print(re.match('[a-z]+',s).group(0))
print(re.match('[\d]+',s))
print(re.match('[A-Z]+', s , re.I).group(0))
print(re.match('[a-z]+',s).span())