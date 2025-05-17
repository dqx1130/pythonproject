class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.M = k + 1
        self.data = [None] * self.M
        self.front = 0
        self.rear = 0
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.rear = (self.rear +1 ) % self.M
        self.data[self.rear] = value                                                                                                                                                                                                                
        return True


    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.M
        return True
    
    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.data[(self.front + 1) % self.M]
           

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.data[self.rear]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.rear == self.front

    def isFull(self):
        """
        :rtype: bool
        """
        return (self.rear + 1) % self.M == self.front
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()