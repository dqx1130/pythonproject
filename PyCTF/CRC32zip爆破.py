import binascii
import zipfile
from zlib import crc32
import random

table = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890_!@#$%^&*()~`[]{};:,.<>?/'

def crc_4(content):
    for a in table:
        for b in table:
            for c in table:
                for d in table:
                    txt = str(a) + str(b) + str(c) + str(d)
                    crc = binascii.crc32(txt.encode())
                    if (crc & 0xFFFFFFFF) == content:
                        print(txt)

def crc_2(content):
    for a in table:
        for b in table:
            txt = str(a) + str(b)
            crc = binascii.crc32(txt.encode())
            if (crc & 0xFFFFFFFF) == content:
                print(txt)

# 爆破单个zip
def crc_1():
    s = "0123456789"
    text = ""
    f = zipfile.ZipFile(r"C:\Users\Administrator\Desktop\Misc-2-\level_1.zip")
    for i in range(0, 9999999999):
        data = str(i).zfill(10)
        # print(data,binascii.crc32(data.encode()))
        if hex(binascii.crc32(data.encode())) == '0x342f0e5c':
            print(data)
            break
    # 0009656856


#使用教程
# crc_4(0x7D90EE19)
# crc_2(0xA28E7734)
# crc_2(0x4394EE70)
crc_1()