class Btree:
    def __init__(self):
        pass
def create(strings):
    pass
def preOrder(T):
    pass
def inOrder(T):
    pass
def postOrder(T):
    pass
def layerOrder(T):
    pass
def height(T):
    pass
def printLeaf(T):
    pass

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
print("二叉树的树叶：")
printLeaf(T)






