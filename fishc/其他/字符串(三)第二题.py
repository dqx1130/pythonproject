#编写一个程序，判断输入的字符串是否由多个子字符串重复多次构成
s = input("请输入一个由字母构成的字符串：")
    
n = len(s)
for i in range(1, n//2+1):
# 如果子字符串的长度为i，则n必须可以被i整除才行
    if n % i == 0:
        # 如果子字符串的长度为i，则i到i*2之间是一个重复的子字符串
        if s.startswith(s[i:i*2]) and s.count(s[i:i*2]) == n/i:
            print(True)
            break
else:
    print(False)
    
#如果一个长度为 n 的字符串 s 可以由它的一个长度为 i 的子串 s’ 重复多次构成，
# 那么必须要满足以下条件：
# n 一定是 i 的倍数
# s' 一定是 s 的前缀子字符串
# n 除以 i 的结果必定是 s' 在 s 中出现的次数