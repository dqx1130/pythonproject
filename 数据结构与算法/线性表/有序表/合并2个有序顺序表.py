class SqList:
    M = 5                   #初始容量
    #1.构造方法
    def __init__(self):
        self.capcity = SqList.M         #最大容量
        self.n = 0                      #顺序表的长度初始化为0
        self.a = [None] * self.capcity  #顺序表的元素
    #2.修改容量
    def __resize(self,newCapcity):
        assert newCapcity > 0
        b = self.a                      #备份原来的数据
        self.a = [None] * newCapcity
        for i in range(self.n):
            self.a[i] = b[i]
        self.capcity = newCapcity       #更新顺序表的最大容量
    #3.根据列表a创建顺序表
    def create(self,a):
        for i in range(len(a)):
            if self.n == self.capcity:
                self.__resize(2 * self.n)
            self.a[self.n] = a[i]
            self.n += 1
    #4.输出顺序表
    def print(self):
        print("the Length of SqList:",self.n)
        print("the Elements of SqList:",*self.a[:self.n])
    #5.查询序号i的元素
    def getIndex(self,i):
        assert 0 <= i < self.n
        return self.a[i]
    #6.查询元素x第一次出现的序号，找不到返回-1，细节布标
    def get(self,x):
        pass
    #7.修改序号i的元素为x
    def set(self,i,x):
        assert 0 <= i < self.n
        self.a[i] = x
    #8.插入，在序号i的前面插入新的元素x,细节不表
    def insert(self,i,x):
        pass
    #9.删除，删除序号i的元素,细节不表
    def erase(self,i):
       pass
    #10.尾部添加元素x
    def add(self,x):
        self.insert(self.n,x)
    #11.重载[]，读操作
    def __getitem__(self, i):
        assert 0 <= i < self.n
        return self.a[i]
     #12.重载[]，写操作
    def __setitem__(self, i, x):
        assert 0 <= i < self.n
        self.a[i] = x

#你的代码将被嵌在这里
#合并2个有序表A和B，返回合并后的有序表C
def merge(A,B):
    i = 0
    j = 0
    new = []
    while i < A.n and j < B.n:
        if A[i] < B[j]:
            new.append(A[i])
            i += 1
        else:
            new.append(B[j])
            j += 1

    while i < A.n:
        new.append(A[i])
        i += 1

    while j < B.n:
        new.append(B[j])
        j += 1

    c = SqList()
    c.create(new)
    return c

A = SqList() #顺序表A
B = SqList()             #顺序表B
A.create(list(map(int,input().split())))    #输入第1行创建有序表A
B.create(list(map(int,input().split())))    #输入第2行创建有序表B
C = merge(A,B)          #合并有序表A和B为有序表C
C.print()               #输出有序表C