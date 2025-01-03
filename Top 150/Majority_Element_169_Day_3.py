class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_element = 0
        frequency = 0
        for num in nums:
            if frequency == 0:
                current_element = num
                frequency = 1
            elif num == current_element:
                frequency += 1
            else:
                frequency -= 1
        return current_element
