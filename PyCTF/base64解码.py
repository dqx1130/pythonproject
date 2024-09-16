import base64
# a = input("请输入需要解密的字符串：")
# # 解密：
# print('解密：'+ str(base64.b64decode(a), "utf-8"))
file_old = open(r"C:\Users\Administrator\Desktop\secenc.txt","w+",encoding='utf-8')
a = file_old.read()
b=str(base64.b64decode(a),"utf-8")
print(str(base64.b64decode(a),"utf-8"))
file = open(r"C:\Users\Administrator\Desktop\flag.txt","w+",encoding='utf-8')
file.write(b)