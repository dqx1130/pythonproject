from PIL import Image

x = y = 200
img = Image.new("RGB",(x,y))
f = open("C:/Users/槐序/Desktop/qr.txt",'r')
for width in range(0,x):
    for height in range(0,y):
        line = f.readline().lstrip('(').rstrip(')\n')
        rgb = line.split(', ')
        img.putpixel((width,height),(int(rgb[0]),int(rgb[1]),int(rgb[2])))
img.save('flag.jpg')
#x和y为200是因为文件长度为40000=200×200
#转化为二维码

