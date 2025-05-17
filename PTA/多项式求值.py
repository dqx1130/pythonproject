def f(n, x, *a):
    res = 0
    for i in range(n+1):
        res += a[i] * (x**i)
    return res

# n,x=input().split()
n = 3
x = 1.5
n=int(n)
x=float(x)
a=list(map(float,"2 11.3 3.5 -40".split()))
print(f(n,x,*a))