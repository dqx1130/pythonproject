class Btree:
    def __init__(self,x = None):
        self.data = x
        self.lchild = None
        self.rchild = None

def create(preOrder , inOrder):
    if len(preOrder)== 0:
        return None
    T = Btree(preOrder[0])
    m = inOrder.index(preOrder[0])
    T.lchild = create(preOrder[1 : m+1],inOrder[:m])
    T.rchild = create(preOrder[m + 1 :],inOrder[m+1:])
    return T

def getHeight(T):
    if T is None:
        return 0
    return 1 + max(getHeight(T.lchild),getHeight(T.rchild))

preOrder = list("ABDFGHIEC")
inOrder = list("FDHGIBEAC")
Bt = create(preOrder,inOrder)
print(getHeight(Bt))


