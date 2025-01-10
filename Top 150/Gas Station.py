class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        start_index = 0
        current_gas = 0
        for i in xrange(len(gas)):
            current_gas = current_gas + gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                start_index = i+1
        return start_index
