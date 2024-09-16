#判断是否是目录
import pathlib
path = r"D:\CTF"
PATH = pathlib.Path(path)
print(PATH.is_dir())

