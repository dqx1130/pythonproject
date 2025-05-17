def partition(arr, low, high):
    pivot = arr[low]  # 选择第一个元素作为基准
    while low < high:
        # 从右向左找第一个小于基准的数
        while low < high and arr[high] >= pivot:
            high -= 1
        arr[low] = arr[high]
        
        # 从左向右找第一个大于基准的数
        while low < high and arr[low] <= pivot:
            low += 1
        arr[high] = arr[low]
    
    arr[low] = pivot  # 放置基准值
    return low

def quick_sort(arr, low, high):
    if low < high:
        # 找到基准位置
        pivot_pos = partition(arr, low, high)
        # 对基准左边的子序列进行快速排序
        quick_sort(arr, low, pivot_pos - 1)
        # 对基准右边的子序列进行快速排序
        quick_sort(arr, pivot_pos + 1, high)

def main():
    # 读取测试用例数量
    t = int(input())
    
    for _ in range(t):
        # 读取数组长度
        n = int(input())
        # 读取数组元素
        arr = list(map(int, input().split()))
        
        # 执行快速排序
        quick_sort(arr, 0, n-1)
        
        # 输出排序结果
        print(' '.join(map(str, arr)))

if __name__ == "__main__":
    main()