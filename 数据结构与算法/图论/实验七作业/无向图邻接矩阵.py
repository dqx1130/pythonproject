'''
无向图测试数据：
4 6
v1 v2 v3 v4
v1 v2
v1 v3
v1 v4
v2 v3
v2 v4
v3 v4
'''


class adjMatrixGraph:
    def __init__(self,verNum = 0,edgeNum = 0):
        # 顶点数和边数,不填形参默认为0
        self.verNum = verNum
        self.edgeNum = edgeNum
        #一维数组存顶点信息
        self.vertex = []
        #二维数组存边的信息
        #矩阵 : 顶点数×顶点数
        # 1 存在 ； 0 不存在
        self.edge = [[ 0 for i in range(verNum)] for j in range(verNum)]

    def print(self):
        #打印顶点数，边数，顶点信息，矩阵表
        print(f"顶点数：{self.verNum} 边数：{self.edgeNum}")
        print(*self.vertex)
        for i in range(self.verNum):
            for j in range(self.verNum):
                print(f"{self.edge[i][j] : < 5}",end = "")
            print()
    #写顶点信息,不填默认None
    def addVertex(self , vertexInfoList = None):
        self.vertex = vertexInfoList

    #矩阵填空，start→end，输入字符串，信息查找获取坐标
    # col列，row行
    #坐标 ：边[col][row]
    def addEdge(self,start,end):
        #矩阵，行列，索引相同，信息相同，
        col = self.vertex.index(start)
        row = self.vertex.index(end)
        #1 表示存在
        self.edge[col][row] = 1
        self.edge[row][col] = 1

    #打印每个顶点的度
    def printDegree(self):
        for i in range(self.verNum):
            tmp = sum(self.edge[i])
            print(f"矩阵第{(i+1)}行,顶点：{self.vertex[i]},对应的度数：{tmp}")


verNum , edgeNum = map(int,input().split())
vertexInfoList = list(input().split(" "))
G = adjMatrixGraph(verNum,edgeNum)
G.addVertex(vertexInfoList)
print()
print(f"顶点信息：{G.vertex}")
for _ in range(edgeNum):
    start , end = input().split()
    G.addEdge(start, end)

G.print()
G.printDegree()



