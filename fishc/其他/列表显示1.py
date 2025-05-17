nums = [2, 7, 11, 15]
target = 9
lenth = len(nums)
for i in range(0,lenth,1):
    for j in range(i,lenth,1):
        if target == nums[i] + nums[j]:
            list = nums[i] + nums[j]
            print([i,j])
###########################################
#给定一个整数列表 nums 和一个目标值 target，请在该数组中找出和为目标值的两个元素，并将它们的数组下标值打印出来。
#比如给定的列表 nums = [2, 7, 11, 15]，目标值 target = 9，那么由于 nums[0] + nums[1] = 2 + 7 = 9，所以打印结果是：[0, 1]
