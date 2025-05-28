class Vertex: #vertex：顶点
    def __init__(self, num):
        # 形参num: 顶点的标识符
        self.id = num  # 顶点的标识符
        self.connectedTo = {}  # 存储与该顶点相连的邻接点及其权重
    # 功能: 初始化一个顶点对象
    def addNeighbor(self, nbr, weight=0):
        # 形参nbr: 邻接点，weight: 连接的权重（默认为0）
        # 功能: 向该顶点添加一个邻接点及对应的权重
        self.connectedTo[nbr] = weight


class Graph: #graph：图
    # 功能: 初始化一个空图
    def __init__(self):
        self.vertices = {}  # 存储图中的所有顶点
        self.numVertices = 0  # 记录顶点数量


    # 功能: 创建并添加一个新的顶点到图中
    def addVertex(self, key):
        # 形参key: 新顶点的标识符
        self.numVertices = self.numVertices + 1  # 增加顶点计数
        newVertex = Vertex(key)  # 创建新顶点
        self.vertices[key] = newVertex  # 将新顶点加入图中
        return newVertex  # 返回新创建的顶点

    #在两个顶点之间建立一条带权重的连接
    def addEdge(self, f, t, cost=0):
        # 形参f: 边的起点，t: 边的终点，cost: 边的权重（默认为0）

        if f not in self.vertices:
            nv = self.addVertex(f)  # 若起点不存在，则添加起点
        if t not in self.vertices:
            nv = self.addVertex(t)  # 若终点不存在，则添加终点
        self.vertices[f].addNeighbor(self.vertices[t], cost)  # 在起点顶点中添加到终点的连接

    #输出邻接表
    def print(self):
        for i in self.vertices.keys():
            v = self.vertices[i]
            print(v.id,end = "")
            for j in v.connectTo.keys():
                print(f"->{j.id} {v.connectTo[j]}",end = "")
            print()

    #输出度
    def printDegree(self):
        a = []
        #出度
        for i in self.vertices.keys():
            v = self.vertices[i]
            n1 = len(v.connectTo.keys())
            print(f"{v.id} : {n1}")
        #入度
        b = [0] * self.numVertices
        for i in self.vertices.keys():
            for j in v.connectTo.keys():
                b[j.id] = b.get(j.id,0) + 1
        a.sort(key = lambda x:x[0])
        for x in a:
            k = x[0]
            print(f"{k}:{x[1]},{b.get(k,0)}")

n,m = map(int,input().split())
g = Graph



