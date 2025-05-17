n = input()
nums = list(n)
s = int(input())
for _ in range(s):
    if len(nums) == 0:
        break
    i = 0
    while i < len(nums) -1 and nums[i] <= nums[i+1]:
        i += 1
    nums.pop(i)
res = ''.join(nums).strip("0")
if res :
    print(res)
else:
    print('0')