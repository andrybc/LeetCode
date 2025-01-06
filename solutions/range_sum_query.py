class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        range_sum = 0
        for i in range(left, right+1):
            range_sum += self.nums[i]
        
        return range_sum