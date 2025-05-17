class LinkNode:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = LinkNode()
        self.head.next = None

    def print(self):
        p = self.head.next
        if p is None:
            print("空链表")
        else:
            while p.next is not None:
                print(p.data,"->",sep='',end='')
                p = p.next
            print(p.data)


    def createTail(self,a):
        assert len(a) > 0
        tail = self.head
        for each in a:
            p = LinkNode(each)
            tail.next = p
            tail = p

    def createHead(self,a):
        assert len(a) > 0
        for each in a:
            p = LinkNode(each)
            p.next = self.head.next
            self.head.next = p

    #查找链表第i个节点
    def get(self,i):
        assert i > 0
        p = self.head
        for k in range(i):
            p = p.next
            if p is None:
                print("第{}个节点是不存在".format(i))
                return p
        return p

    #输出第i个结点数据，支持[]操作符
    def __getitem__(self, i):
        p = self.get(i)
        if p is None:
            return None
        return p.data



# 测试程序
h = LinkList()  # 创建链表对象
h.createTail([1, 2, 3, 5, 7, 8, 12, 6])  # 使用尾插法创建链表
h.print()  # 打印链表：1->2->3->5->7->8->12->6
print(h[10])  # 尝试获取第10个结点（不存在，输出None）
# h.insert(1, 4)  # 在第1个位置插入4
# h.print()  # 打印链表：4->1->2->3->5->7->8->12->6
# h.createHead([10, 20, 30])  # 使用头插法创建链表
# h.print()  # 打印链表：30->20->10->4->1->2->3->5->7->8->12->6
# print(h.find(5))  # 查找元素5是否存在（存在，输出True）
# print(h.find(15))  # 查找元素15是否存在（不存在，输出False）
# h.pop(3)  # 删除第3个结点
# h.print()  # 打印链表：30->20->4->1->2->3->5->7->8->12->6
# h.set(2, 100)  # 修改第2个结点的数据为100
# h.print()  # 打印链表：30->100->4->1->2->3->5->7->8->12->6
# print(h.size())  # 输出链表长度（11）


