class LinkNode:
    def __init__(self,x = None):
        self.data = x        #数据域data
        self.next = None     #指针域next初始化为空值None
#单链表类
class CLinkList:
    #0.构造方法
    def __init__(self):
        self.head = LinkNode()  #创建一个带头结点
        self.head.next = self.head  #构成循环单链表
        self.n = 0                  #链表长度
    #1.输出循环单链表
    def print(self):
        p = self.head.next  #p指向链表的第一个有效结点
        if p is None:
            print("空链表")
        else:
            while p.next is not self.head:
                print(p.data,"->",sep = "",end = "")
                p = p.next
            print(p.data)
    #2.创建循环单链表-尾插法，细节不表
    def createTail(self,a):
        now = self.head
        for each in a:
            new = LinkNode(each)
            new.next = now.next
            now.next = new
            now = new
            self.n += 1
    #你的代码将被嵌在这里，注意整个方法的代码都要缩进4个空格（类里面的方法）
    #输出约瑟夫序列，数到m的出圈
    def Joseph(self,m):
        res = []
        while self.n > 0:
            p = self.head.next
            for _ in range(m):
                p = p.next
            res.append(p.next.data)
            p.next = p.next.next
            self.n -= 1
        print(*res)


h = CLinkList()   #创建循环单链表
n,m = map(int,input().split())    #n个小孩，数到m出圈
a = [i for i in range(1,n + 1)]   #列表a为前n个正整数
h.createTail(a)     #尾插法创建循环单链表
h.Joseph(m)
