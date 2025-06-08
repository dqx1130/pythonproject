
tmp = list(map(int,input().split(" ")))
length = len(tmp)
list1 = tmp[1:length - 1]
length = len(list1)
index = tmp[0]
print(list1)
print(length)
print(index)
if index <= length:
    print(list1[length - index ])
else:
    print("NULL")