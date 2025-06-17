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
        now = self.head
        for each in a:
            tmp = LinkNode(each)
            tmp.next = now.next
            now.next = tmp
            now = tmp
            self.n += 1

    #你的代码将被嵌在这里，注意整个方法的代码都要缩进4个空格（类里面的方法）
    #查找第一个值为x的结点，如果结点存在返回该结点的序号（从0开始），否则返回-1
    def findIndex(self,x):
        p = self.head.next
        noRes = -1
        index = 0
        while p is not None:
            if p.data == x:
                return index
            index += 1
            p = p.next
        return noRes

h = LinkList()       #创建单链表（含带头结点）
a = list(map(int,input().split())) #输入数据到列表a
h.createTail(a)     #尾插法创建单链表
h.print()
x = int(input())    #输入要查找的结点数据（从0开始）
i = h.findIndex(x)        #查找第一个值为x的结点
print(i)