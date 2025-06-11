def insertSort(a):
    n = len(a)
    for i in range(1,n):
        j = i - 1
        t = a[i]
        #找合适的位置，不合适就后移
        while j >= 0 and t < a[j]:
            a[j+1] = a[j]
            j -= 1
        #元素插入
        a[j+1] = t
        #解包
        print(*a)

n = int(input())
sqlist = list(map(int,input().split(" ")))
insertSort(sqlist)
