# -*- encoding: utf-8 -*-
import base64

f = open("C:/Users/mimo/Desktop/flag.txt",'rb').read()
while True:
    f = base64.b64decode(f)
    if b'{' in f:
        print(f)
        break
    else:
        continue
#末尾有==使用这个