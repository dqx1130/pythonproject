def isHd(n):
    list1 = []
    for each in str(n):
        list1.append(each)
    list1 = list(map(int, list1))
    # print(list1)
    listmax = list(map(str, (sorted(list1, reverse=True))))
    max = int(''.join(listmax))
    # print(max)
    listmin = list(map(str, (sorted(list1, reverse=False))))
    min = int(''.join(listmin))
    # print(min)
    if max - min == n:
        return True
    else:
        return False


n = int(input())
if isHd(n):
    print("yes")
else:
    print("no")