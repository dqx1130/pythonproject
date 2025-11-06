# -*- encoding: utf-8 -*-
import base64

f = open(r'C:\Users\23940\Desktop\base64套娃.txt','rb').read()
while True:
    f = base64.b64decode(f)
    if b'{' in f:
        print(f)
        break
    else:
        continue
