class LinkNode:
    def __init__(self,x = None):
        self.data = x
        self.next = None

class LinkQueue:
    def __init__(self):
         self.front = LinkNode()
         self.rear = self.front
    
    def empty(self):
        return self.front.next == None
    
    def push(self,x):
        new_node = LinkNode(x)
        self.rear.next = new_node
        self.rear = new_node

    def pop(self):
        assert not self.empty()
        p = self.front.next
        self.front.next = p.next    
        return p.data
    
    def getFront(self):
        assert not self.empty()
        return self.front.next.data

    def getSize(self):
        cnt = 0
        p = self.front.next
        while p:
            cnt += 1
            p = p.next
        return cnt

q = LinkQueue()
for i in range(1,6):
    q.push(i)
while not q.empty():
    print(q.pop())    
    