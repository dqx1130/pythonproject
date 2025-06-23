class adjMatrixGraph:
    # 构造方法，n个顶点m条边
    def __init__(self,n,m):
        self.verNum = n     #顶点数
        self.edgeNum = m    #边数
        self.vertex = [0] * n       #顶点列表
        self.edge = [[0 for i in range(self.verNum)] \
                     for j in range(self.verNum)]   #邻接矩阵二维列表
        self.vis = [False] * n     #顶点的访问列表，默认没访问过
    def addVertex(self,ls): #添加顶点列表
        self.vertex = ls
    def addEdge(self,fr,to):#添加边(fr,to)
        ifr = self.vertex.index(fr)     #起点下标
        ito = self.vertex.index(to)     #终点下标
        self.edge[ifr][ito] = self.edge[ito][ifr] = 1 #邻接矩阵

#邻接矩阵建图
def createGraph():
    n,m = map(int,input().split())  #输入n个顶点和m条边
    g = adjMatrixGraph(n,m)         #创建无向图G
    g.addVertex(list(input().split()))  #输入顶点列表
    for i in range(m):              #输入m条边
        fr,to = input().split()
        g.addEdge(fr,to)
    return g                        #返回无向图g

#输出无向图G每个顶点的度数
def printDegree(G):
    for i in range(G.verNum):
        print(f"{G.vertex[i]}:{sum(G.edge[i])}")

g = createGraph()   #创建无向图g
printDegree(g)      #输出g的度数
#你的代码将被嵌在这里