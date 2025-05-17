from collections import deque
def valid(s,m):
    sq = deque()
    for c in s:
        if c == "S":
            if len(sq) == m:
                return False
            sq.append(c)
        else:
            if len(sq) == 0:
                return False
            sq.pop()
    return len(sq) == 0
n,m = map(int,input().split())
for _ in range(n):
    print("Yes" if valid(input(),m) else "NO")
