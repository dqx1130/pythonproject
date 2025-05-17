from collections import deque

def get_position(pos):
    # 将棋盘坐标转换为数组下标
    col = ord(pos[0]) - ord('a')


    
    row = int(pos[1]) - 1
    return row, col

def is_valid(x, y):
    # 判断位置是否在棋盘内
    return 0 <= x < 8 and 0 <= y < 8

def knight_moves(start, end):
    # 马可以移动的八个方向
    directions = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    
    # 获取起点和终点的坐标
    start_row, start_col = get_position(start)
    end_row, end_col = get_position(end)
    
    # 如果起点和终点相同，直接返回0
    if (start_row, start_col) == (end_row, end_col):
        return 0
    
    # 使用BFS寻找最短路径
    visited = [[False] * 8 for _ in range(8)]
    queue = deque([(start_row, start_col, 0)])  # (行, 列, 步数)
    visited[start_row][start_col] = True
    
    while queue:
        row, col, steps = queue.popleft()
        
        # 尝试所有可能的移动
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # 检查新位置是否有效且未访问过
            if is_valid(new_row, new_col) and not visited[new_row][new_col]:
                # 如果到达目标位置，返回步数
                if new_row == end_row and new_col == end_col:
                    return steps + 1
                
                # 将新位置加入队列
                queue.append((new_row, new_col, steps + 1))
                visited[new_row][new_col] = True
    
    return 0  # 如果无法到达（实际上国际象棋棋盘上任意两点都是可达的）

# 处理输入
while True:
    try:
        start, end = input().split()
        moves = knight_moves(start, end)
        print(f"To get from {start} to {end} takes {moves} knight moves.")
    except EOFError:
        break