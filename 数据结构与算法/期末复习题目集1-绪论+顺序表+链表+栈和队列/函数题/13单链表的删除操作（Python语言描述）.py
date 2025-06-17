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
    #删除序号为i（从0开始）的结点，成功返回True，删除序号不合法返回False
    def erase(self,i):
        if i < 0 or i >= self.n:
            return False
        now = self.head
        for _ in range(i):
            now = now.next
        now.next = now.next.next
        return True

h = LinkList()       #创建单链表（含带头结点）
a = list(map(int,input().split())) #输入数据到列表a
h.createTail(a)     #尾插法创建单链表
i = int(input())    #输入要删除的结点序号（从0开始）
if h.erase(i):      #删除成功,输出插入后的单链表
    h.print()
else:               #结点不存在，输出Not Found
    print("Not Found")
