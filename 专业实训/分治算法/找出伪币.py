def find(c,l,r):
    if r - l == 1 :
        return l
    m = l + (r - l)//2
    avgl = sum(c[l:m]) / len(c[l:m])
    avgr = sum(c[m:r]) / len(c[m:r])
    if avgl < avgr:
        return find(c,l,m)
    else:
        return find(c,m,r)

n = int(input())
coins = list(map(int,input().split()))
s = find(coins,0,len(coins))
print(s+1,coins[s])