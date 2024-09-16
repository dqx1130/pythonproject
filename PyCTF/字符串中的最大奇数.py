nums = input()
nums_list = []
for i in range(len(nums)):
    for j in range(len(nums)):
        # print(nums[i:j])
        if nums[i:j+1] != "":
            nums_list.append(nums[i:j+1])
print(nums_list)
tmp = 0
for each in nums_list:
    each = int(each)
    if each >= tmp and each % 2 == 1:
        tmp = each
        print(tmp)

print(tmp)