#批量文件重命名
import os
import re
import sys
def add_mark():
    pre = input("请输入要添加的前缀:")
    mark = "[%s]"%pre
    old_names = os.listdir()
    for old_name in old_names:
        if old_name != sys.argv[0]:
            os.rename(old_name,mark+old_name)

def remove_mark():
    oldnames = os.listdir()
    for oldname in oldnames:
        try:
            result = re.match(r"(^\[.*\])(.*)",oldname).group(2)
            rm = oldname

            if result:
                os.rename(oldname,result)
            print("已为%s移除前缀"%rm)

        except Exception as e :
            pass
def main():
    while True:
        option  = int(input("请选择功能数值:\n1.添加前缀\n2.删除前缀\n3.退出程序"))
        if option == 1:
            add_mark()
        elif option == 2:
            remove_mark()
        else:
            exit()

if __name__ == "__main__":
    main()