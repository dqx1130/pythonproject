import re

current_path = "C:/Users/槐序/PycharmProjects/ctf杂项/111/files/"
start = open(current_path + "start.txt","r")
zipfile = open("1.zip","wb")
content = start.read()
while True:
    num = re.findall(r"^[0-9]+",content)[0]
    zipfile.write((int(num)).to_bytes(2, byteorder = 'big'))
    filename = re.findall(r" ([A-Za-z0-9.]+)$",content)
    if filename:
        nextfile = open(current_path + filename[0],"r")
        content = nextfile.read()
        nextfile.close()
    else:
        break
print(content)
start.close()
zipfile.close()
#提取每个文本开头数字组成zip
