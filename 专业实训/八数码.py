from collections import deque

def get_next_states(state):
    # 获取0的位置
    zero_pos = state.index('0')
    row, col = zero_pos // 3, zero_pos % 3
    
    # 可能的移动方向：上、下、左、右
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    next_states = []
    
    for dx, dy in moves:
        new_row, new_col = row + dx, col + dy
        
        # 检查新位置是否有效
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            # 计算新位置在字符串中的索引
            new_pos = new_row * 3 + new_col
            # 创建新状态
            new_state = list(state)
            new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
            next_states.append(''.join(new_state))
    
    return next_states

def solve_puzzle(initial_state):
    target_state = "123804765"
    
    # 如果初始状态就是目标状态
    if initial_state == target_state:
        return 0
    
    # BFS队列和访问集合
    queue = deque([(initial_state, 0)])  # (状态, 步数)
    visited = {initial_state}
    
    while queue:
        current_state, steps = queue.popleft()
        
        # 获取所有可能的下一步状态
        for next_state in get_next_states(current_state):
            if next_state == target_state:
                return steps + 1
                
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, steps + 1))
    
    return -1  # 如果无法到达目标状态

def main():
    # 读取初始状态
    initial_state = input().strip()
    
    # 计算最少步数
    result = solve_puzzle(initial_state)
    print(result)

if __name__ == "__main__":
    main()