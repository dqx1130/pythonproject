import hashlib
data = {}
while True:
    user = input("请输入用户名：")
    if user in data.keys():
        print("当前用户名已被注册")
        user = input("请重新输入用户名：")
    else:
        pwd = hashlib.md5(bytes(input("请输入密码"), "utf-8")).hexdigest()
        data[user] = pwd
    if "N" in input("是否继续录入？（Y/N)"):
        break
print("目前已注册的用户有：")
for each in data:
    print(each+":"+data[each])

