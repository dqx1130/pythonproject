i = 2
while i < 10:
    j = 2
    while i > j:
        if i % j ==0 :
            print(i,"=",j,"*", i // j)
            break
        j += 1
    else:
        print(i,"是一个素数。")
    i += 1
