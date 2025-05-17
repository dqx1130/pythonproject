def countPrime(n):
    # 创建一个布尔列表，初始时假设所有数都是质数
    prime = [True for i in range(n+1)]
    p = 2  # 从最小的质数2开始
    # 使用埃拉托斯特尼筛法标记非质数
    while p * p <= n:
        # 如果 prime[p] 没有被标记为 False，则它是一个质数
        if prime[p] == True:
            # 更新所有 p 的倍数为非质数
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1  # 检查下一个数

    count = 0  # 质数计数器
    # 从2到n-1遍历，统计质数的数量
    for p in range(2, n):
        if prime[p]:
            count += 1
    return count  # 返回质数的数量

n = int(input())  # 输入一个整数 n
print(countPrime(n))  # 输出小于 n 的质数数量