list = []   #用于记录用户输入数字的列表。
judge = 1   #判断值judge，决定了while循环是否可以进行。
while judge == 1:   #只有在判断值judge为1时，while循环才能跑起来。
    x = (input("请输入一个正整数(输入stop结束！)："))    #用户输入正整数。
    if x == "stop":     #如果用户输入了stop。
        judge = 0       #判断值judge改为1。
        break           #退出while循环，不重开了，结束了。
    if int(x) <= 0:     #如果用户输入的不是正整数。
        print("他妈的说了多少遍了！正整数！正整数！他妈的正整数！")   #善意的提醒 ^_^
        continue           #退出while循环,并且重开本轮循环。
    list.append(int(x))     #将用户输入的数放到list列表之中。
if judge == 0:
    print("生成的列表长这样：",list)
    target = input("请输入目标整数：")
    lenth = len(list)
    iffound = 0
    for i in range(0,lenth,1):
        for j in range(i,lenth,1):
            if int(target) == list[i] + list[j]:
                print([i,j])
                iffound = 1
    if iffound == 0:
        print("找不到诶！")
