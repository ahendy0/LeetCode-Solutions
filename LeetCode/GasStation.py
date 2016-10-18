class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost) or not gas or not cost:
            return -1
        
        tank = 0
        start = 0
        for i, g in enumerate(gas):
            tank += g - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
            
        return start
                
            
