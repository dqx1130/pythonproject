class fenpai:
    def __init__(self,n,pai):
        self.n = n
        self.pai = pai
        self.avg = sum(self.pai) // self.n
        self.step = 0
    def start(self):
        for i in range(self.n):
            if self.pai[i] == self.avg:
                continue
            self.pai[i+1] += self.pai[i] - self.avg
            self.step += 1
        print(self.step) 

n = int(input())
pai = list(map(int,input().split()))
S = fenpai(n,pai)
S.start()