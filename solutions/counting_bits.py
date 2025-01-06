class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # arr = [0]*(n+1)
        
        # for i in range(len(arr)):
        #     index = i
        #     number_of_ones = 0
        #     while(i !=0):
        #         if (i & 1) == 1:
        #             number_of_ones = number_of_ones + 1
        #         i = i >> 1
        #        # print(f"for index {index} we are now at value {i} and number of ones is {number_of_ones}")
        #     arr[index] = number_of_ones
        
        # return arr
        
        #DP
        
        arr =arr = [0]*(n+1)
        
        for i in range(len(arr)):
            arr[i] = arr[i>>1] + (i&1)
            
        return arr
                    