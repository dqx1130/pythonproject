#获得目录.exe文件
import glob
for line in glob.glob(r'D:\*.exe'):
    print(line)