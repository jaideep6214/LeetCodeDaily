class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        for i in range(1,n):
            answer[i]=answer[i-1]*nums[i-1]
        
        right_products = 1
        for i in range(n-1,-1,-1):
            answer[i]=answer[i]*right_products
            right_products = right_products*nums[i]

        #[1,2,3,4]
        #[1,1,2,6]
        #[24,12,8,6]

        return answer
