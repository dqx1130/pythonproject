def find_start(grid, h, w):
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '@':
                grid[i][j] = '.'  # 将起点标记为黑砖
                return i, j
    return -1, -1

def dfs(grid, x, y, h, w, visited):
    if (x < 0 or x >= h or y < 0 or y >= w or 
        grid[x][y] == '#' or visited[x][y]):
        return 0
    
    if grid[x][y] != '.':  # 只能在黑砖上移动
        return 0
        
    visited[x][y] = True
    count = 1
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        count += dfs(grid, new_x, new_y, h, w, visited)
    
    return count

def solve():
    # 读取宽度和高度
    w, h = map(int, input().split())
        
    # 读取网格
    grid = []
    for _ in range(h):
        grid.append(list(input().strip()))
    
    # 找到起点并计算结果
    start_x, start_y = find_start(grid, h, w)
    visited = [[False] * w for _ in range(h)]
    result = dfs(grid, start_x, start_y, h, w, visited)
    
    # 输出结果
    print(result)

if __name__ == "__main__":
    solve()