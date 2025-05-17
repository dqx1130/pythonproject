class CSqQueue:
    M = 5
    #构造函数
    def __init__(self):
        self.M = CSqQueue.M
        self.data = [None] * self.M
        self.front = 0
        self.rear = 0

    #入队,放进队尾
    def push(self,x):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.M
        self.data[self.rear] = x
        return True

    #出队，扔掉队首
    def pop(self):
        if self.isEmpty():
            return None
        self.front = (self.front + 1) % self.M
        return self.data[self.front]

    #取队首,不扔
    def getFront(self):
        if self.isEmpty():
            return None
        return self.data[(self.front + 1) % self.M ]

    #判空
    def isEmpty(self):
        if self.rear == self.front:
            return True
        return False

    #已满
    def isFull(self):
        if (self.rear + 1) % self.M == self.front:
            return True
        return False 

    def size(self):
        return (self.rear - self.front + self.M) % self.M

    def __len__(self):
        return self.size()

    def print(self):
        if self.isEmpty():
            print("队列为空")
            return
        print("队列：",end="")
        length = self.size()
        i = (self.front + 1) % self.M  # 从第一个元素开始
        while length > 0:
            print(self.data[i], end=' ')
            i = (i + 1) % self.M
            length -= 1
        print()

q = CSqQueue()
#连续入队测试
for i in range(6):
    if q.push(i):
        print(f"{i},入队成功")
    else:
        print(i,"队列已满")
print("队列元素个数",len(q))
#取队首
print("队首",q.getFront())
q.print()
#连续出队
for i in range(3):
    q.pop()
q.print()
#连续入队测试
for i in range(3):
    if q.push(i):
        print(f"{i},入队成功")
    else:
        print(i,"队列已满")
print("队列元素个数", len(q))
#取队首
print("队首",q.getFront())
q.print()



