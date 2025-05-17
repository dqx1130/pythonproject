class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        res = []
        index = (l - k) % l
        for _ in range(l):
            res.append(nums[index])
            index = (index + 1) % l
        for i in range(l):
            nums[i] = res[i]

nums = [-1,-100,3,99]
k =2
q = Solution()
print(q.rotate(nums,k))