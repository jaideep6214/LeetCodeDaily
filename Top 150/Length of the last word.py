class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        flag = False
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                count +=1
                flag = True
            else:
                if flag == True:
                    break
        return count

        #or you use
        # words = s.split()
        # return len(words[-1])
        

