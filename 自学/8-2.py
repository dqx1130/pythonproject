file = open(r'C:\Users\Administrator\Desktop\new.txt','r')
try:
    print(file.read())
finally:
    file.close()