#输入ip并录入列表ip中：
ip =[]
while True:
    userinput = input("请输入ip地址(stop停止，完整输入ipv4后，请按回车！):")
    if userinput == 'stop':
        break
    else:
        ip.append(userinput)
# print(len(ip))
# print(len(ip[1][0]))

#对列表ip进行去除小数点，录入二维列表ipsort之中：
ipsort =[]
list =[]
for i in range(len(ip)):
    str1 = ip[i]
    list= str1.split('.')
    # print(list)
    ipsort.append(list)
    # print(ipsort)
# [
#   ['10', '51', '3', '31'],
#   ['10', '41', '2', '15'],
#   ['152', '222', '55', '1'],
#   ['15', '5', '64', '22'],
#   ['123', '213', '25', '11']
# ]

for i in range(len(ipsort)):
    for j in range(len(ipsort[i])):
        ipsort[i][j] = int(ipsort[i][j])
        # print(ipsort)

#第一次冒泡排序：
for i in range(len(ipsort)):
    for j in range(0, len(ipsort) - i - 1):
        if ipsort[j][3] > ipsort[j + 1][3]:
            ipsort[j], ipsort[j + 1] = ipsort[j + 1], ipsort[j]
# print(ipsort)

#第二次冒泡排序:
for i in range(len(ipsort)):
    for j in range(0, len(ipsort) - i - 1):
        if ipsort[j][2] > ipsort[j + 1][2]:
            ipsort[j], ipsort[j + 1] = ipsort[j + 1], ipsort[j]
# print(ipsort)

#第三次冒泡排序:
for i in range(len(ipsort)):
    for j in range(0, len(ipsort) - i - 1):
        if ipsort[j][1] > ipsort[j + 1][1]:
            ipsort[j], ipsort[j + 1] = ipsort[j + 1], ipsort[j]
# print(ipsort)

#第四次冒泡排序:
for i in range(len(ipsort)):
    for j in range(0, len(ipsort) - i - 1):
        if ipsort[j][0] > ipsort[j + 1][0]:
            ipsort[j], ipsort[j + 1] = ipsort[j + 1], ipsort[j]
# print(ipsort)

#输出
for i in range(len(ipsort)):
    print(str(ipsort[i][0])+"."+str(ipsort[i][1])+"."+str(ipsort[i][2])+"."+str(ipsort[i][3]))