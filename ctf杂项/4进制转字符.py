flag = "12031310"
str1 = ''
for i in range(0, len(flag), 4):
    tmp = flag[i:i + 4]
    str1 += chr(int(tmp, 4))

print(str1)