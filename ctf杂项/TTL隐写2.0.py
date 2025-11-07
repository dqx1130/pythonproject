import binascii
f=open("C:/Users/槐序/Desktop/out.txt","r")
f2=open("C:/Users/槐序/Desktop/flag.txt","wb")
num=''
res=''
for i in f:
    if int(i)==63:
        num+="00"
    if int(i)==127:
        num+="01"
    if int(i)==191:
        num+="10"
    if int(i)==255:
        num+="11"
for j in range(0,len(num),8):
    res += chr(int(num[j:j+8],2))#转换为字符
res = binascii.unhexlify(res)#unhexlify:从十六进制字符串返回二进制数据
f2.write(res)