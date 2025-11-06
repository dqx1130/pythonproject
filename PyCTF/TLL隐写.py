with open('C:/Users/brighten/Desktop/attachment.txt', 'r') as f:    #打开
    for line in f:                                                  #按行读取
        num=int(line)                                               #文本转int
        ss=bin(num)                                                 #转2进制
        while len(ss)<10:
            ss=ss[:2]+'0'+ss[2:]
        print(ss)
