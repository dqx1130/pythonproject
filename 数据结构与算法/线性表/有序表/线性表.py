class SqList:
    #构造方法
    def __init__(self):
        #初始容量
        self.capacity = 10
        self.sqlist = [None] * self.capacity
        self.size = 0
    #扩容
    def resize(self,capacity):
        assert capacity > 0
        #扩2倍容量
        new_capacity = 2 * self.capacity
        #旧的顺序表备份
        old_sqlist = self.sqlist
        #创建新的顺序表
        new_sqlist = [None] * new_capacity
        #将数据存入新的顺序表中
        for i in range(self.size):
            new_sqlist[i] = old_sqlist[i]
        #更新self.sqlist
        self.sqlist = new_sqlist
        #更新容量大小
        self.capacity = new_capacity

    #缩容
    def downsize(self,capacity):
        assert capacity > 0
        #缩容1/2
        new_capacity = self.capacity // 2
                #旧的顺序表备份
        old_sqlist = self.sqlist
        #创建新的顺序表
        new_sqlist = [None] * new_capacity
        #将数据存入新的顺序表中
        for i in range(self.size):
            new_sqlist[i] = old_sqlist[i]
        #更新self.sqlist
        self.sqlist = new_sqlist
        #更新容量大小
        self.capacity = new_capacity

    #根据列表arr创建顺序表
    def create(self,arr):
        for i in range(len(arr)):
            #如果占满了，就扩容
            if self.size == self.capacity:
                self.resize(self.capacity)
            self.sqlist[i] = arr[i]
            self.size += 1

    #输出顺序表
    def print(self):
        print("顺序表的容量是：",self.capacity)
        print("顺序表的元素个数是：",self.size)
        print("顺序表：",self.sqlist)

    #查找一个元素x在顺序表里面的位置
    def find(self,x):
        for i in range(self.size):
            if self.sqlist[i] == x:
                print("元素",x,"的位置是:第",i+1,"个")

    #指定第i个位置插入一个元素x
    def insert(self,i,x):
        # 满了，没位置要扩容
        if self.size == self.capacity:
            self.resize(self.capacity)
        #从i-1到size-1的元素整体后移一个位置，插入元素x
        for j in range(self.size,i-1,-1):
            self.sqlist[j] = self.sqlist[j-1]
        self.sqlist[i-1] = x
        self.size += 1
    
    def delete(self,i):
        #空太多了，缩容
        if self.size * 4 <= self.capacity:
            self.downsize(self.capacity)
        for j in range(i-1,self.size-1):
            self.sqlist[j] = self.sqlist[j+1]
        #最后一个元素设置成None
        self.sqlist[self.size-1] = None
        self.size -= 1
        
           
sq = SqList()
sq.create([1, 2, 3, 4, 5,4365,123,5246,123,65346,457,895,234,134])
sq.print()
sq.insert(1,"a")
sq.print()


