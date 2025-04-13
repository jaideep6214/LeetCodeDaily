class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                water_trapped += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += max(0, right_max - height[right])
        #main logic is max(0, left_max - height[left])
        #you try to check max in left and right side
        #then you move from smaller side to largest
        #you try to calculate the water filled by the main logic
        #you do this till left and right indexes crosses
        return water_trapped
                    


            
