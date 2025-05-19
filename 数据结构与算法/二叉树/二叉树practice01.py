from collections import deque
class Btree:
    def __init__(self,x = None):
        self.data = x
        self.lchild = None
        self.rchild = None
def create(s):
    if s[0] == "#":
        s.pop(0)
        return None

    T = Btree(s[0])
    s.pop(0)
    T.lchild = create(s)
    T.rchild = create(s)
    return T

def preOrder(T):
    if T is None:
        return None
    print(T.data,end="")
    preOrder(T.lchild)
    preOrder(T.rchild)

def inOrder(T):
    if T is None:
        return None
    preOrder(T.lchild)
    print(T.data,end="")
    preOrder(T.rchild)
def postOrder(T):
    if T is None:
        return None
    preOrder(T.lchild)
    print(T.data,end="")
    preOrder(T.rchild)
def layerOrder(T):
    if T is None:
        return None
    Q = deque()
    Q.append(T)
    while Q :
        tmp = Q.popleft()
        print(tmp.data,end="")
        if tmp.lchild:
            Q.append(tmp.lchild)
        if tmp.rchild:
            Q.append(tmp.rchild)

def height(T):
    if T is None:
        return 0
    return 1 + max(height(T.lchild),height(T.rchild))
def printLeaf(T):
    if T is None:
        return None
    if T.lchild is None and T.rchild is None:
        print(T.data,end="")
    printLeaf(T.lchild)
    printLeaf(T.rchild)

T = create(list("ABD#E###CGH##I##F##"))
print("先序遍历：",end = "")
preOrder(T)
print("\n中序遍历：",end = "")
inOrder(T)
print("\n后序遍历：",end = "")
postOrder(T)
print("\n层次遍历：",end = "")
layerOrder(T)
print("\n二叉树的高度：",height(T))
print("二叉树的树叶：",end = "")
printLeaf(T)






