class sqStack:
    def __init__(self):
        self.data = []
    
    #入栈
    def push(self,x):
        self.data.append(x)
        
    #出栈
    def pop(self):
        if self.empty():
            return None
        return self.data.pop()
    
    #判断栈是否为空
    def empty(self):
        return len(self.data) == 0

    #取栈顶
    def getTop(self):
        if self.empty():
            return None
        return self.data[-1]
    
def valid(s):
    sq = sqStack()
    dic = {"}":"{","]":"[",")":"("}
    for c in s:
        #左括号入栈
        if c in "{[(":
            sq.push(c)
        #右括号出栈
        if c in ")]}":
            if sq.empty():
                return False
            x = sq.pop()
            if x != dic[c]:
                return False
    #判断栈是否为空
    if sq.empty():
        return True
    return False

s = input()
print("yes" if valid(s) else "no")

