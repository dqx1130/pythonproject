# 获得当前文件
import os
print(os.getcwd())                   #获取当前工作目录路径
print(os.path.abspath('.'))          #获取当前工作目录路径
print(os.path.abspath('test.txt'))   #获取当前目录文件下的工作目录路径
print(os.path.abspath('..'))         #获取当前工作的父目录！
print(os.path.abspath(os.curdir))    #获取当前工作目录路径

