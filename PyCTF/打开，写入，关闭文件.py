file = open(r'C:\Users\23940\Desktop\123.txt', 'w+',encoding='utf-8')
for i in range(0,10000):
    file.write(str(i).zfill(4)+'\n')
    print(str(i).zfill(4)+'\n')
file.close()

