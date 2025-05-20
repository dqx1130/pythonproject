class BinaryTree:
    #1.构造方法
    def __init__(self,newValue):
        self.key = newValue     #树根
        self.left = None        #左子树初始化为空
        self.right = None       #右子树初始化为空
    #2.访问左子树
    def getLeft(self):
        return self.left
    #3.访问右子树
    def getRight(self):
        return self.right
    #4.修改树根的值
    def setRoot(self,newValue):
        self.key = newValue
    #5.访问树根的值
    def getRoot(self):
        return self.key

def createBT(T):
    pass
#统计二叉树结点个数
def  nodeCount(T):
    if T is None:
        return 0
    else:
        return 1 + nodeCount(T.left) + nodeCount(T.right)




# ABDFECGHI
# DBEFAGHCI

T = createBT()   #创建二叉树，实现细节不表
print(nodeCount(T)) #输出二叉树的结点数