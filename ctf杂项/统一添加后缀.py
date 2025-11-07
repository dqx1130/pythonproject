import os

path = "C:/Users/槐序/Desktop/吹着贝斯扫二维码" #文件具体路径，这个1是那堆文件所在的文件夹，不成功时可以改个路径
for i in os.listdir("C:/Users/槐序/Desktop/吹着贝斯扫二维码"): #路径最好用绝对路径，不会出错
	#if i == '修改后缀.py':
	#	continue

	#else:
		oldname = os.path.join(path,i)
		newname = os.path.join(path,i+'.jpg')
		os.rename(oldname,newname)
