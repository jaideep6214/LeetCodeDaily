class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        if len(s) == 0:
            return True
        for character in t:
            if s[i]==character:
                i+=1
            if i == len(s):
                return True
        return False

             
        
