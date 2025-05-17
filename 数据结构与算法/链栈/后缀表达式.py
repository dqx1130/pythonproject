import sys

class LinkNode:
    def __init__(self, x=None):
        self.data = x
        self.next = None

class LinkStack:
    def __init__(self):
        self.top = LinkNode()

    def push(self, x):
        p = LinkNode(x)
        p.next = self.top.next
        self.top.next = p

    def pop(self):
        assert self.top.next is not None
        value = self.top.next.data
        self.top.next = self.top.next.next
        return value

    def empty(self):
        return self.top.next is None

def calculate(expr: str) -> int:
    st = LinkStack()
    tokens = expr.strip().split()
    
    for token in tokens:
        if token in "+-*/%":
            # 弹出两个操作数
            b = st.pop()
            a = st.pop()
            # 进行计算
            if token == '+':
                st.push(a + b)
            elif token == '-':
                st.push(a - b)
            elif token == '*':
                st.push(a * b)
            elif token == '/':
                st.push(a // b)  # 整数除法
            elif token == '%':
                st.push(a % b)
        else:
            # 数字直接入栈
            st.push(int(token))
    
    return st.pop()

# 从标准输入读取数据直到EOF
for line in sys.stdin:
    if line.strip():  # 忽略空行
        try:
            result = calculate(line)
            print(result)
        except:
            print("表达式错误")