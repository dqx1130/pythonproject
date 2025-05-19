def polyvalue(lst,y):
    res = 0
    for i in range(len(lst)):
        res += lst[i]*(y**i)
    return res


# lst=eval(input())
# y=float(input())
lst = [1,3,0,0,9]
y=float("1")
print("{:.1f}".format(polyvalue(lst,y)))