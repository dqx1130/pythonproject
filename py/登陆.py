#账号密码数据库
username = ["admin"]
passwd = ["password"]

#登陆
times = 0
while True:
    usernameinput = input("请输入账号：")
    userpasswdinput = input("请输入密码：")
    #验证账号
    for i in range(len(username)):
        if username[i] == usernameinput and passwd[i] == userpasswdinput:
            print("登陆成功")
            exit()
        else:
            print("登陆失败")
            times += 1
            if times == 3 :
                print("登陆超过三次，请稍后再试")
                exit()



