def  sum_factor (n):
    list1 = []
    for i in range(1,n+1):
        for j in range(i,n+1):
            if i * j == n:
                list1.append(i)
                list1.append(j)
    set1 = set(list1)
    return sum(set1)

x=int(input())
sum = sum_factor(x)
print("{}的因子之和是{}".format(x,sum))