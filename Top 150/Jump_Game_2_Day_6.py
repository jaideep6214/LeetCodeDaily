class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n == 1:  # No jumps needed if there's only one element
            return 0
        
        jumps = 0
        current_end = 0
        max_reach = 0
        
        for i in range(n - 1):  # Stop before the last index
            # Update the farthest index reachable
            max_reach = max(max_reach, i + nums[i])
            
            # If we've reached the end of the current jump range
            if i == current_end:
                jumps += 1
                current_end = max_reach  # Update the range for the next jump
                
                # If we've already reached or exceeded the last index
                if current_end >= n - 1:
                    break
        
        return jumps
