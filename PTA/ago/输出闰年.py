def isLeap(y):
    if y % 100 == 0 and y % 400 != 0:
        return False
    if y % 400 == 0 or y % 4 == 0:
        return True
    else:
        return False

n = 0
for year in range(1900,2021):
    if isLeap(year)==True:
        print(year,end=' ')
        n+=1
        if n%5==0:print()