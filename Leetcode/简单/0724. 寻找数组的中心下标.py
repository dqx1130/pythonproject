class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1
        for i in range(len(nums)):
            left = sum(nums[0:i])
            right = sum(nums[i+1:len(nums)])
            if left == right:
                return i
        return res

a = Solution()
print(a.pivotIndex([1,7,3,6,5,6]))
