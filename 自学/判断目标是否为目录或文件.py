# coding:gbk
import pathlib
path = 'D:\新建文件夹'
PATH = pathlib.Path(path)
print(PATH.is_dir())
print(PATH.is_file())
