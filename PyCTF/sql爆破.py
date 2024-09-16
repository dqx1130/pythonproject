import requests
list=[]
i = 0
while i <= 999999:
    list.append(i)
    i += 1


import_url =""
j = 3
while True:
    url = import_url + str(list[j])
    if int(len(requests.get(url).text)) >= 492:
        break
    j += 1
print(url)





