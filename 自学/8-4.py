#readline()方法读取文件
try:
    file = open(r'C:\Users\Administrator\Desktop\new.txt','r')
    while True:
        chunk = file.readline()
        print(chunk)
        if not chunk:
            break
finally:
    print(chunk)
#readlines()方法读取整个文件所有行，
# 保存在一个列表（list）变量中，每行作为一个元素，
# 但读取大文件时会比较占内存.