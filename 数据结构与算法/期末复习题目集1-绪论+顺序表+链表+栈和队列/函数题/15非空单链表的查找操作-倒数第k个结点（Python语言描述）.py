class LinkNode:
    def __init__(self,x = None):
        self.data = x        #数据域data
        self.next = None     #指针域next初始化为空值None
#单链表类
class LinkList:
    #0.构造方法
    def __init__(self):
        self.head = LinkNode()  #创建带头结点
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

    #你的代码将被嵌在这里，注意整个方法的代码都要缩进4个空格（类里面的方法）
    # 查找倒数第k个结点，返回指向该结点的指针p，如果结点不存在，则返回空值None
    def getLastK(self, k):
        length = 0
        now = self.head
        while now.next is not None:
            length += 1
            now = now.next
        if  k <= 0 or k > length:
            return None
        res = self.head
        index = length - k + 1
        for _ in range(index):
            res = res.next
        return res
        
h = LinkList() #创建单链表（含带头结点）
a = list(map(int,input().split())) #输入数据到列表a
h.createTail(a)     #尾插法创建单链表
k = int(input())    #输入要查找的结点序号（从1开始）
p = h.getLastK(k)   #查找倒数第k个结点
if p:               #找到，输出该结点数据
    print(p.data)
else:               #找不到，输出Not Found
    print("Not Found")
