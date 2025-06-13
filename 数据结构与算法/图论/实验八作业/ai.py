from pythonds.basic import Queue

class Vertex:
    def __init__(self, num):
        self.id = num
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + " connectedTo: " + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        self.vis = set()

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self, n):
        return self.vertices.get(n)

    def __contains__(self, n):
        return n in self.vertices

    def addEdge(self, f, t, cost=0):
        if f not in self.vertices:
            self.addVertex(f)
        if t not in self.vertices:
            self.addVertex(t)
        self.vertices[f].addNeighbor(self.vertices[t], cost)

    def getVertices(self):
        return list(self.vertices.keys())

    # 输出邻接表
    def print(self):
        print("邻接表：")
        for i in self.vertices.keys():
            v = self.vertices[i]
            print(v.id, end="")
            for j in v.connectedTo.keys():
                print("->", j.id, end="")
            print()

    # 计算度数（适用于有向图）
    def degree(self):
        in_degrees = {k: 0 for k in self.vertices}
        out_degrees = {k: len(self.vertices[k].connectedTo) for k in self.vertices}

        for v in self.vertices.values():
            for nbr in v.connectedTo.keys():
                in_degrees[nbr.id] += 1

        print("顶点的度数（入度，出度）：")
        for k in self.vertices:
            print(f"{k}: 入度={in_degrees[k]}, 出度={out_degrees[k]}")

    # 深度优先搜索（单点出发）
    def dfs(self, st, d):
        self.vis.add(st)
        if d > 1:
            print(",", end="")
        print(st, end="")
        for v in self.vertices[st].connectedTo.keys():
            if v.id not in self.vis:
                self.dfs(v.id, d + 1)

    # 深度优先搜索（所有点）
    def dfsAll(self, st):
        self.vis = set()
        ls = list(self.vertices.keys())
        idx = ls.index(st)
        ls = ls[idx:] + ls[:idx]
        for v in ls:
            if v not in self.vis:
                self.dfs(v, 1)
                print()

    # 广度优先搜索（单点）
    def bfs(self, st):
        q = Queue()
        vis = set()
        q.enqueue(st)
        vis.add(st)
        while not q.isEmpty():
            vt = q.dequeue()
            print(vt, end=",")
            for v in self.vertices[vt].connectedTo.keys():
                if v.id not in vis:
                    q.enqueue(v.id)
                    vis.add(v.id)
        print()

    # 广度优先搜索（所有点）
    def bfsAll(self, st):
        vis = set()
        ls = list(self.vertices.keys())
        idx = ls.index(st)
        ls = ls[idx:] + ls[:idx]
        for v in ls:
            if v not in vis:
                q = Queue()
                q.enqueue(v)
                vis.add(v)
                while not q.isEmpty():
                    vt = q.dequeue()
                    print(vt, end=",")
                    for nb in self.vertices[vt].connectedTo.keys():
                        if nb.id not in vis:
                            q.enqueue(nb.id)
                            vis.add(nb.id)
                print()

# 示例用图
g = Graph()
g.addEdge('v1', 'v2')
g.addEdge('v2', 'v1')
g.addEdge('v2', 'v3')
g.addEdge('v3', 'v2')
g.addEdge('v3', 'v4')
g.addEdge('v4', 'v3')
g.addEdge('v4', 'v1')
g.addEdge('v1', 'v4')

# 打印邻接表
g.print()

# 打印度数
g.degree()

# 深度优先遍历（单点）
print("DFS from v1:")
g.vis = set()
g.dfs("v1", 1)
print()

# 深度优先遍历（全图）
print("DFS for all:")
g.dfsAll("v1")

# 广度优先遍历（单点）
print("BFS from v1:")
g.bfs("v1")

# 广度优先遍历（全图）
print("BFS for all:")
g.bfsAll("v1")
