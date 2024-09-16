def rc4(data, key):
    # 初始化 s-box
    sbox = list(range(256))
    j = 0
    for i in range(256):
        j = (j + sbox[i] + key[i % len(key)]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]

    # 初始化加密变量
    i = j = 0
    out = []
    for char in data:
        i = (i + 1) % 256
        j = (j + sbox[i]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]
        out.append(char ^ sbox[(sbox[i] + sbox[j]) % 256])

    # 返回解密结果
    return ''.join([chr(b) for b in out])


# 测试代码
if __name__ == '__main__':
    ciphertext = b'U2FsdGVkX19uI2lzmxYrQ9mc16y7la7qc7VTS8gLaUKa49gzXPclxRXVsRJxWz/p'
    key = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = rc4(ciphertext, key)
    print(plaintext)

