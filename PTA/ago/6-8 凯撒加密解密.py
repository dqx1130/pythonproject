def Decrypt( cryptedText, numToMove):
    res = ''
    for each in cryptedText:
        if each.isupper():
            res += chr((ord(each) - 65 - numToMove)%26 + 65)
        elif each.islower():
            res += chr((ord(each) - 97 - numToMove)%26 + 97)
        else:
            res += each
    return res

# text = input('请输入密文：')
# num = eval(input("请输入加密的移动位数："))
text ="mjqqt btwqi"
num = 5
orgText = Decrypt(text, num)
print(orgText)
