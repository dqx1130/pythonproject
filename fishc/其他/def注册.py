import hashlib
database = {}
def get_int():
    print("1.注册\n2.登录\n3.退出")
    choice = input()
    while choice != '1' and choice != '2' and choice != '3':
        choice = input("错误！请输入正确的指令：")
        if choice == '1' or choice == '2' or choice == '3':
            break
    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        print(database)

def register():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    password = encrypt(password)
    database[username] = password
    print("恭喜，注册成功！")

def login():
    username = input("请输入用户名：")
    while True:
        if username in database:
            break
        else:
            print("该用户名不存在")
            username = input("请重新输入用户名：")
    password = input("请输入密码：")
    password = encrypt(password)
    while True:
        if password == database[username]:
            break
        else:
            print("密码错误")
            password = input("请重新输入密码：")
            password = encrypt(password)
    print("恭喜登录成功")

def encrypt(plaintext):
    bstr = bytes(plaintext, "utf-8")
    ciphertext = hashlib.md5(bstr).hexdigest()
    return ciphertext

while True:
    get_int()
