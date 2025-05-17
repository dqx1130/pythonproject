class LinkNode:
    def __init__(self,x=None):
        self.data = x #数据域为x，不传参数默认为None
        self.next = None #指针域初始化为none，目前不知道接下来指向谁，需要下面的代码手动指定
#单链表型
class LinkList:
    #构造方法
    def __init__(self):
        self.head = LinkNode() #创建带头节点
        self.len = 0           #表长初始化为0
    #输出单链表
    def print(self):
        p = self.head.next #p是节点，是带头节点的next，是指向单链表的第一个有效节点
        #判断是否为空链表
        #是空的
        if p is None:
            print("空链表")
        #不是空的
        else:
            # 一直循环输出，直到p节点的指向为None为止
            while p.next is not None:
                #打印当前的节点data数据域和指向符号
                print(p.data,"->",sep = '',end = '')
                #更新节点为 上一个p指向的下一个节点
                p = p.next
            #指向None的节点在循环中并不会输出，因此需要单独输出该节点的data域
            print(p.data)

    # 尾插法创建单链法
    #a 是要传入的python列表
    #思路是将列表传入函数中，遍历列表中的元素，将其一个一个地插入单链表的尾部
    def createTail(self, a):
        #创建带头节点
        tail = self.head
        # 循环列表a的元素
        for each in a:
            #将每个遍历到的元素都创建数据域和指针域
            p = LinkNode(each)
            # 尾结点(目前暂时的)下一个节点指向刚刚的元素创建的节点（p）
            tail.next = p
            tail = p
            self.len += 1




h = LinkList()       #创建单链表（含带头结点）
a = list(map(int,input().split())) #输入数据到列表a
# 2025 0 3 15
h.createTail(a)     #尾插法创建单链表
h.print()           #输出单链表