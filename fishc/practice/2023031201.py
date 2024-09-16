# 统计字符串中的单词个数（“单词”以空格进行分隔）
userinput = input("输入:")
count = 1
if len(userinput)  == 0 :
    print("输出:0")
else:
    for each in userinput:
        if ord(each) == 32:
            count += 1
    print("输出:",count)

#方法二
# s = input("请输入测试字符串：")
# print(len(s.split()))