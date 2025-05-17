class SqStruck:
    def __init__(self):
        self.data = []
    #判空
    def empty(self):
        return len(self.data) == 0
    #压栈
    def push(self,x):
        self.data.append(x)

    #出栈
    def pop(self):
        if self.empty():
            return None
        else:
            self.data.pop()
            return self.data[-1]
    
    #取栈顶
    def getTop(self):
        if self.empty():
            return None
        else:
            return self.data[-1]
    
    #看看你的
    def show(self):
        for x in self.data:
            print(x)

s = [1,2,3]
S = SqStruck()
for x in s:
    S.push(x)
S.show()
    


