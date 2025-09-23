import uuid
import random

# 1. 您之前提供的 SERVER_START_TIME
server_start_time = 1755260666.274804

# 2. 从服务器源码复制的 padding 函数
def padding(input_string):
    byte_string = input_string.encode('utf-8')
    if len(byte_string) > 6:
        byte_string = byte_string[:6]
    padded_byte_string = byte_string.ljust(6, b'\x00')
    padded_int = int.from_bytes(padded_byte_string, byteorder='big')
    return padded_int

# 3. 直接调用 uuid.uuid8 函数
target_username = 'admin'

print(f"[*] 使用种子: {server_start_time}")
random.seed(server_start_time)

padded_admin_int = padding(target_username)

# 直接调用您环境中已存在的 uuid.uuid8 函数
predicted_token = str(uuid.uuid8(a=padded_admin_int))

print("\n" + "="*40)
print(f"[*] 【最终正确版】预测的令牌:")
print(f"[*] Token: {predicted_token}")
print("="*40)