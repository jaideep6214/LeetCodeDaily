class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_value = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        ans = ""
        for i in range(len(str(num))):
            numval = num%10
            val = numval*pow(10,i)
            num = num//10
            if numval in [4,9]:
                ans= roman_value[pow(10,i)] + roman_value[pow(10,i)+val]+ans
            else:
                if val in roman_value:
                    ans=roman_value[val]+ans
                elif numval in [2,3]:
                    ans=roman_value[pow(10,i)]*numval+ans
                elif numval in [6,7,8]:
                    ans=roman_value[5*pow(10,i)]+roman_value[pow(10,i)]*(numval-5)+ans
        return ans




