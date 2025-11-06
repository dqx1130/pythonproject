import base64
f = open(r'C:\Users\23940\Desktop\base64加密50次.txt','wb')
flag='flag{h4ve_fun^_^!!!}'
for i in range(0,30):
    encryption = str(base64.b64encode(flag.encode('utf-8')), "utf-8")
    flag = encryption
print(flag)
