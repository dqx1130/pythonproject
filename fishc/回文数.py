judge = 0
while True :
    a = (input("请输入一个正整数："))
    if a.isdigit():
        judge = 1
        break
if judge == 1:
    if a[::1] == a[::-1]:
        print(a,"是回文数")
    else:
        print(a,"不是回文数")