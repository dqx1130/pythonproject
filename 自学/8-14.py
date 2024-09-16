#删除多层目录
import os
CUR_PATH = ""
def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path,i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.rmdir(c_path)
del_file()