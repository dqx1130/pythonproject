def prime(p):
    if p < 2 :
        return False
    for i in range(2,int(p**0.5)+1):
        if p % i == 0:
            return False
    return True

def PrimeSum(m,n):
    res = 0
    for i in range(m,n+1):
        if prime(i):
            res += i
    return res


m,n=input().split()
m=int(m)
n=int(n)
print(PrimeSum(m,n))
# print(prime(4))