#二叉树的存储-二叉链表
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

#定义抽象类型队列Queue，FIFO（First In,First Out)
class Queue:
    #1.构造方法,定义一个空的列表
    def __init__(self):
        self.items = []
    #2.入队,队尾（列表尾部）入队
    def push(self,item):
        self.items.append(item)
    #3.出队，队首（列表头部）出队
    def pop(self):
        return self.items.pop(0)
    #4.判断队列是否为空
    def isEmpty(self):
        return self.items == []
    #5.取队首
    def getFront(self):
        return self.items[0]
    #6.求队列大小
    def getSize(self):
        return len(self.items)
# ABDFECGHI
# DBEFAGHCI
def createBT(T):
    pass
def layerOrder(T):
    if T is None:
        return None
    Q = Queue()
    Q.push(T)

    while Q.getSize() > 0:
        tmp = Q.pop()
        print(tmp.key,end = " ")
        if tmp.left:
            Q.push(tmp.left)
        if tmp.right:
            Q.push(tmp.right)



T = createBT()   #创建二叉树，实现细节不表
layerOrder(T)      #输出层次遍历

#你的代码将被嵌在这里
