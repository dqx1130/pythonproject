def option():
    while True:
        print("请输入enc（加密）或dec（解密），退出请输入q")
        mode=input("选择：").lower()
        if mode in "enc dec q".split():
            return mode
        else:
            print("请输入正确选项！")

def getKey(mode):
    key=0
    while key<=0 or key>=26:
        try:
            key=int(input("请输入密钥（1-26）："))
        except:
            print("请输入正确密钥！")
    if mode=="dec":
        key=-key  #对密钥进行变换
    return key

def getMessage(key):
    text=input("请输入一段英文：")
    message=""
    for i in text:
        num=ord(i)
        num=num+key
        if i.isupper():
            if num>ord("Z"):
                num=num-26
            elif num<ord("A"):
                num=num+26
        elif i.islower():
            if num>ord("z"):
                num=num-26
            elif num<ord("a"):
                num=num+26
        message += chr(num)
    return message

mode = option()
if mode == "q":
    print("欢迎下次使用！")
elif mode == "enc":
    key=getKey(mode)
    str1=getMessage(key)
    print("密文为：",str1)
elif mode == "dec":
    key=getKey(mode)
    str2=getMessage(key)
    print("明文为：",str2)

