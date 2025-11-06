import requests
input_url= input("请输入待扫描的URL：")
list1 = ['web','website','backup','back','www','wwwroot','temp']
list2 = ['tar','tar.gz','zip','rar','bak']
for each1 in list1:
    for each2 in list2:
        bak = each1 + '.' + each2
        url = input_url + '/' + bak
        print(bak + '  ',"http状态码：",requests.get(url).status_code,"文件长度：",len(requests.get(url).text))
