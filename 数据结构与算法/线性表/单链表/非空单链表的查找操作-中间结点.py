class LinkNode:
    def __init__(self,x = None):
        self.data = x        #数据域data
        self.next = None     #指针域next初始化为空值None
#单链表类
class LinkList:
    #0.构造方法
    def __init__(self):
        self.head = LinkNode()  #创建带头结点
        self.n = 0              #表长初始化为0
    #1.输出单链表
    def print(self):
        p = self.head.next  #p指向链表的第一个有效结点
        if p is None:
            print("空链表")
        else:
            while p.next is not None:
                print(p.data,"->",sep = "",end = "")
                p = p.next
            print(p.data)
    #2.创建单链表-尾插法，细节不表
    def createTail(self,a):
        p = self.head
        for x in a:
            p.next = LinkNode(x)
            p = p.next
    #你的代码将被嵌在这里，注意整个方法的代码都要缩进4个空格（类里面的方法）
    #查找中间结点，返回指向中间结点的指针p
    def getMid(self):
        pass

h = LinkList() #创建单链表（含带头结点）
a = list(map(int,input().split())) #输入数据到列表a
h.createTail(a)     #尾插法创建单链表
p = h.getMid()      #查找中间结点
print(p.data)