class actchoice:
    def __init__(self,time):
        self.time = time
        self.end = time[0][1]
        self.count = 1
    def choose(self):
        for each in self.time:
            if each[0] >= self.end:
                self.end = each[1]
                self.count += 1
                # print(self.end)
        print(self.count)
n = int(input())
time = []
for _ in range(n):
    a , b = map(int,input().split())
    tmp = [a,b]
    time.append(tmp)
time = sorted(time,key = lambda x:x[1] , reverse= False)
# print(time)
S = actchoice(time)
S.choose()