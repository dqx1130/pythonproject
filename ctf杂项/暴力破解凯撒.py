LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
LETTERS1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS2="abcdefghijklmnopqrstuvwxyz"

text=input("请输入密文：")
for key in range(len(LETTERS)):
    str=""
    for i in text:
        if i in LETTERS:
            if i.isupper():  #密文字母为大写
                num = LETTERS1.find(i)  #在字母里搜索到密文字符的位置
                num = num - key
                if num<0:
                    num = num + len(LETTERS1)
                str = str + LETTERS1[num]  #将解密后字符追加到字符串末尾
            elif i.islower():  #密文字母为小写
                num = LETTERS2.find(i)  #在字母里搜索到密文字符的位置
                num = num - key
                if num<0:
                    num = num + len(LETTERS2)
                str = str + LETTERS2[num]  #将解密后字符追加到字符串末尾
        else:
            str = str + i  #如果密文中内容不在字母里则不解密，直接追加
    print('第%d把钥匙的结果是%s' %(key, str))  #显示每一个可能的值
