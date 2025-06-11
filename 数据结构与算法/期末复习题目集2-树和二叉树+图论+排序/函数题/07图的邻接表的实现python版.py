class arcnode:
    def __init__(self,adjvex,weight,link=None):
        self.adjvex = adjvex
        self.weight = weight
        self.link=link

class vexnode:
    def __init__(self,data,first_arc=None):
        self.data = data
        self.first_arc = first_arc

class Graph:
    def __init__(self):
        self.vex_list=[]
        self.vex_num=0
        self.edge_num=0

    # 请在这里填写答案
    def addVertex(self, vex_val):
        v = vexnode(vex_val)
        self.vex_list.append(v)
        self.vex_num += 1

    # 请在这里填写答案
    def addEdge(self, f, t, cost=0):
        fr = self.vex_list[f]
        to = self.vex_list[t]
        fr.first_arc = arcnode(t,cost,fr.first_arc)
        to.first_arc = arcnode(f,cost,to.first_arc)

    def print_graph(self):
        for i in range(self.vex_num):
            print(self.vex_list[i].data,end="->")
            cur = self.vex_list[i].first_arc
            while cur:
                print("adj:{},weight:{}".format(cur.adjvex,cur.weight),end="->")
                cur = cur.link
            print('None')

if __name__ =="__main__":
    g = Graph()
    s =input()
    for vertex in s:
        g.addVertex(vertex)

    g.addEdge(0,1,11)
    g.addEdge(0,2,55)
    g.addEdge(2,3,88)
    g.addEdge(0,3,33)
    g.addEdge(1,2,44)
    g.print_graph()