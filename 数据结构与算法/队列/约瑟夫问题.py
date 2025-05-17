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

def josephus(n, k, m):
    q = CSqQueue()
    # 初始化队列，确保队列足够大
    while q.M <= n:
        q.M *= 2
        q.data = [None] * q.M
    # 将所有人入队
    for i in range(1, n+1):
        q.push(i)
    
    # 移动到起始位置k
    for _ in range(k-1):
        q.push(q.pop())
    
    result = []
    while not q.isEmpty():
        # 报数m-1次，将前面的人移到队尾
        for _ in range(m-1):
            q.push(q.pop())
        # 第m个人出队
        result.append(str(q.pop()))
    
    return ','.join(result)

# 测试样例
n, k, m = map(int, input().split())
print(josephus(n, k, m))