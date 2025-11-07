import base64
file = open(r"C:\Users\mimo\Desktop\1024.txt",'r')
text = file.read()
while(1):
    try:
        text = base64.b32decode(text ).decode()
    except:
        try:
            text = base64.b64decode(text ).decode()
        except:
            try:
                text = base64.b16decode(text ).decode()
            except:
                print(text)
                break
#什么解码都使用，直到出现