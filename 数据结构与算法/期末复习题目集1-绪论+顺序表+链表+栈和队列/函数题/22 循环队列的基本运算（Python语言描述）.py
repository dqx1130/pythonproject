class CSqQueue:
    M = 10          #最大容量，类属性
    #构造方法，初始化队列
    def __init__(self):
        self.data = [None] * CSqQueue.M  #队列的元素
        self.front = 0          #队首
        self.rear = 0           #队尾
    #3.取队首
    def getFront(self):
        if self.empty():
            return None
        return self.data[(self.front + 1) % CSqQueue.M]
    #4.判断队列是否为空
    def empty(self):
        return self.rear == self.front
    #5.判断队列是否已满
    def full(self):
        return (self.rear + 1) % CSqQueue.M == self.front
    # 你的代码将被嵌在这里，注意整个方法的代码都要缩进4个空格（类里面的方法）
    #入队，成功返回True，失败返回False
    def push(self, x):
        if self.full():
            return False
        self.data[self.rear] = x
        self.rear = (self.rear + 1) % CSqQueue.M
        return True


    #出队，成功返回队首，失败返回None
    def pop(self):
        if self.empty():
            return None
        tmp = self.data[self.front]
        self.front = (self.front + 1) % CSqQueue.M
        return tmp


n = int(input())
a = list(map(int,input().split()))
q = CSqQueue()
for x in a:
    if x != 0:
        if q.full():
            print('FULL',end = ' ')
        q.push(x)
    else:
        if q.empty():
            print('EMPTY',end = ' ')
        else:
            print(q.pop(),end = ' ')
print()
while not q.empty():
    print(q.pop(),end = ' ')