import requests
def allvisit(a):
    r = requests.get(a)
    # file = open(r"C:\Users\23940\Desktop\out.txt", "w",encoding='utf-8')
    print("访问网站：",a,"\n返回的http状态码为：",r.status_code)
    print("响应对象的类型为：",type(r))
    print("响应的内容为:",r.text)
    print("cookies值为",r.cookies)
    # file.write(r.text)
allvisit("http://www.baidu.com")
