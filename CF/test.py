n = int(input())
for i in range(n):
    k = 9
    for j in range(n):
        if j < k -1:
            print(" ") 
        else:
            print("*")
        k -= 1
    print("\n")

