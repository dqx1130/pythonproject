import re
def groups(p):
    if p is not None:
        print("p.group()==%s"%p.group())
    else:
        print("p.group()==None"),
    print("p.group()==%s"%str(p.group()))   
p = re.match("(?: [abcd] ) (color)","acolor")
groups(p)