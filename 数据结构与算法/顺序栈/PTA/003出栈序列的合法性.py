'''
5 7 5
1 2 3 4 5 6 7
3 2 1 7 5 6 4
7 6 5 4 3 2 1
5 6 4 3 7 2 1
1 7 6 5 4 3 2
'''
from collections import deque
def valid(a,n,m):
    sq = deque()
    # b = [i for i in range (1,n+1)]
    for x in a:
        if x == sq[-1]:
            sq.pop()
        else:
            if cnt > n or len(sq) == m:
                return False
            for i in range(cnt + 1, x + 1):
                sq.pop()
        while True:
            if b[i] == x:
                break
            if len(sq) == m:
                return False
            sq.append(b[i])
        

