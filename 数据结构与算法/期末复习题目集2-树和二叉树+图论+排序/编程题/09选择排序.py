def choice(a):
    n = len(a)
    for i in range(n):
        flag = 0
        index = i
        for j in range(i+1,n):
            if a[j] < a[index]:
                index = j
                flag = 1
        if flag == 0:
            continue
        a[i] , a[index] = a[index] , a[i]

        print(*a)

n = int(input())
sqlist = list(map(int,input().split(" ")))
choice(sqlist)