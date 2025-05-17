import requests
from bs4 import BeautifulSoup
import re

# 定义要爬取的URL列表
urls = [
    "http://www.just.edu.cn/news/kdyw_8158/list1.htm",
    "http://www.just.edu.cn/news/kdyw_8158/list2.htm",
    "http://www.just.edu.cn/news/kdyw_8158/list3.htm",
    "http://www.just.edu.cn/news/kdyw_8158/list4.htm",
    "http://www.just.edu.cn/news/kdyw_8158/list5.htm",
    "http://www.just.edu.cn/news/kdyw_8158/list6.htm",
    "http://www.just.edu.cn/news/kdyw_8158/list7.htm",
    "http://www.just.edu.cn/news/kdyw_8158/list8.htm",
    "http://www.just.edu.cn/news/kdyw_8158/list9.htm"
]

# 存储新闻信息的列表
news = []

for url in urls:
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    s = BeautifulSoup(r.text, 'html.parser')

    # 查找所有符合条件的<li>标签
    li = s.find_all('li', class_=re.compile(r'news n\d+ clearfix'))

    # 处理每个<li>标签
    for i in li:
        tmp = i.text.split('\n')
        tmp.pop(0)  # 移除第一个空元素
        tmp.pop(-1)  # 移除最后一个空元素
        tmp.append("http://www.just.edu.cn" + i.a.attrs['href'])  # 添加新闻链接

        # 过滤新闻日期在9月至12月或1月的新闻
        if 9 <= int(tmp[1][5:7]) <= 12 or int(tmp[1][5:7]) == 1:
            news.append(tmp)

# 打印所有新闻信息
for each in news:
    print(each)

with open('new.html', 'w', encoding='utf-8') as f:
    f.write('''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <title>新闻</title>
            <style>
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                th, td {
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #f2f2f2;
                }
            </style>
        </head>
        <body>
            <h1>江苏科技大学新闻信息</h1>
            <table>
                <tr>
                    <th>新闻标题</th>
                    <th>发布日期</th>
                    <th>链接</th>
                </tr>
    ''')

    for each in news:
        title = each[0]  # 新闻标题
        date = each[1]  # 日期
        link = each[2]  # 新闻链接

        # 写入表格内容
        f.write(f'''
                <tr>
                    <td>{title}</td>
                    <td>{date}</td>
                    <td><a href="{link}" target="_blank">查看详情</a></td>
                </tr>
        ''')

    f.write('''
            </table>
        </body>
    </html>
    ''')