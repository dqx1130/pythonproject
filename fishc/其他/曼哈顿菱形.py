n = 5  # 可以根据需要调整这个值

# 计算菱形的总宽度和高度
width = 2 * n - 1

# 打印菱形嵌入网格
for y in range(width):
    for x in range(width):
        # 计算当前点 (x, y) 到中心点 (n-1, n-1) 的曼哈顿距离
        manhattan_distance = abs(x - (n - 1)) + abs(y - (n - 1))

        # 如果曼哈顿距离小于等于 n-1，则打印星号；否则打印点
        if manhattan_distance <= n - 1:
            print('*', end='')
        else:
            print('.', end='')
    print()  # 换行
