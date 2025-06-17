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
    #修改序号i（从0开始）的结点数据为x，修改成功返回True，结点不存在返回False。
    def update(self,i,x):
        if i < 0 or i >= self.n:
            return False
        now  = self.head.next
        for _ in range(i):
            now = now.next
        now.data = x
        return True


h = LinkList()       #创建单链表（含带头结点）
a = list(map(int,input().split())) #输入数据到列表a
h.createTail(a)     #尾插法创建单链表
print()
h.print()
i,x = map(int,input().split()) #输入要修改的结点序号i和修改后的结点数据x
if h.update(i,x):   #修改成功,输出更新后的单链表
    h.print()
else:               #结点不存在，输出Not Found
    print("Not Found")