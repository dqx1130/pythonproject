import math
def funcos(eps,x):
    res = 0
    times = 0
    while True:
        tmp = x**(times*2)/math.factorial(times*2)
        if tmp < eps:
            break
        else:
            if times % 2 == 0:
                res += tmp
            else:
                res += tmp * (-1)
        times += 1
    return res

# eps,x=input().split()
# eps,x=float(eps),float(x)
eps = 0.0001 
x = -3.1
value=funcos(eps,x )
print("cos({0}) = {1:.4f}".format(x,value))