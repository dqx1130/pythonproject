#readlines()方法读取文件
try:
    file = open(r"C:\Users\Administrator\Desktop\new.txt",'r')
    lines = file.readlines()
    print(type(lines))
    print(lines)
finally:
    file.close()