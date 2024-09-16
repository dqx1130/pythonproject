import hashlib
str = hashlib.md5()
str.update("hello!".encode("utf-8"))
result = str.hexdigest()
print(result)
