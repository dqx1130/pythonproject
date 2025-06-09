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
    def insertSorted(self,x):
        #扩容
        if self.size + 1 >= len(self.data):
            self.__resize(2 * len(self.data))
        # 寻找合适的位置
        k = 0
        while k < self.size:
            if x <= self.data[k]:
                break
            k += 1
        #移位
        for i in range(self.size,k,-1):
            self.data[i] = self.data[i-1]
        #改元素
        self.data[k] = x
        #改长度
        self.size += 1
        return k

"""
输入样例1：
输入共有2行，第1行表示顺序表的元素，第2行表示插入的元素

2 4 6
3
输出样例1：
输出最小插入位置（从0开始），按样例格式输出。

the Minimum Insertion Position is:1
the Length of SqList: 4
the Elements of SqList: 2 3 4 6
输入样例2：
输入共有2行，第1行表示顺序表的元素，第2行表示插入的元素

1 1 2 4 6
1
输出样例2：
输出最小插入位置（从0开始），按样例格式输出。

the Minimum Insertion Position is:0
the Length of SqList: 6
the Elements of SqList: 1 1 1 2 4 6
"""
sq = SqList()   #创建顺序表
a = list(map(int,input().split())) #输入数据到列表a
x = int(input())    #输入插入元素x
sq.create(a)        #根据列表a整体创建顺序表sq
k = sq.insertSorted(x)        #插入元素x，返回最小插入位置
print(f"the Minimum Insertion Position is:{k}")
sq.print()