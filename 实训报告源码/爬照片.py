import requests
from bs4 import BeautifulSoup
import os

# 定义要爬取的URL列表
urls = [
    "http://www.just.edu.cn/mxxq/list.htm",
    "http://www.just.edu.cn/zsxq/list.htm",
    "http://www.just.edu.cn/zjgxq/list.htm"
]

# 存储图片URL的列表
pic_urls = []

# 遍历每个URL
for url in urls:
    # 发送HTTP GET请求
    response = requests.get(url)
    # 设置响应的编码
    response.encoding = response.apparent_encoding
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')
    # 查找所有<img>标签
    img = soup.find_all('img')
    # 处理每个<img>标签
    for i in img:
        # 如果图片URL中包含'article'，则添加到pic_urls列表中
        if 'article' in i.get('src', ''):
            pic_urls.append(i['src'])

# 检查并创建保存图片的文件夹
if not os.path.exists('pic'):
    os.makedirs('pic')

# 打印所有图片URL
for each in pic_urls:
    print(each)

# 下载每张图片并保存到本地
for i in range(1, len(pic_urls) + 1):
    try:
        image_url = pic_urls[i - 1]
        if not image_url.startswith('http'):
            image_url = "http://www.just.edu.cn" + image_url  # 拼接完整URL

        # 发送HTTP GET请求获取图片内容
        image_data = requests.get(image_url).content

        with open(f'pic/{i:>02d}.jpg', 'wb') as f:
            f.write(image_data)
            print(f"第{i:>02d}张图片下载成功")
    except Exception as e:
        print(f"第{i:>02d}张图片下载失败: {e}")
