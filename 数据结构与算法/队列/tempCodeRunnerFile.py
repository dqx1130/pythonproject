class CSqQueue:
    M = 5
    #构造方法，初始化队列
    def __init__(self):
        #队列的元素
        self.data = [None] * CSqQueue.M
        #队首
        self.front = 0
        #队尾
        self.rear = 0
    
    #入队
    def push(self,x):
        if self.full():
            return False
        self.rear = (self.rear + 1) % CSqQueue.M
        self.data[self.rear] = x
        return True
    
    #出队,返回队首元素
    def pop(self):
        if self.empty():
            return None
        self.front = (self.front + 1) % CSqQueue.M
        return self.data[self.front]

    #取队首
    def getFront(self):
        if self.empty():
            return None
        return  self.data[(self.front + 1) % CSqQueue.M]

    #判断队列是否为空
    def empty(self):
        return self.rear == self.front
    
   #判断队列是否已满
    def full(self):
        return (self.rear + 1 ) % CSqQueue.M == self.front
    
    def size(self):
        return (self.rear - self.front + CSqQueue.M) % CSqQueue.M
    
    def __len__(self):
        return self.size()

#约瑟夫环，n个人围成一圈，编号为k的人从1开始报数，数到m的那个出列
def Josph(n,k,m):
    q = CSqQueue()
    a = []
    for i in range(1,n+1):
        q.push(i)
    #让编号为k的人变成队首
    for i in range(k - 1):
        q.push(q.pop())
    #出队n次
    for i in range(n):
        #从1开始报数，数到m的人变成队首
        for i in range(m - 1):
            q.push(q.pop())
        a.append(q.pop())
    print(*a,sep=",")
Josph(5,1,3)