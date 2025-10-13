# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 

# Example 1:

# Input: s = "bcbbbcba"

# Output: 4

# Explanation:

# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
# Example 2:

# Input: s = "aaaa"

# Output: 2

# Explanation:

# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

# Constraints:

# 2 <= s.length <= 100
# s consists only of lowercase English letters.


class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0

        for i in range(len(s)):
            map_sub = {}
            for j in range(i, len(s)):
                k = s[j]
                map_sub[k] = map_sub.get(k, 0) + 1
                if map_sub[k] > 2:
                    break
                
                max_len = max(max_len, j - i + 1)

        return max_len
