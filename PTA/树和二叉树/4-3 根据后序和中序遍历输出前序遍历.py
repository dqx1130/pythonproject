
class Btree:
    def __init__(self,x = None):
        self.data = x
        self.lchild = None
        self.rchild = None

def create(onOrder,postOrder):
    if len(postOrder) == 0:
        return None
    T = Btree(postOrder[-1])
    m = onOrder.index(postOrder[-1])
    T.lchild = create(onOrder[0:m],postOrder[0:m])
    T.rchild = create(onOrder[m+1:],postOrder[m:len(postOrder) - 1])
    return T

def preOrder(T):
    if T is  None:
        return None

    print(T.data,end=' ')
    preOrder(T.lchild)
    preOrder(T.rchild)

# 7
# 1 2 3 4 5 6 7
# 2 3 1 5 7 6 4
n = input()
# onOrder = list("1 2 3 4 5 6 7".split(" "))
# postOrder = list("2 3 1 5 7 6 4".split(" "))

postOrder = list(input().split(" "))
onOrder = list(input().split(" "))
Bt = create(onOrder,postOrder)
print("Preorder:",end = " ")
preOrder(Bt)


