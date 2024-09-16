s = input("请输入测试字符串:")

str09 = []
straz = []

#将数字和字母进行归类存放
for each in s:
    if each.isdecimal():
        str09.append(each)
    else:
        straz.append(each)

len09 = len(str09)
lenaz = len(straz)

#如果两个容器的元素个数相差1个以上，则不满足重新格式化的条件
if abs(lenaz - len09 > 1):
    print("字符串中数字和字母的数量不满足重新格式化的条件。")
else:
    if len09 > lenaz :
        longer = str09
        shorter = straz
    else:
        longer = straz
        shorter = str09

    result = []
    for i in range(len(shorter)):
        result.append(longer[i])
        result.append(shorter[i])

    #由于 longer 是有可能等于 shorter 的，就不必执行下面这一步
    if len(longer) > len(shorter):
        result.append(longer[-1])
    print("".join(result))