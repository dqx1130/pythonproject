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
    #2.创建单链表-尾插法
    def createTail(self,a):
        tail = self.head
        for each in a:
            p = LinkNode(each)
            tail.next = p
            tail = p
            self.n +=1
    #你的代码将被嵌在这里，注意整个方法的代码都要缩进4个空格（类里面的方法）
    #在序号为i（从0开始）的结点前插入一个新结点q（数据域为x），插入成功返回True，结点不存在返回False
    #在序号为i（从0开始）的结点前插入一个新结点q（数据域为x），插入成功返回True，结点不存在返回False
    def insert(self,i,x):
        if i < 0 or i > self.n:  # i大于n表示超过末尾
            return False
        p = self.head
        for _ in range(i):
            p = p.next
        q = LinkNode(x)
        q.next = p.next
        p.next = q
        self.n += 1
        return True

h = LinkList()       #创建单链表（含带头结点）
a = list(map(int,input().split())) #输入数据到列表a
h.createTail(a)     #尾插法创建单链表
i,x = map(int,input().split()) #输入插入的结点序号i和结点数据x
if h.insert(i,x):   #插入成功,输出插入后的单链表
    h.print()
else:               #结点不存在，输出Not Found
    print("Not Found")