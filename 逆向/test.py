enflag = 'izwhroz""w"v.K".Ni'
key = 0x12
result = ""
for i in range(0,key,3):
    a = (ord(enflag[i])^key) - 6
    b = (ord(enflag[i+1])^key) + 6
    c = (ord(enflag[i+2])^key) ^ 6
    result = result + chr(a) + chr(b) + chr(c)
print(result)