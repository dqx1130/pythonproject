class adjMaterixGraph:
    def __init__(self, n=0, m=0):
        # 初始化图的顶点数量和边数量
        self.n = n      # n个顶点
        self.m = m        # m个边
        self.vertex = []  # 存储顶点列表
        self.edge = [[0 for i in range(n)] for j in range(n)]  # 邻接矩阵初始化

    def print(self):
        # 打印图的基本信息和邻接矩阵
        print(f"顶点数:{self.n},边数:{self.m}")
        print(*self.vertex)
        # 打印邻接矩阵
        for i in range(self.n):
            for j in range(self.n):
                print(f"{self.edge[i][j] : < 5}", end="")
            print()

    def addVertex(self, ls):
        # 添加顶点列表
        self.vertex = ls

    def addEdge(self, fr, to):
        # 根据顶点名称查找索引并添加边
        ifr = self.vertex.index(fr)  # 获取起点索引
        ito = self.vertex.index(to)  # 获取终点索引
        # 设置邻接矩阵中对应的值为1，表示边存在
        self.edge[ifr][ito] = self.edge[ito][ifr] = 1

    def printDegree(self):
        # 打印每个顶点的度
        for i in range(self.n):
            degree = sum(self.edge[i])  # 每行加起来就是该点的度
            print(f"{self.vertex[i]} 的度是: {degree}")

# 主程序部分
n, m = map(int, input().split())  # 输入顶点和边的数量
g = adjMaterixGraph(n, m)  # 创建图对象
ls = input().split()  # 输入顶点信息
g.addVertex(ls)     #添加顶点信息进图
for _ in range(m):
    a, b = list(input())  # 输入边的信息
    g.addEdge(a, b)  # 添加边
g.print()  # 打印最终的邻接矩阵
g.printDegree()