import base64


def b64encode():  # 定义一个加密函数
    a = input("base64加密：")  # input()函数接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。
    encode = base64.b64encode(a.encode('utf-8'))  # 因为3.x中字符都为unicode编码，而b64encode函数的参数为byte类型，所以必须先转码
    print(("**********encryption complete**********\n:"), str(encode, 'utf-8'))  # 将byte转换回去就好了，如果不转的化，输出结果会被字符串b包围
    return "****************************************"


def b64decode():  # 定义一个解码函数
    b = input("base64解码：")
    decode = base64.b64decode(b)
    print(("**********Decoding complete**********\n:"), str(decode, 'utf-8'))
    return "****************************************"


a = 0
while a == 0:  # 设置第一个循环
    print("<<< 选择 >>>\n--加密--\n--解码--\n--退出--")
    user = input("：")
    while (
            user != '加密' and user != '解码' and user != "退出"):  # 设置第二个循环，设置循环条件如果不等于这些条件
        print("输入错误!请重新输入:")  # 就一直会在 print("输入错误!请重新输入:")循环
        user = input("：")

    if user == '加密':  # 如果输入的字符等于加密就执行下一个条件，进行加密
        c = b64encode()
        print(c)
    if user == '解码':  # 如果输入的字符等于解码就执行下一个条件，进行解码
        b = b64decode()
        print(b)
    if user == '退出':  # 输入退出则跳出循环，退出程序
        break
print("已退出")

