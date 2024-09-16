import random
list = []
for i in range(0,10000):
    a = random.randint(1,65535)
    list.append(a)
lenth = len(list)
target = input("请输入目标整数！：")
iffound = 0
for a in range(0,lenth,1):
    for b in range(a,lenth,1):
        if int(target) == list[a] + list[b] :
            print([a,b])
            iffound = 1
if iffound == 0:
    print("找不到诶！！！")