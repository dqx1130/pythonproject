class Btree:
    def __init__(self,x = None):
        self.data = x
        self.lchild = None
        self.rchild = None

def create(s):
    if s[0] == "0":
        s.pop(0)
        return None

    T = Btree(s[0])
    s.pop(0)
    Btree.lchild = create(s)
    Btree.rchild = create(s)
    return T


s = list("30 15 0 0 70 33 0 35 34 0 0  0 50 0 0")
T = create(s)