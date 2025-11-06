import random
import hashlib
value = "8b184b"
while 1:
    plainText = random.randint(10 ** 11, 10 ** 12 - 1)
    plainText = str(plainText)
    MD5 = hashlib.md5()
    MD5.update(plainText.encode(encoding='utf-8'))
    cipherText = MD5.hexdigest()
    if cipherText[-6:] == value:
        print("碰撞成功:")
        print("密文为:" + cipherText)
        print("明文为:" + plainText)
        break
    else:
        print("碰撞中.....")