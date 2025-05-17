from collections import deque

def bfs(graph, n):
    # 初始化访问数组和结果列表
    visited = [False] * n
    result = []
    queue = deque()
    
    # 从顶点0开始遍历
    queue.append(0)
    visited[0] = True
    
    while queue:
        # 取出队首顶点并加入结果
        vertex = queue.popleft()
        result.append(vertex)
        
        # 遍历当前顶点的所有邻接点
        for i in range(n):
            # 如果有边相连且未访问过
            if graph[vertex][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True
    
    return result

def main():
    # 读取顶点数
    n = int(input())
    
    # 读取邻接矩阵
    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
    
    # 执行BFS遍历
    result = bfs(graph, n)
    
    # 输出结果
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()