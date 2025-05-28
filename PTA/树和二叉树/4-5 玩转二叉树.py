from collections import deque

class Btree:
    def __init__(self,x = None):
        self.data = x
        self.lchild = None
        self.rchild = None

def create(inOrder,preOrder):
    if len(preOrder) == 0:
        return None
    T = Btree(preOrder[0])
    m = inOrder.index(preOrder[0])
    T.lchild = create(inOrder[m+1:],preOrder[m+1:])
    T.rchild = create(inOrder[:m],preOrder[1:m+1])

    return T

def lay(T):
    global n
    if T is None:
        return None
    Q = deque()
    Q.append(T)
    while Q:
        tmp = Q.popleft()
        n -= 1
        if n != 0:
            print(tmp.data,end = " ")
        else:
            print(tmp.data,end = "")
        if tmp.lchild is not None:
            Q.append(tmp.lchild)
        if tmp.rchild is not None:
            Q.append(tmp.rchild)

# 7
# 1 2 3 4 5 6 7
# 4 1 3 2 6 5 7
n = int(input())
inOrder = list(input().split(" "))
preOrder = list(input().split(" "))

Bt = create(inOrder,preOrder)
lay(Bt)

