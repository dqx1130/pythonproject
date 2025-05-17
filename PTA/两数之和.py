def judge(nums,want):
    if len(nums) <= 1:
        return "no answer"
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == want:
                return f"{i} {j}"
    return "no answer"

nums  = list(map(int,input().split(",")))
want = int(input())
# print(nums)
# print(want)
print(judge(nums,want))

