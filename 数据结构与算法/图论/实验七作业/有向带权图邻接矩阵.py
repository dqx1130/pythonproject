'''
6 9
v0 v1 v2 v3 v4 v5
v0 v1 5
v0 v5 2
v1 v2 4
v2 v3 9
v3 v4 7
v3 v5 3
v4 v0 1
v5 v2 1
v5 v4 8
'''
class adjMatrixGraph:
    INF = float("inf")
    def __init__(self,verNum,edgeNum):
        self.verNum = verNum
        self.edgeNum = edgeNum
        self.vertex = []
        self.edge = [[adjMatrixGraph.INF for i in range(verNum)] for j in range(verNum)]

    def addVertex(self,vertexInfoList):
        self.vertex = vertexInfoList
    def addEdge(self,start,end,value):
        col = self.vertex.index(start)
        row = self.vertex.index(end)
        self.edge[col][row] = value
    def inDegree(self):
        inDegree = [0 for i in range(self.verNum)]
        for i in range(self.verNum):
            for j in range(self.verNum):
                if self.edge[i][j] != adjMatrixGraph.INF:
                    inDegree[j] += 1
        return inDegree
    def outDegree(self):
        outDegree = [0 for i in range(self.verNum)]
        for i in range(self.verNum):
            tmp = 0
            for j in range(self.verNum):
                if self.edge[i][j] != adjMatrixGraph.INF:
                    tmp += 1
            outDegree[i] += 1
        return outDegree
    def print(self):
        for i in range(self.verNum):
            for j in range(self.verNum):
                print(f"{self.edge[i][j]: < 5}",end = "")
            print()

    def printDegree(self):
        inDegree = self.inDegree()
        outDegree = self.outDegree()
        for i in range(self.verNum):
            print(f"矩阵第{i+1}行,顶点：{self.vertex[i]},入度：{inDegree[i]},出度：{outDegree[i]},总度数：{inDegree[i]+outDegree[i]}")

verNum , edgeNum = map(int,input().split())
G = adjMatrixGraph(verNum,edgeNum)
vertexInfoList = input().split(" ")
G.addVertex(vertexInfoList)
for i in range(verNum):
    tmp = list(input().split(" "))
    start = tmp[0]
    end = tmp[1]
    value = int(tmp[2])
    G.addEdge(start,end,value)
print()
G.print()
G.printDegree()

