i = 1
while i <= 9 :
    j = 9
    while j >= i:
        print(j,"*",i,"=",j*i,end=" ")
        j = j - 1
    print()
    i += 1
