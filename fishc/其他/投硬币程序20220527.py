import random
counts=int(input("请输入投硬币的次数：")) #输入硬币次数
judge=0 #判断次数是否大于100次，大于就不打印
if counts > 100:
        judge = 1
i=0 #现在硬币抛了多少次
turescounts=0 #正面的次数
flasecounts=0 #反面的次数
maxture=0 #连续正面最大次
lasttrue=0 #正面持续次数
lastfalse=0 #反面持续次数
maxflase=0 #连续反面最大次
last=0 #上一次是正还是反,1为正面，2为反面，初始值为0
while i < counts:
        num = random.randint(1,10)
        if num % 2 == 0:
                turescounts += 1
                last = 1
                if not judge:
                        print("正面",end=" ")
                if last == 1:
                        lasttrue = lasttrue + 1
                        if lasttrue > maxture:
                                maxture = lasttrue
                                lasttrue = 0
        else:
                flasecounts += 1
                last = 2
                if not  judge:
                        print("反面",end=" ")
                if last == 2:
                        lastfalse = lastfalse + 1
                        if lastfalse > maxflase:
                                maxflase = lastfalse
                                lastfalse = 0
        i += 1
print("正面",str(turescounts),"次",end=" ")
print("反面",str(flasecounts),"次",end=" ")
print("正面连续投了",str(maxture),"次",end=" ")
print("反面连续投了",str(maxflase),"次",end=" ")