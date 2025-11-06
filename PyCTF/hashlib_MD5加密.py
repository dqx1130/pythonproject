import hashlib
inputstr=input("请输入要进行MD5加密的字符串：")
a = hashlib.md5(inputstr.encode('UTF-8')).hexdigest()
print(a)