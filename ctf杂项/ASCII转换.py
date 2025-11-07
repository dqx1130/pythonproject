with open("C:/Users/mimo/Desktop/2.txt",'r') as f:
	data = f.readlines()
	for i in data:
		print(chr(int(i)),end="")
#需要竖着