file = open(r"C:\Users\23940\Desktop\flag.txt")
#读取每一行，并加入list
list = []
for line in file:
    line = line.strip()
    list.append(line)
print(list)
#循环转换chr
flag=''
for i in range(len(list)):
    list[i] = int(list[i])
    flag = flag + chr(list[i])
    print(flag)


