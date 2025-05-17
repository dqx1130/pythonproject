def try_compute(nums):
    if len(nums) == 1:
        return nums[0] == 24
    
    n = len(nums)
    # 尝试任意两个数的组合
    for i in range(n):
        for j in range(i + 1, n):
            a, b = nums[i], nums[j]
            # 将剩余的数字放入新列表
            remain = nums[:i] + nums[i+1:j] + nums[j+1:]
            
            # 尝试加法
            if try_compute(remain + [a + b]):
                return True
                
            # 尝试减法（两种顺序）
            if try_compute(remain + [a - b]):
                return True
            if try_compute(remain + [b - a]):
                return True
                
            # 尝试乘法
            if try_compute(remain + [a * b]):
                return True
                
            # 尝试除法（需要确保没有余数）
            if b != 0 and a % b == 0:
                if try_compute(remain + [a // b]):
                    return True
            if a != 0 and b % a == 0:
                if try_compute(remain + [b // a]):
                    return True
    
    return False

def main():
    while True:
        try:
            # 读取输入的四个数
            nums = list(map(int, input().split()))
            # 判断是否能得到24
            print("Yes" if try_compute(nums) else "No")
        except EOFError:
            break

if __name__ == "__main__":
    main()