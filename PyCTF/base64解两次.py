import base64
result=[]
with open(r'flag.txt','r') as f:
    for line in f:
        result.append(line.strip('\n').split(','))
print(result)
        #文件读取，每一行，并存放在列表result中
print("--------------------------------------------------------------------------------")#分割
for a in result:
    print(a)
        #读取列表result中每一个的内容，并且放进列表
result2 = []
length = len(result)
for b in range(length):
    result2.append(str(base64.b64decode(result[b][0]),"utf-8"))
        #将result中的每一行进行base64解码，并存入列表result2（一维列表）中
for each in result2:
    print(each)
print("---------------------------------------------------------------------------------")#分割
result3=[]
length2 = len(result2)
for c in result2:
    print(base64.b64decode(c))
    result3.append(base64.b64decode(c))
        #二次base64解码，并将结果存入result3（一维列表）中
print("---------------------------------------------------------------------------------")#分割
for each in result3:
    print(each)
         #结果打印
