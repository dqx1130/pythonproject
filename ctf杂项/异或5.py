import base64

f1 = open("C:/Users/槐序/Desktop/真实的压缩包/亦真亦假", 'r')
xor_data = f1.read()
f1.close()
dec_data = ""
for i in xor_data:
    tmp = int(i, 16) ^ 5
    dec_data += hex(tmp)[2:]

print(dec_data)
f2 = open('./data.doc', 'wb')
f2.write(base64.b16decode(dec_data.upper()))
f2.close()