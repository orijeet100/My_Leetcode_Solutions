# Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

# Example 1:

# Input: n = 987
# Output: "987"
# Example 2:

# Input: n = 1234
# Output: "1.234"
 

# Constraints:

# 0 <= n <= 231 - 1

class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        string_num=str(n)
        i=len(string_num)-1
        ans=""
        done=0
        while i>=0:
            if done!=0 and (done)%3==0:
                ans=string_num[i]+"."+ans
            else:
                ans=string_num[i]+ans
            done+=1
            i-=1

        return ans

        
