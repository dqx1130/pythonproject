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
    def erase(self,i):
        #检查
        if i < 1 or i > self.size:
            return False
        #改下标
        i -= 1
        #直接覆盖
        for k in range(i,self.size):
            self.data[k] = self.data[k+1]
        #最后一位置为none
        self.data[self.size - 1] = None
        #size
        self.size -= 1
        return True



'''
输入样例1：
输入共有2行，第1行表示顺序表的元素，第2行表示删除的位置

2 6 4
1
输出样例1：
删除成功，按样例格式输出。

Delete Success
the Length of SqList: 2
the Elements of SqList: 6 4
输入样例2：
输入共有2行，第1行表示顺序表的元素，第2行表示删除的位置

2 6 4
0
输出样例2：
删除失败，按样例格式输出。

Delete Fail,Index is Error!
'''
sq = SqList()   #创建顺序表
a = list(map(int,input().split())) #输入数据到列表a
i = int(input())    #输入删除位置
sq.create(a)        #根据列表a整体创建顺序表sq
if sq.erase(i):     #删除位置i的元素成功
    print("Delete Success")
    sq.print()
else:               #删除失败
    print("Delete Fail,Index is Error!")