def f(a,x,arr):
    res = 0
    for i in range(a,-1,-1):
        res = res + arr[i] * (x ** i)
    return f"{res:.3f}"
a , x = input().split()
a = int(a)
x = float(x)
arr = list(map(float,input().split()))
print(f(a,x,arr))