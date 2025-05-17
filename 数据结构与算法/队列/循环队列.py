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
        return (self.front + 1) % CSqQueue.M

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
    

    
#队列测试
q = CSqQueue()
for i in range(1,6):
    if not q.push(i):
        print("队列已满，入队失败")
    else:
        print(f"{i},入队成功")
