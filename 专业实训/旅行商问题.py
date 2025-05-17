def tsp(n, graph):
    INF = 10000000
    dp = {}
    
    # 初始状态：从节点1出发，已访问节点1
    for i in range(2, n+1):
        dp[(1 << 0 | 1 << (i-1), i)] = graph[1][i]
    
    # 遍历所有可能的状态
    for s in range(3, 1 << n):
        # 确保状态包含起点1
        if not (s & (1 << 0)):
            continue
        
        for curr in range(2, n+1):
            if not (s & (1 << (curr-1))):
                continue
            
            prev_s = s ^ (1 << (curr-1))
            min_dist = INF
            
            # 遍历所有可能的前一个节点
            for prev in range(1, n+1):
                if prev != curr and (prev_s & (1 << (prev-1))):
                    if (prev_s, prev) in dp:
                        dist = dp[(prev_s, prev)] + graph[prev][curr]
                        min_dist = min(min_dist, dist)
            
            if min_dist != INF:
                dp[(s, curr)] = min_dist
    
    # 计算最终结果：所有节点都访问后返回起点1
    final_state = (1 << n) - 1
    result = INF
    
    # 从最后一个节点返回起点1
    for last in range(2, n+1):
        if (final_state, last) in dp and graph[last][1] != INF:
            total_dist = dp[(final_state, last)] + graph[last][1]
            result = min(result, total_dist)
    
    return result if result != INF else 10000000

def main():
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        
        # 初始化图
        graph = [[10000000] * (n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            graph[i][i] = 0
        
        # 读取边的信息
        for _ in range(m):
            u, v, w = map(int, input().split())
            graph[u][v] = w
            graph[v][u] = w
        
        # 计算最短路径
        result = tsp(n, graph)
        print(result)

if __name__ == "__main__":
    main()