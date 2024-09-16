# coding:gbk
import os
import re
import sys

def add_mark():
    pre = input("��������Ҫ��ӵ�ǰ׺:")
    mark = "[%s]"%pre
    old_names = os.listdir()
    for old_name in old_names:
        if old_name != sys.argv(0):
            os.rename(old_name,mark+old_name)

def remove_mark():
    old_names = os.listdir()
    for old_name in old_names:
        try:
            result = re.match(r"(^\[.*\])(.*)",old_name).group(2)
            rm = old_name
            if result:
                os.rename(old_name,result)
            print("��Ϊ%s�Ƴ�ǰ׺"%rm)
        except Exception as e:
            pass

def main():
    while True:
        option = int(input("��ѡ������ֵ:\n1.���ǰ׺\n2.ɾ��ǰ׺\n3.�˳�����\n"))
        if option == 1:
            add_mark()
        if option == 2:
            remove_mark()
        if option == 3:
            exit()

if __name__ == "__main__":
    main()
