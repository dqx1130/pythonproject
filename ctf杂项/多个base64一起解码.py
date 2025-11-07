import base64

with open("C:/Users/mimo/Desktop/1.txt",'r') as file:
   for i in file.readlines():
      line=str(base64.b64decode(i),'utf8')
      print(line.replace("1"," "))
#replace("旧","新")