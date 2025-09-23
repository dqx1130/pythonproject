import uuid

def padding(input_string):
    """
    将字符串转成长度为6字节，不足补0，超出截断，并转为整数（大端字节序）
    用于自定义uuid参数
    """
    byte_string = input_string.encode('utf-8')
    if len(byte_string) > 6:
        byte_string = byte_string[:6]
    padded_byte_string = byte_string.ljust(6, b'\x00')
    padded_int = int.from_bytes(padded_byte_string, byteorder='big')
    return padded_int

token = str(uuid.uuid8('admin'))
print(token)