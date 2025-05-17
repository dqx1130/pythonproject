# 单链表的基本操作
# 单链表的结点（数据域和指针域）
class LinkNode:
    def __init__(self, x=None):
        self.data = x  # 数据域，存储结点值
        self.next = None  # 指针域初始化为空，指向下一个结点
# 单链表类
class LinkList:
    # 0.构造方法
    def __init__(self):
        self.head = LinkNode()  # 创建一个带头结点的空链表

    # 1.输出单链表
    def print(self):
        p = self.head.next  # p指向链表的第一个有效结点（跳过头结点）
        if p is None:
            print("空链表")
        else:
            while p.next is not None:  # 遍历到倒数第二个结点
                print(p.data, "->", sep="", end="")  # 打印当前结点数据和箭头
                p = p.next  # 移动到下一个结点
            print(p.data)  # 打印最后一个结点的数据（不加箭头）

    # 2.创建单链表-尾插法
    def createTail(self, a):
        assert len(a) > 0  # 确保输入列表不为空
        tail = self.head  # tail指向链表的头结点（初始时头结点就是尾结点）
        # 遍历列表a中的每个元素
        for x in a:
            # 根据x创建新结点
            p = LinkNode(x)
            # 新结点p链接到链表的尾部
            tail.next = p  # 当前尾结点的next指向新结点
            tail = p  # 更新尾结点为新结点

    # 3.创建单链表-头插法
    def createHead(self, a):
        assert len(a) > 0  # 确保输入列表不为空
        # 遍历列表a中的每个元素
        for x in a:
            # 根据x创建新结点
            p = LinkNode(x)
            # 新结点p链接到链表的头部
            p.next = self.head.next  # 新结点的next指向当前头结点的next
            self.head.next = p  # 头结点的next指向新结点

    # 4.查找第i个结点
    def get(self, i):
        assert i > 0  # 确保i是正整数
        p = self.head  # p从头结点开始
        for j in range(i):  # 循环i次找到第i个结点
            p = p.next  # 移动到下一个结点
            if p is None:  # 如果已经到链表末尾
                print("第%d个结点不存在" % i)
                return p  # 返回None表示不存在
        return p  # 返回找到的结点

    # 5.输出第i个结点数据，支持[]操作符
    def __getitem__(self, i):
        p = self.get(i)  # 调用get方法找到第i个结点
        if p is None:  # 如果结点不存在
            return None
        return p.data  # 返回结点的数据域

    # 6.查找x是否存在
    def find(self, x):
        p = self.head.next  # p从第一个有效结点开始
        while p is not None:
            if p.data == x:
                return True
            p = p.next
        return False

    # 7.插入操作，在第i个结点前插入数据域为x的新结点
    def insert(self, i, x):
        # 第1个结点前插入，特判一下
        if i == 1:
            p = self.head  # 插入位置的前驱结点是头结点
        # 1)找到第i-1个结点
        else:
            p = self.get(i - 1)  # 获取第i-1个结点作为前驱结点
        if p is None:  # 如果前驱结点不存在
            return False
        # 2)创建新结点，数据域为x
        q = LinkNode(x)
        # 3)插入新结点q
        q.next = p.next  # 先连：新结点的next指向原第i个结点
        p.next = q  # 后断：前驱结点的next指向新结点
        return True

    # 8.删除操作
    def pop(self, i):
        assert i > 0  # 确保i是正整数
        # 第1个结点前删除，特判一下
        if i == 1:
            p = self.head  # 删除位置的前驱结点是头结点
        # 1)找到第i-1个结点
        else:
            p = self.get(i - 1)  # 获取第i-1个结点作为前驱结点
        if p is None or p.next is None:  # 如果前驱结点不存在或第i个结点不存在
            return False
        # 2)删除第i个结点
        q = p.next  # q指向第i个结点
        p.next = q.next  # 前驱结点的next指向第i+1个结点
        return True

    # 9.修改操作
    def set(self, i, x):
        p = self.get(i)  # 获取第i个结点
        if p is None:  # 如果结点不存在
            return False
        p.data = x  # 修改结点的数据域
        return True

    # 10.链表的长度
    def size(self):
        p = self.head.next  # p从第一个有效结点开始
        length = 0
        while p is not None:
            length += 1
            p = p.next
        return length


# 测试程序
h = LinkList()  # 创建链表对象
h.createTail([1, 2, 3, 5, 7, 8, 12, 6])  # 使用尾插法创建链表
h.print()  # 打印链表：1->2->3->5->7->8->12->6
print(h[10])  # 尝试获取第10个结点（不存在，输出None）
h.insert(1, 4)  # 在第1个位置插入4
h.print()  # 打印链表：4->1->2->3->5->7->8->12->6
h.createHead([10, 20, 30])  # 使用头插法创建链表
h.print()  # 打印链表：30->20->10->4->1->2->3->5->7->8->12->6
print(h.find(5))  # 查找元素5是否存在（存在，输出True）
print(h.find(15))  # 查找元素15是否存在（不存在，输出False）
h.pop(3)  # 删除第3个结点
h.print()  # 打印链表：30->20->4->1->2->3->5->7->8->12->6
h.set(2, 100)  # 修改第2个结点的数据为100
h.print()  # 打印链表：30->100->4->1->2->3->5->7->8->12->6
print(h.size())  # 输出链表长度（11）