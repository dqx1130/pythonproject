try:
    file = open(r"C:\Users\Administrator\Desktop\new1.txt","w")
    file.write("hello world!")
finally:
    file.close()
