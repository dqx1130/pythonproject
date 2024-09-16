from Crypto.Cipher import AES
import binascii
import zlib

key = b'748007e861908c03'

# 要解密的加密数据（十六进制形式）
encrypted_hex_data = "384bbb3ece28dd34875987e3a7516872bd976a6e0627a428ec520ea7e591c9b012b0bb631ebf97aa5449804e421b99c82fc1d2b3f9c38dacf824db8362e18f3638501b21cdcf427c6aed77e22dd1b90eb405e66d1cd7a10fb07dee0228f9afbbe615026487a14d3810472d75f64a14a11da6c3b037dba17f488cfeb4dcd7f9b0"

def decode(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(data)
    return decrypted_data

def ungzip(in_str):
    s = zlib.decompress(in_str, 16 + zlib.MAX_WBITS).decode()
    print("Decoded and Unzipped:\n", s)

# 将十六进制数据转换为字节序列
encrypted_bytes = bytes.fromhex(encrypted_hex_data)

# 解密数据并解压缩
decrypted_data = decode(encrypted_bytes, key)
ungzip(decrypted_data)
