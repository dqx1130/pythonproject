import requests
url = "http://challenge.xinshi.fun:44003/upload"

with open(r"C:\Users\admin\Desktop\tmp\2.zip","rb") as f:
    files ={'file':('2.zip',f)}
    res = requests.post(url ,files = files)
    print(res.status_code)
print(res.text)

