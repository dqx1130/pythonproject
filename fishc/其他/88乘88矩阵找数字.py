import random
list = []
for a in range(88):
    list.append([])
    for b in range(88):
       list[a].append(random.randint(0,1024))
print(list)
maninput = int(input("请输入："))
for i in range(88):
    for j in range(88):
        if maninput == list[i][j]:
            print(i,j)