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
        pass

    #你的代码将被嵌在这里
    #合并2个有序链表（含带头结点）h1和h2
    def merge(h1,h2):
        h = LinkList()
        p1,p2,p = h1.head.next,h2.head.next,h
        while p1 and p2:
            if p1.data <p2.data:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return h


h1 = LinkList() #创建单链表h1（含带头结点）
h2 = LinkList() #创建单链表h2（含带头结点）
a = list(map(int,input().split())) #输入数据到列表a
b = list(map(int,input().split())) #输入数据到列表b
h1.createTail(a)     #尾插法创建单链表h1
h2.createTail(b)     #尾插法创建单链表h2
h = merge(h1,h2)     #合并2个有序链表（含带头结点）h1和h2
h.print()            #输出合并后的有序链表h