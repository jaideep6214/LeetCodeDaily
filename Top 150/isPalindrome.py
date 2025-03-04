class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        values=[]
        rev_values = []
   
        while (x!=0):
            values.append(x%10)
            rev_values = [x%10] + rev_values 
            x = x//10

        return values == rev_values
        
        # return str(x) == str(x)[::-1]
   
            
