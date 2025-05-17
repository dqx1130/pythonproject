class CSqQueue:
    M = 5
    #构造
    def __init__(self):
        self.M = CSqQueue.M
        self.data = [None] * self.M
        self.front = 0
        self.rear = 0

    #入队
    def push(self,x):
        if self.isFull():
            return False
        self.rear = ( self.rear + 1 ) % self.M
        self.data[self.rear] = x
        return True

    #出队
    def pop(self):
        if self.isEmpty():
            return None
        self.front = (self.front + 1) % self.M
        return self.data[self.front]

    #取队首
    def getFront(self):
        if self.isEmpty():
            return None
        return self.data[(self.front + 1) % self.M ]


    #判空
    def isEmpty(self):
        if self.rear == self.front:
            return True
        return False

    #判满
    def isFull(self):
        if (self.rear + 1 ) % self.M == self.front:
            return True
        return False

    #看看长度
    def size(self):
        pass
    #用len
    def __len__(self):
        pass
    #输出队列
    def print(self):
        pass

q = CSqQueue()
for i in range(6):
    if q.push(i) :
        print(f"{i},成功入队")
    else:
        print(i,"队列已满")

