with open(r"C:\Users\Administrator\Desktop\convert.txt",'r') as f:
    strings = f.read()
f.close()
len1 = len(strings)

print(len1)
list1 = []
list2 = []
list3 = []
for i in range(0,len1 + 1,8):
    list1.append(i)
#list1 用于标记每个8的倍数的位置

len2 = len(list1)
print(list1)
for i in range(len2):
    if i != len2 - 1:
        list2.append(strings[list1[i]:list1[i+1]])
#将每八位二进制，存进list2
print(list2)

len3 = len(list2)
for i in range(len3):
    list3.append(chr(int(list2[i],2)))
    print(chr(int(list2[i],2)))
print(list3)

#将list2中的八位二进制转换为文本

with open(r"C:\Users\Administrator\Desktop\flag.txt","w+") as f:
    f.write("".join(list3))
f.close()