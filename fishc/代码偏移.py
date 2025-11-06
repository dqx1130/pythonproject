# 给定的字符串 s 是按照如下规则存放的：它的偶数下标为小写英文字母，奇数下标为正整数。
# 题目要求：编写代码，将奇数下标的数字转换为相对于上一个字母偏移后的字母。
# 比如 s = "a1b2c3" 转换后的结果是 "abbdcf"（a1 -> ab，b2 -> bd，c3 -> cf）；
# s = "x7y8z9" 转换后的结果是 "xeygzi"（遇到最后字母 z ，则从 a 继续计算偏移）

s = input("请按规则输入一个字符串：")

length = len(s)
res = []
# 获取字母 a 的编码值
base = ord('a')

# 从第一个元素开始，每次迭代跳过一个元素
for i in range(0, length, 2):
    # ord(s[i]) - base 操作得到一个字母的偏移值，比如 b 就是 1
    # 跟 26 求余数的作用是防止溢出，循环计算偏移
    shift = chr((ord(s[i]) - base + int(s[i + 1])) % 26 + base)
    print(s[i] + shift, end="")