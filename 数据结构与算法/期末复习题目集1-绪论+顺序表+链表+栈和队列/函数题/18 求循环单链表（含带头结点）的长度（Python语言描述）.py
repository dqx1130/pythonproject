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
    #1.输出循环单链表
    def print(self):
        p = self.head.next  #p指向链表的第一个有效结点
        if p is self.head:
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

    #3.创建循环单链表-头插法，细节不表
    def createHead(self,a):
        pass
    #4.你的代码将被嵌在这里，注意整个方法的代码都要缩进4个空格（类里面的方法）
#求循环单链表的长度，空表返回0
    def length(self):
        p = self.head.next
        res = 0
        while p is not self.head:
            p = p.next
            res += 1
        return res



h = CLinkList()   #创建单链表
a = list(map(int,input().split())) #输入数据到列表a
h.createTail(a)     #尾插法创建单链表
print(h.length())   #输出链表的长度