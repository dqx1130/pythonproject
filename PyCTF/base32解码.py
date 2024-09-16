import base64
file = open(r"C:\Users\Administrator\Desktop\flag.txt","w+",encoding='utf-8')
a = file.read()
b = str(base64.b32decode(a),'utf-8')
print(b)
file.write(b)
file.close()
