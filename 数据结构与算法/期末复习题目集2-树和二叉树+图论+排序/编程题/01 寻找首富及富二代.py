class Btree:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

def Create(s):
    if s[0] == "0":
        s.pop(0)
        return None
    T = Btree(s[0])
    s.pop(0)
    T.left = Create(s)
    T.right = Create(s)
    return T

def



s = list(input().split(" "))




