def frange(start ,stop = None , step = None): #非默认形参必须在默认形参之前
    s = str(step) #转字符串
    pre = len(s[s.find('.')+1:]) #字符串 ， 小数点的位置索引处+1的切片长度，就是小数点后的位数
    start += 0.0 #保证是浮点数

    if stop == None:
        stop = start + 0.0
        start = 0.0 #刷新start = 0 ，浮点数

    while stop < start :
        yield round(start,pre)
        start += step





for i in frange(1):
    print(i)
for i in frange(1,2):
    print(i)
for i in frange(5,10,0.5):
    print(i)