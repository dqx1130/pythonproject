#利用字符串调用split()
s = "We are family"
print(s.split(' '))     #使用空格分割字符串，只要有空格就分割
print(s.split(' ',1))   #使用空格分割字符串，只分割一次
print(s.split('a',1))   #使用a分割字符串，分割一次
print(s.split('a',2))   #使用a分割字符串,分割两次