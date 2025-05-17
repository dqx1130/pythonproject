n = int(input())
nums = list(input().split())
#冒泡排序
for i in range(n-1,-1,-1):
    for j in range(0,i,1):
        # print(nums[j] + nums[j+1])
        # print(nums[j+1] + nums[j])
        if int(nums[j] + nums[j+1]) < int(nums[j+1] + nums[j]):
            nums[j] , nums[j+1] = nums[j+1],nums[j]
print(''.join(nums))

