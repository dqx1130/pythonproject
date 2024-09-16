plain = input("请输入需要加密的明文：")
x = input("请输入需要替换的字符：")
y = input("请输入将要替换的字符：")

# 加密的代码
if len(x) != len(y):
    print("需要替换的字符数量必须跟将要替换的字符数量一致！")
else:
    cipher = plain.translate(str.maketrans(x, y))
    print("加密后的密文是：" + cipher)

# 检测冲突的代码
# flag 变量标志是否退出检测（只要找到一个冲突，就可以直接退出）
flag = 0

# 如果 x 中存在相同的字符，那么 y 对应下标的字符也应该是相同的
for each in x:
    if x.count(each) > 1 and flag == 0:
        i = x.find(each)
        last = y[i]
        while i != -1:
            if last != y[i]:
                print("由于替换字符出现冲突，该密文无法解密！")
                flag = -1
                break

            i = x.find(each, i + 1)

# 如果 y 中存在相同的字符，那么 x 对应下标的字符也应该是相同的
for each in y:
    if y.count(each) > 1 and flag == 0:
        i = y.find(each)
        last = x[i]
        while i != -1:
            if last != x[i]:
                print("由于替换字符出现冲突，该密文无法解密！")
                flag = -1
                break

            i = y.find(each, i + 1)