def getMode():
  while 1:
    print('请选择加密或解密模式：')
    print('加密e')
    print('解密d')
    mode = input()
    if mode in "e d".split(' ',1):
      return mode
    else:
      print("请重新输入：")
def getMessage():
  print('请输入要执行的信息：')
  return input()
def getKey():
  print("请输入密钥：")
  key = int(input())
  return key
def encrypt(mode,message,key):
  if mode == 'd':
    key = -key
  d = {}
  for c in (65, 97):
    for i in range(26):
      d[chr(i+c)] = chr((i+key) % 26 + c)
  print("结果为：")
  print("".join([d.get(c, c) for c in message])) #这里套用了this.py文件

mode = getMode()
message = getMessage()
key = getKey()
encrypt(mode,message,key)