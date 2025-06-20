from collections import deque
def valid(s,m):
    Q = deque()
    for each in s:
        if each == "S":
            if len(Q) == m:
                return False
            Q.append(each)
        else:
            if len(Q) == 0:
                return False
            Q.pop()
    return len(Q) == 0

n , m = map(int,input().split())
for _ in range(n):
    print("YES" if valid(input(),m) else "NO")
