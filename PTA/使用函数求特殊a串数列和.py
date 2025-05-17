def fn(a, n):
    if n == 0 :
        return 0
    #计算每个项
    res = 0
    for i in range(n,0,-1):
        res += a*(10**(i-1))
    return res + fn(a, n-1)


# a, b = input().split()
# s = fn(int(a), int(b))
s = fn(2,3)
print(s)