# #此脚本丢进kali
# 命令: python3 xxx.py

import os
import subprocess
from calendar import monthrange
import re

year = 2012
month = 1
day = 1

key = ""


def inttostr(a, n):
    ret = str(a)
    while len(ret) < n:
        ret = '0' + ret
    return ret


def getNextKey():
    global key
    global year
    global month, day
    if key == '20200101':
        return 0
    day = day + 1
    if day > monthrange(year, month)[1]:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    key = str(year) + inttostr(month, 2) + inttostr(day, 2)
    return 1


def main():
    # 创建 output 文件夹
    if not os.path.exists("output"):
        os.makedirs("output")

    while getNextKey():
        cmd = ["outguess", "-k", key, "-r", "Ziggs.jpg", "-t", f"./output/{key}.txt"]
        subprocess.run(cmd)

        # 读取输出文件并执行正则匹配
        with open(f"./output/{key}.txt", "r", encoding="latin1") as f:
            lines = f.readlines()
            for line in lines:
                if re.search(r"flag", line):
                    with open("flag.txt", "a", encoding="utf-8") as flag_file:
                        flag_file.write(line)


if __name__ == "__main__":
    main()