str=input("请输入密文：")
n=int(input("请输入密钥："))
str_decrypt=""
for word in str:
    if word==" ":  #遇到空格选择不解密
        word_decrypt=" "
    else:
        word_decrypt=chr((ord(word)-ord("A") -n) %26 +ord("A"))
    str_decrypt = str_decrypt+word_decrypt
print("明文为：",str_decrypt)
