from numpy.ma.core import empty
class SqStack:
    def __init__(self):
        self.data = []

    #判断栈是否为空
    def empty(self):
        return len(self.data) == 0
    #取栈顶，成功返回栈顶，失败返回None，细节不表
    def getTop(self):
        if self.empty():
            return None
        return self.data[-1]
    #你的代码将被嵌在这里，注意整个方法的代码都要缩进4个空格（类里面的方法）
    #入栈
    def push(self,x):
        self.data.append(x)
    #出栈，成功返回栈顶，失败返回None
    def pop(self):
        if self.empty():
            return None
        tmp = self.data.pop()
        return tmp

str = input()           #输入字符串串
s = SqStack()           #定义顺序栈
for c in str:           #遍历字符串str
    if c.islower():     #小写字母入栈
        s.push(c)
while not s.empty():    #出栈
    print(s.pop(),end = " ")