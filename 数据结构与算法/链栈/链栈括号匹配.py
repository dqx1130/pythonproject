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
        self.top.next = self.top.next.next

    def getTop(self):
        assert self.top.next is not None
        return self.top.next.data

    def empty(self):
        return self.top.next is None

def isValid(s: str) -> bool:
    dc = {")": "(", "]": "[", "}": "{"}
    st = LinkStack()
    
    for c in s:
        if c in "([{":
            st.push(c)
        elif c in ")]}":
            if st.empty():
                return False
            if st.getTop() != dc[c]:
                return False
            st.pop()
    return st.empty()

# 从标准输入读取数据直到EOF
for line in sys.stdin:
    line = line.strip()  # 去除输入字符串的首尾空白
    print("yes" if isValid(line) else "no")