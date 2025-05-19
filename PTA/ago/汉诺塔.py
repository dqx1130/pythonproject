def hanoi(n,a,b,c):
    global step
    if n == 0:
        return
    hanoi(n-1,a,c,b)
    print(a,'->',c)
    step += 1
    hanoi(n-1,b,a,c)


n = int(input())
step=0
hanoi(n,'A','B','C')
print('共移动次数:',step)