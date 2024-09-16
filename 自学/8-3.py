#read()方法读取文件
content = ""
try:
    file = open(r'C:\Users\Administrator\Desktop\new.txt','r')
    while True:
        chunk = file.read(5)
        print(chunk)
        if not chunk:
            break
        content += chunk
finally:
    print(content)
#在实例中设置read()方法每次读取5字节，从运行结果可以看出，
# 每次从文件中读取5字节的数据，然后打印出换行。但是如果文件中有中文时，
# 可能会出现乱码，因为中文字符占用两字节。