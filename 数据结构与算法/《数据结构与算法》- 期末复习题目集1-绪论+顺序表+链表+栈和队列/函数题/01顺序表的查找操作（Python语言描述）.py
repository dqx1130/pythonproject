#顺序表
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

    #你的代码将被嵌在这里，注意整个方法的代码都要缩进4个空格（类里面的方法）
    #6.查询元素x第一次出现的序号，找不到返回-1
    def get(self,x):
        for i in range(self.n):
            if self.a[i] == x:
                return i
        return -1


'''
in:
2 0 2 5 0 3 0 9
0
out:
1
'''

A = SqList() #顺序表A
A.create(list(map(int,input().split())))    #输入第1行创建有序表A
x = int(input())        #输入查找元素x
print(A.get(x))         #输出x第一次出现的序号（找不到输出-1）