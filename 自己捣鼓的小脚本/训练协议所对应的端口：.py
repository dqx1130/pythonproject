import random

list1 = [
        "20",#1
        "21",#2
        "22",#3
        "23",#4
        "25",#5
        "53",#6
        "67",#7
        "69",#8
        "80",#9
        "110",#10
        "123",#11
        "161",#12
        "443",#13
        "143",#14
        "1723",#15
        "1645"#16
        ]
#list1为端口列表

list2 = [
        "ftp",#1
        "ftp",#2
        "ssh",#3
        "telnet",#4
        "smtp",#5
        "dns",#6
        "dhcp",#7
        "tftp",#8
        "http",#9
        "pop3",#10
        "ntp",#11
        "snmp",#12
        "https",#13
        "imap",#14
        "pptp",#15
        "radius"#16
        ]
#list2为协议列表，一定要保证一一对应。

jugde = 1
while True:
    i = random.randint(0,15)
    if jugde == 1:
        print("协议为：",list2[i],",其对应的端口号为：","      (输入stop以结束)")
        cat = input("")
        if cat == "stop":  # 输入stop，训练结束
            jugde = 0
            break
        if list2[i] == "ftp" and (cat == "20" or cat == "21"):  # ftp有两个答案
            print("正确")
        elif cat == list1[i]:
            print("正确")
        else:
            print("错误,","正确答案为：",list1[i])
    else:
        break

#  Written by dqx , 2022/6/15