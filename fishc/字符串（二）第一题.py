#用户输入两个版本号 v1 和 v2，请编写代码比较它们，找出较新的版本。
#也可以用于ip地址排序
v1 = input("请输入第一个版本号，v1 =")
v2 = input("请输入第一个版本号，v2 =")
n = len(v1)       #v1版本号的长度
m = len(v2)       #v2版本号的长度
i = 0             #i为当前遍历到v1的位置
j = 0             #j为当前遍历到v2的位置
while i < n or j < m:
    x = 0       #用于记录小数点前的v1大小
    while i < n and v1[i] != '.':
        x = x * 10 + int(v1[i])         #将所有数字向上移一位，为个位数腾出空间
        i += 1                          
    i += 1      #如果在第一个小数点前，v1=v2，此时的i遍历到第一个小数点后
    y = 0       #用于记录小数点前的v2大小
    while j < m and v2[j] != '.':
        y = y * 10 + int(v2[j])
        j += 1
    j += 1
#相当于，从左到右的比较小数点前的数
    if x > y:
        print("v1")
        break
    elif x < y:
        print("v2")
        break

if x == y:
    print("v1 = v2")

