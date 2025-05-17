def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
        
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    for i in range(left, right + 1):
        arr[i] = temp[i]

def merge_sort(arr, temp, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, temp, left, mid)
        merge_sort(arr, temp, mid + 1, right)
        merge(arr, temp, left, mid, right)

def main():
    T = int(input())  # 测试数据组数
    
    for _ in range(T):
        n = int(input())  # 元素个数
        arr = list(map(int, input().split()))  # 读入数组
        
        # 创建临时数组
        temp = [0] * n
        
        # 执行归并排序
        merge_sort(arr, temp, 0, n-1)
        
        # 输出结果
        print(' '.join(map(str, arr)))

if __name__ == "__main__":
    main()