import zipfile
import os

now = "C:/Users/mimo/Desktop/1024.zip"       #压缩包地址

while 1:
    print("now zip: "+now, end='\t')
    zfile = zipfile.ZipFile(now)
    passFile=open(r"C:\Users\mimo\Desktop\工具\字典\0124全排列.txt") #先用0124全排列做字典(爆破用的字典)
    for line in passFile.readlines():
        try:
            password = line.strip('\n')
            zfile.extractall(members=zfile.namelist(), pwd=password.encode('utf-8'))
            zfile.close()
            try:
                os.remove(now)
            except OSError as e:
                print(e)
            names = os.listdir()
            print(names)
            for name in names:
                if name.endswith('.zip') and name != now:
                    now=name
                    break
            break
        except:
            pass


#适用于加密压缩包套娃，字典自己找