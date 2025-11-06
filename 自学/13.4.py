import re
s = 'abc123abc'
print(re.search('[a-z]+',s).group())
print(re.search('[a-z]+',s).span())
print(re.search('[\d]+',s).group())
print(re.search('[\d]+',s).span())
print(re.search('[a-z]+',s))
print(re.search('xyz',s))