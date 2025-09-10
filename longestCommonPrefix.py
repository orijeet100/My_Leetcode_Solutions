# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        all_checked=False
        i=0
        ans=""
        while (True):
            if i==len(strs[0]):
                return ans
            first_char=strs[0][i]
            for j in range(1,len(strs)):
                if i==len(strs[j]) or strs[j][i]!=first_char:
                    return ans
            ans+=strs[0][i]
            i+=1
            

                 

        