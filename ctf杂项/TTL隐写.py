#63 (255) 127 191  得文件
import binascii
with open("C:/Users/槐序/Desktop/out.txt",'r') as fp:
    a=fp.readlines()
    p=[]
    for x in range(len(a)):
       p.append(int(a[x]))
    s=''
    for i in p:
        if(i==63):
            b='00'
        elif(i==127):
            b='01'
        elif(i==191):
            b='10'
        else:
            b='11'
        s +=b
# print(s)
flag = ''
for i in range(0,len(s),8):
    flag += chr(int(s[i:i+8],2))
flag = binascii.unhexlify(flag)
wp = open('ans.zip','wb')
wp.write(flag)
wp.close()

#import binascii
#f=open("attachment.txt","r")
#f2=open("result.txt","wb")
#num=''
#res=''
#for i in f:
#    if int(i)==63:
#        num+="00"
#    if int(i)==127:
#        num+="01"
#    if int(i)==191:
#        num+="10"
#    if int(i)==255:
#        num+="11"
#for j in range(0,len(num),8):
#    res += chr(int(num[j:j+8],2))#转换为字符
#res = binascii.unhexlify(res)#unhexlify:从十六进制字符串返回二进制数据
#f2.write(res)