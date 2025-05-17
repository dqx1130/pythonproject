class SqStack:
    def __init__(self):
        self.data = []
    #入栈
    def push(self,x):
        self.data.append(x)
    #出栈
    def pop(self):
        if self.empty():
            return None
        x = self.data[-1]
        self.data.pop()
        return x
    #判断栈是否为空
    def empty(self):
        return len(self.data) == 0
    #取栈顶
    def getTop(self):
        if self.empty(): 
            return None
        x = self.data[-1]
        return x

a = [1,2,3]
st = SqStack()
for x in a:
    st.push(x)
while not st.empty():
    print(st.pop())