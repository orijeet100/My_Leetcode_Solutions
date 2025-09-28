# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.
 

# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false
 

# Constraints:

# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.


class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """

        if len(s)!=len(goal):
            return False

        length=len(s)

        ans=[0 for _ in range(length)]

        j=0


        def checkEqual(s1,s2):
            for i in range(0,len(s1)):
                if s1[i]!=s2[i]:
                    return False

            return True

        while(j<length):

            for i in range(0,length):

                ans[i%length]=s[(i+j)%length]

            if checkEqual(ans,goal):
                return True            
            
            j+=1

        return False
        
