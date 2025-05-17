def I():
    print("\n--录入模式--")
    while True:
        name = input("请输入姓名：")
        if name in phone_book.keys():
            print(f"该姓名已经录入，手机号码是{phone_book[name]}")
            if "Y" in input("请问是否修改？（Y/N)"):
                phone = input("请输入新的手机号码：")
                phone_book[name] = phone
        else:
            phone = input("请输入手机号码：")
            while  len(phone) != 11 or not phone.isnumeric():
                phone = input("输入不合法，请重新输入：")
            phone_book[name] = phone
            if "N" in input("是否继续录入？（Y/N)"):
                break
def C():
    print("\n--查询模式--")
    while True:
        name = input("请输入姓名：")
        if name in phone_book.keys():
            print(f"{name}:{phone_book[name]}")
        else:
            print("查无此人！")
        if "N" in input("是否继续查询？（Y/N)"):
            break
def D():
    print("\n--删除模式--")
    while True:
        name = input("请输入姓名：")
        if name in phone_book.keys():
            if "Y" in input("确定删除？（Y/N)"):
                del phone_book[name]
                print("成功删除")
        if "N" in input("是否继续删除？（Y/N)"):
            break
def P():
    print("\n--打印模式--")
    for each in phone_book:
        print(each, phone_book[each],sep= ": ")
def E():
    exit()
phone_book = {}
print("欢迎进入电话簿")
while True:
    cmd = input("请输入命令（I:录入/C:查询/D:删除/P:打印/E:退出）：")
    if cmd == "I":
        I()
    elif cmd == "C":
        C()
    elif cmd == "D":
        D()
    elif cmd == "P":
        P()
    elif cmd == "E":
        E()
