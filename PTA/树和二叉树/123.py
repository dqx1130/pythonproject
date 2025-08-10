class Btree:
    def __init__(self,data= None):
        self.data = data
        self.left = None
        self.right = None

def create(pre,on):
    if len(pre) == 0:
        return None

    T = Btree(pre[0])
    m = on.index(pre[0])
    T.left = create(pre[1:m+1],on[0:m])
    T.right = create(pre[m+1:],on[m+1:])
    return T


def postOrder(T):
    if T is  None:
        return None
    postOrder(T.left)
    postOrder(T.right)
    print(T.data,end=' ')

def height(T):
    if T is None:
        return 0
    else:
        return 1 + max(height(T.left) , height(T.right))
# 9
# ABDFGHIEC
# FDHGIBEAC
n = int(input())
pre = input()
on = input()
Bt = create(pre,on)
print("Preorder:",end = " ")
postOrder(Bt)
print()
print(height(Bt))