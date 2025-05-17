import time

class Exp:
    def __init__(self, n, ans=0, tm=0):
        self.n = n
        self.ans = ans
        self.tm = tm
    
    def solve1(self):
        for i in range(1, self.n + 1):
            tmp = 0
            for j in range(1, i + 1):
                tmp += j
            self.ans += tmp
        return self.ans
    
    def solve2(self):
        for i in range(1, self.n + 1):
            self.ans += i * (i + 1) // 2
        return self.ans
    
    def solve3(self):
        self.ans = self.n * (self.n + 1) * (self.n + 2) // 6
        return self.ans
    
    def print(self):
        start = time.time()
        print("结果：", self.solve1())
        end = time.time()
        self.tm = end - start
        print(f"用时：{self.tm:.30f}秒")  # 使用 f-string 格式化输出，保留 6 位小数

        start = time.time()
        print("结果：", self.solve2())
        end = time.time()
        self.tm = end - start
        print(f"用时：{self.tm:.30f}秒")  # 使用 f-string 格式化输出，保留 6 位小数

        start = time.time()
        print("结果：", self.solve3())
        end = time.time()
        self.tm = end - start
        print(f"用时：{self.tm:.30f}秒")  # 使用 f-string 格式化输出，保留 6 位小数

# 输入 n
n = int(input("请输入n："))
s = Exp(n)
s.print()  # 调用方法
