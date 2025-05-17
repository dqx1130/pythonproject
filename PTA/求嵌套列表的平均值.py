def Avg(lst):
    res = []
    for each in lst:
        res.append(sum(each)/len(each))
    return res

lst= [[5],[1,2,3],[7,9,4]]
result = Avg(lst)
for value in result:
    print("{:.1f}".format(value),end=" ")