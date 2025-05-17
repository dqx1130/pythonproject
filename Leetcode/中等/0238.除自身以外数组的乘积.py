class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]
        left = nums[0]
        for l in range(1,len(nums)):
            res.append(left)
            left = left * nums[l]
        right = 1
        for r in range(len(nums) - 1 , -1 , - 1):
            res[r] = res[r] * right
            right = right * nums[r]
        return res

a = Solution()
print(a.productExceptSelf([1,2,3,4]))
