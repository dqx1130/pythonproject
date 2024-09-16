#判断是否是文件
import pathlib
path = "D:\CTF"
PATH = pathlib.Path(path)
print(PATH.is_file())