'''
4 6
v1 v2 v3 v4
v1 v2
v1 v3
v1 v4
v2 v3
v2 v4
v3 v4

'''
from operator import index


class adjMatrixGraph:
    def __init__(self,verNum = 0,edgeNum = 0):
        self.verNum = verNum
        self.edgeNum = edgeNum
        self.vertex = []
        self.edge = [[0 for i in range(verNum)] for j in range(edgeNum)]
    def addVertex(self,vertexInfoList):
        self.vertex = vertexInfoList
    def addEdge(self,start,end):
        col = self.vertex.index(start)
        row = self.vertex.index(end)
        self.edge[col][row] = 1
    def print(self):
        for i in range(self.verNum):
            for j in range(self.verNum):
                print(f"{self.edge[i][j]: < 5d}",end = "")
            print()

    #统计入度
    def inDegree(self):
        inDegree = [0 for k in range(self.verNum)]
        for i in range(self.verNum):
            for j in range(self.verNum):
                if self.edge[i][j] == 1:
                    inDegree[j] += 1
        return inDegree
    #统计出度
    def outDegree(self):
        outDegree = [0 for k in range(self.verNum)]
        for i in range(self.verNum):
            tmp = sum(self.edge[i])
            outDegree[i] += tmp
        return outDegree

    def printDegree(self):
        inDegree = self.inDegree()
        outDegree = self.outDegree()
        for i in range(self.verNum):
            print(f"矩阵第{i+1}行,顶点：{self.vertex[i]},入度：{inDegree[i]},出度：{outDegree[i]},总度数：{inDegree[i]+outDegree[i]}")


verNum , edgeNum = map(int,input().split())
G = adjMatrixGraph(verNum,edgeNum)
vertexInfoList = list(input().split(" "))
G.addVertex(vertexInfoList)
for i in range(edgeNum):
    start , end = input().split(" ")
    G.addEdge(start,end)
G.print()
G.printDegree()
