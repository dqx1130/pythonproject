list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 8, 5, 6, 3, 2, 1, 2]
count = list.count(1)
print("list中1的个数",count)
length = len(list)
print("list列表中一共有",length,"个数")
for i in range(length):
    if list[i] == 1:
        count -= 1
        print("现在还剩",count,"个 1")
    if count == 0:
        print(i)
        break
