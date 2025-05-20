from collections import deque
class Btree:
    def __init__(self,x = None):
        self.data = x
        self.lchild = None
        self.rchild = None


def create(s):
    if s[0] == 0:
        s.pop(0)
        return None

    T = Btree(s[0])
    s.pop(0)

    T.lchild = create(s)
    T.rchild = create(s)
    return T

def findBoss(T):
    if T is None:
        return None
    Boss = 0
    Q = deque()
    Q.append(T)
    while Q:
        tmp = Q.popleft()
        if tmp.data > Boss:
            Boss = tmp.data
        if tmp.lchild is not None:
            Q.append(tmp.lchild)
        if tmp.rchild is not None:
            Q.append(tmp.rchild)

    return Boss
def findSidekick(T,Boss):
    if T is None:
        return None
    Q = deque()
    Q.append(T)
    while Q:
        tmp = Q.popleft()
        if tmp.data == Boss:
            if tmp.lchild is not None and tmp.rchild is not None:
                print(tmp.lchild.data,tmp.rchild.data)
            elif tmp.lchild is not None and tmp.rchild is None:
                print(tmp.lchild.data)
            elif tmp.lchild is None and tmp.rchild is not None:
                print(tmp.rchild.data)
            else:
                print("none")
            return
        if tmp.lchild is not None:
            Q.append(tmp.lchild)
        if tmp.rchild is not None:
            Q.append(tmp.rchild)
    return None

data = input().split()
s =  list(map(int,data))
T = create(s)
Boss = findBoss(T)
print(Boss)
findSidekick(T,Boss)