class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        actual_sum = sum(nums)
        supposed_sum = (n*(n+1))//2
        
        return supposed_sum - actual_sum