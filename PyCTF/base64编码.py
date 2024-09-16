import base64
a = input("请输入需要加密的字符串：")
bs = str(base64.b64encode(a.encode('utf-8')), "utf-8")
# 加密：
print('加密：' + bs)
# 解密：
print('解密：'+ str(base64.b64decode(bs), "utf-8"))