class SqList:
    def __init__(self):
        self.initcapacity = 10
        self.capacity = self.initcapacity
        self.data = [None] * self.capacity
        self.size = 0

    def __resize(self, n):
        assert n >= 0
        a = self.data
        self.data = [None] * n
        for i in range(self.size):
            self.data[i] = a[i]

    def create(self, a):
        for i in range(len(a)):
            if self.size == self.capacity:
                self.__resize(self.capacity * 2)
            self.data[i] = a[i]
            self.size += 1

    def print(self):
        print("顺序表的长度是：", self.size)
        print("顺序表的元素是：", *self.data[:self.size])

    def findIndex(self, i):
        return self.data[i]

    def find(self, x):
        pass

    def set(self, i, x):
        self.data[i] = x

    def insert(self, i, x):
        assert 0 <= i <= self.size
        if self.size == self.capacity:
            self.__resize(2 * self.capacity)
        for j in range(self.size, i, -1):
            self.data[j] = self.data[j - 1]
        self.data[i] = x
        self.size += 1

    def erase(self, i):
        pass

    def sort(self):
        pass

    def insertSorted(self, x):
        pass

def mergeSorted(a, b):
    c = SqList()
    i = j = k = 0
    while i < a.size and j < b.size:
        if a.findIndex(i) < b.findIndex(j):
            c.insert(k, a.findIndex(i))
            i += 1
        else:
            c.insert(k, b.findIndex(j))
            j += 1
        k += 1
    while i < a.size:
        c.insert(k, a.findIndex(i))
        i += 1
        k += 1
    while j < b.size:
        c.insert(k, b.findIndex(j))
        j += 1
        k += 1
    return c

sq = SqList()
sq.create([1, 2, 3, 4, 5])
sq.print()
sq.insert(0, 6)
sq.print()
a = SqList()
b = SqList()
a.create([1, 3, 5, 7])
b.create([2, 4, 6, 8])
c = mergeSorted(a, b)
c.print()
