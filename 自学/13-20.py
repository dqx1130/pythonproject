import re
print(re.findall(r'(?i)yes','yes! Yes.. YES??'))
print(re.findall(r'(?i)p\w+','Python is a very easy to use programming language'))
print(re.findall(r'(?im) (^th[\w ]+)',
"""
... This is the frist,
... another line,
... that line,it's the best
... """ ))