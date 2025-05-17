import requests
from bs4 import BeautifulSoup

# URL 列表
urls = [
    "http://www.weather.com.cn/textFC/hb.shtml",
    "http://www.weather.com.cn/textFC/db.shtml",
    "http://www.weather.com.cn/textFC/hd.shtml",
    "http://www.weather.com.cn/textFC/hz.shtml",
    "http://www.weather.com.cn/textFC/hn.shtml",
    "http://www.weather.com.cn/textFC/xb.shtml",
    "http://www.weather.com.cn/textFC/xn.shtml"
]

# 存储所有天气数据的列表
weather_data = []

# 遍历每个 URL
for url in urls:
    # 获取网页内容
    responses = requests.get(url)
    responses.encoding = responses.apparent_encoding

    # 使用 BeautifulSoup 解析网页
    soup = BeautifulSoup(responses.text, 'html.parser')

    # 查找网页中的所有表格
    tables = soup.find_all('table')

    # 处理每个表格
    for table in tables:
        rows = table.find_all('tr')

        # 跳过表头行，通常表头行包含表格标题
        for row in rows[1:]:
            cols = row.find_all('td')

            # 如果列数符合预期，提取数据
            if len(cols) >= 5:
                date = cols[0].get_text(strip=True)  # 日期
                city = cols[1].get_text(strip=True)  # 城市
                max_temp = cols[2].get_text(strip=True)  # 最高气温
                min_temp = cols[3].get_text(strip=True)  # 最低气温

                # 添加到列表
                weather_data.append([date, city, max_temp, min_temp])

# 打印所有数据
for record in weather_data:
    print(record)

# 如果需要，将数据保存到文本文件
with open('weather_data_all.txt', 'w', encoding='utf-8') as f:
    for record in weather_data:
        f.write(",".join(record) + "\n")

print("天气数据已保存到 'weather_data_all.txt'")
