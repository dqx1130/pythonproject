import sys
class Ten_to_R:
    map = {
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
    16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K',
    21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P',
    26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U',
    31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'
}
    def __init__(self):
        self.data = []
        self.r = None
        self.dec = None

    def inputR(self,r):
        self.r = r
    
    def inputDec(self,d):
        self.dec = d

    def empty(self):
        if len(self.data) == 0:
            return True
        return False

    def push(self,x):
        self.data.append(x)

    def pop(self):
        x = self.data.pop()
        return x
    
    def getTop(self):
        if not self.empty():
            return self.data[-1]
        else:
            return None

    def show(self):
        print(f"Struck:{self.data}")

    def calc(self):
        d = self.dec
        r = self.r
        res = ""
        if d == 0 :
            print("0")
            return
        while d > 0:
            t = d % r 
            if t >= 10:
                t = self.map.get(t,str(t))
            else:
                t = str(t)
            #压栈
            self.push(t)
            d //= r 
        #输出
        while not self.empty():
            x = self.pop()
            res += x
        print(res.lstrip("0"))


# d = 255
# r = 8
for line in sys.stdin:
    d , r = map(int,line.split())
    S = Ten_to_R()
    S.inputR(r)
    S.inputDec(d)
    S.calc()
