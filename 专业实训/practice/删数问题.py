def delnum(n,s):
    for _ in range(s):
        if len(n) == 0:
            break
        i = 0
        while i < len(n) - 1 and n[i] <= n[i+1]:
            i =  i + 1
        n.pop(i)
    res = "".join(n).lstrip("0")
    if res:
        print(res)
    else:
        print("0")


n = list(input())
s = int(input())
delnum(n,s)