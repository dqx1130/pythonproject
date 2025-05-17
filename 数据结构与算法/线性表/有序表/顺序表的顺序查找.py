class Sqlist:
    M = 10
    def __init__(self):
        self.capacity = Sqlist.M
        self.size = 0
        self.sqlist = [None] * self.capacity

    def __resize(self):
        new_capacity = 2 * self.capacity
        oldSqlist = self.sqlist
        newSqlist = [None] * new_capacity
        for i in range(self.size):
            newSqlist[i] = oldSqlist[i]
        self.sqlist = newSqlist
        self.capacity = new_capacity

    def create(self, sqList):
        lenth = len(sqList)
        while self.capacity < lenth:  # 添加扩展逻辑
            self.__resize()
        for i in range(lenth):
            self.sqlist[i] = sqList[i]
            self.size += 1

    def find(self,wantFindList):
        indexList = []
        for each in wantFindList:
            if each == -1:
                break
            judge = 0
            for index in range(self.size):
                if each == self.sqlist[index]:
                    indexList.append(index+1)
                    judge = 1
                    break
            if not judge:
                indexList.append(0)
        return indexList

n = int(input())
sqList = list(map(int,input().split()))
wantFindList = list(map(int,input().split()))

sq = Sqlist()
sq.create(sqList)
res = sq.find(wantFindList)
for each in res:
    print(each,end=' ')

