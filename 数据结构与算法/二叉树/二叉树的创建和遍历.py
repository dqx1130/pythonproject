from collections import deque
class Btree:
    def __init__(self, x = None):
        self.data = x       #结点数据域
        self.lchild = None  #左子
        self.rchild = None  #右子

#补空法创建树，根据给定的字符串s
def create(s):
    if s[0] == "#":
        s.pop(0)
        return None

    T = Btree(s[0])   #首字符是树根
    s.pop(0)
    T.lchild = create(s)     #递归创建左子
    T.rchild = create(s)     #递归创建右子
    return T

#先序遍历
def preOrder(T):
    if T is None:
        return
    print(T.data,end="")
    preOrder(T.lchild)
    preOrder(T.rchild)
#中序遍历
def inOrder(T):
    if T is None:
        return
    inOrder(T.lchild)
    print(T.data,end="")
    inOrder(T.rchild)
#后序遍历
def postOrder(T):
    if T is None:
        return
    postOrder(T.lchild)
    postOrder(T.rchild)
    print(T.data,end="")
#层次遍历
def layerOrder(T):
    q = deque()
    #1.树根入队
    q.append(T)
    #2.队列循环
    while len(q) > 0:
        p = q.popleft()
        print(p.data,end="")
        #左子入队
        if p.lchild:
            q.append(p.lchild)
        #右子入队
        if p.rchild:
            q.append(p.rchild)

def height(T):
    if T is None:
        return 0
    return 1 + max(height(T.lchild),height(T.rchild))

def printLeaf(T):
    if T is None:
        return
    if T.lchild is None and T.rchild is None:
        print(T.data, end="")
    printLeaf(T.lchild)
    printLeaf(T.rchild)

# T = create(list("ABD###CG##F##"))

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
