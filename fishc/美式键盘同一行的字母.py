words = ["Twitter", "TOTO", "FishC", "Python", "ASL"]
res = []
for i in words:
    # 由于单词存在大小写，所以这里统一先转换为小写字母
    j = i.lower()
    # 灵活运用 strip() 方法，判断 j 是否所有字符都在键盘的同一行内
    if j.strip("qwertyuiop") == '' or j.strip("asdfghjkl") == '' or j.strip("zxcvbnm") == '':
        res.append(i)
print(res)