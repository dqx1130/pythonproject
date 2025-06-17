n = int(input())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
list2 = list2[:-1]

for each in list2:
    try:
        print(list1.index(each)+1,end = " ")
    except:
        print(0,end = " ")
