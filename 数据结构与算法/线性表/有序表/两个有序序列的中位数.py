class Sqlist:
    def __init__(self,M):
        self.capacity = M
        self.sqlist = [None] * self.capacity
        self.size = 0

    def __resize(self):
        newCapacity = self.capacity * 2
        oldSqList = self.sqlist
        newSqList = [None] * newCapacity
        for i in range(self.size):
            newSqList[i] =  oldSqList[i]
        self.sqlist = newSqList
        self.capacity = newCapacity

    def create(self,sqList):
        while self.capacity <= len(sqList):
            self.__resize()
        for i in range(len(sqList)):
            self.sqlist[i] = sqList[i]
            self.size += 1

    def __getitem__(self, i):
        assert 0 <= i < self.size
        return self.sqlist[i]

    def __setitem__(self, i, x):
        assert 0 <= i < self.size
        self.sqlist[i] = x

def fuck(A, B):
    target = A.size
    i, j = 0, 0  # i、j分别为A、B的索引
    count = 0     # 已合并元素的个数

    while i < A.size and j < B.size:
        if A[i] > B[j]:
            median = B[j]
            j += 1
        else:
            median = A[i]
            i += 1
        count += 1
        if count == target:  # 提前终止
            return median

    while i < A.size:
        median = A[i]
        i += 1
        count += 1
        if count == target:
            return median

    while j < B.size:
        median = B[j]
        j += 1
        count += 1
        if count == target:
            return median



n = int(input())
A = Sqlist(n)
A.create(list(map(int,input().split())))
B = Sqlist(n)
B.create(list(map(int,input().split())))
C = fuck(A,B)
print(C)





