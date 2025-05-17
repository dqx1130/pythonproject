import sys
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
#括弧匹配
#判断括号序列s是否合法
def isValid(s):
    st = SqStack()
    #定义字典
    dic = {"{":"}","[":"]","(":")"}
    for c in s:
        if c in "([{":
            st.push(c)
        else:
            if st.empty():
                return False
            x = st.pop()
            #错误配对
            if dic[x] != c:
                return False
    return st.empty()


a = [1,2,3]
st = SqStack()
for x in a:
    st.push(x)
while not st.empty():
    print(st.pop())
for line in sys.stdin:
    print("Yes" if isValid(line[:-1]) else "No")