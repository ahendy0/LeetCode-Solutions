class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        memo = [1] + [0]*target
        
        for i in xrange(1, target + 1):
            for num in nums:
                if i >= num:
                    memo[i] += memo[i - num]
                    
        return memo[-1]
            
            
