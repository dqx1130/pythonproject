nums = [2,1,-1]
i = 0
left = sum(nums[0:i])
right = sum(nums[i+1:len(nums)])
print(left,right)