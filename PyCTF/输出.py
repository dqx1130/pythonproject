f = open(r'C:\Users\23940\Desktop\123.txt','w')
i = 0
while i <= 999999:
    i += 1
    print(str(i), file=f)
f.close()