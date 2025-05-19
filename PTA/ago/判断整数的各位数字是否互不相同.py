def isdif(n):
    n = str(n)
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            return False
    return True


n=int(input())
if isdif(n):
    print("{}的各位数字互不相同".format(n))
else:
    print("{}的各位数字不是互不相同".format(n))