def sum(*args):
    res = 0
    for i in args:
        res += i
    return res


print(sum(1, 2))
print(sum(1, 2, 3))
