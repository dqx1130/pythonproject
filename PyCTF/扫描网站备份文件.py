import requests

input_url = input("请输入待扫描的URL：")
list1 = ['web', 'website', 'backup', 'back', 'www', 'wwwroot', 'temp']
list2 = ['tar', 'tar.4gz', 'zip', 'rar', 'bak']

for each1 in list1:
    for each2 in list2:
        bak = each1 + '.' + each2
        url = 'http://' + input_url + '/' + bak  # 添加协议前缀
        response = requests.head(url)
        print(bak, "HTTP状态码：", response.status_code,"返回长度",response.headers.get('Content-Length'))
