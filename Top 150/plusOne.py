class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        integer = int(''.join(str(x) for x in digits))
        integer=str(integer+1)
        new_integer = [int(x) for x in list(integer)]
        return new_integer

        
