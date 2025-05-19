def fib(n):
    a = [1,1]
    while True :
        if a[-1] >= n:
            a.pop()
            break
        a.append(a[-1]+a[-2])
    return a

n=int(input())
fiblist=fib(n)
print(fiblist)