from pickle import FALSE


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

    #在顺序表SeqList第i个位置（从1开始）前插入元素x。插入成功返回True，否则返回False。
    def insert(self,i,x):
        if i <= 0 or i > self.size+1:
            return False
        else:
            #如果位置不够，要先扩容
            if self.size + 1 >= self.capcity:
                self.__resize(self.capcity * 2)
            # 挪位置
            for k in range(self.size,i-1,-1):
                self.data[k] = self.data[k-1]
            #处理第i个位置
            self.data[i-1] = x
            self.size += 1
        return True




sq = SqList()   #创建顺序表
a = list(map(int,input().split())) #输入数据到列表a
i,x = map(int,input().split())    #输入插入位置i和元素x
sq.create(a)        #根据列表a整体创建顺序表sq
if sq.insert(i,x):   #位置i前插入元素x成功
    print("Insert Success")
    sq.print()
else:               #插入失败
    print("Insert Fail,Index is Error!")