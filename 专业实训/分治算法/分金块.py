def findMinMax(a,l,h):
    if l == h:
        return a[l],a[h]
    if h == l + 1:
        if a[l] > a[h]:
            return a[l] , a[h]
        else:
            return a[h] , a[l]
    m = (l + h) // 2
    lMax , lMin = findMinMax(a,l,m)
    rMax , rMin = findMinMax(a,m+1,h)
    mergeMax = max(lMax,rMax)
    mergeMin = min(lMin,rMin)
    return mergeMax , mergeMin

n = int(input())
gold = []
for i in range(n):
    gold.append(int(input()))
# print(gold)
goldMax , goldMin = findMinMax(gold,0,n-1)
print(f"{goldMax} {goldMin}")


# def findMinMax(a, low, high):
#     # 如果只有一个，那么既是最重又是最轻
#     if low == high:
#         return a[low], a[high]
#     # 如果有两个，比较大小
#     if high == low + 1:
#         if a[low] > a[high]:
#             return a[low], a[high]
#         else:
#             return a[high], a[low]
#
#     mid = (low + high) // 2
#     lMax, lMin = findMinMax(a, low, mid)
#     rMax, rMin = findMinMax(a, mid + 1, high)
#     mergeMax = max(lMax, rMax)
#     mergeMin = min(lMin, rMin)
#
#     return (mergeMax, mergeMin)