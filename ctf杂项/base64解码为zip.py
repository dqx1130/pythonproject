#将base64解码以字节流形式写成zip
import base64

with open(r"C:\Users\mimo\Desktop\1.txt",'rb') as file:
    with open('1.jpg','wb') as new_file:
        new_file.write(base64.b64decode(file.read()))
