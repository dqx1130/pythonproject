from sympy.codegen.cnodes import sizeof


class SqList:
    #0.构造方法
    def __init__(self):
        self.initcapcity = 10            #初始容量
        self.capcity = self.initcapcity  #最大存储
        self.data = [None] * self.capcity#顺序表的数据，列表
        self.size = 0                    #顺序表的长度
    #0.顺序表的最大容量修改为n
    def __resize(self,n):
        assert n >= 0
        #备份原来的数据
        a = self.data
        self.data = [None] * n
        for i in range(self.size):
            self.data[i] = a[i]
        self.capcity = n
    #1.创建顺序表,数据源是列表a
    def create(self,a):
        for i in range(len(a)):
            if self.size == self.capcity:#顺序表满了，2倍扩容
                self.__resize(self.capcity * 2)
            self.data[i] = a[i]
            self.size += 1
    #2.输出顺序表
    def print(self):
        print("the Length of SqList:",self.size)
        print("the Elements of SqList:",*self.data[:self.size])

    #3.你的代码将被嵌在这里，注意整个方法的代码都要缩进4个空格（类里面的方法）
    # 在有序表SeqList的合适位置插入元素x，返回最小的插入位置
    def insertSorted(self, x):
        #如果位置不够，需要扩容1
        if self.size + 1 >= self.capcity:
            self.__resize(self.capcity * 2)
        index = 0
        # 挨个查找
        while index < self.size and self.data[index] < x:
            index += 1
        #后移位置
        for i in range(self.size,index-1,-1):
            self.data[i] = self.data[i - 1]
        self.data[index] = x
        self.size += 1
        return index


sq = SqList()   #创建顺序表
a = list(map(int,input().split())) #输入数据到列表a
x = int(input())    #输入插入元素x
sq.create(a)        #根据列表a整体创建顺序表sq
k = sq.insertSorted(x)        #插入元素x，返回最小插入位置
print(f"the Minimum Insertion Position is:{k}")
sq.print()