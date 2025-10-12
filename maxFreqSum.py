# You are given a string s consisting of lowercase English letters ('a' to 'z').

# Your task is to:

# Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
# Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.

# Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

# The frequency of a letter x is the number of times it occurs in the string.
 

# Example 1:

# Input: s = "successes"

# Output: 6

# Explanation:

# The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2.
# The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4.
# The output is 2 + 4 = 6.
# Example 2:

# Input: s = "aeiaeia"

# Output: 3

# Explanation:

# The vowels are: 'a' (frequency 3), 'e' ( frequency 2), 'i' (frequency 2). The maximum frequency is 3.
# There are no consonants in s. Hence, maximum consonant frequency = 0.
# The output is 3 + 0 = 3.
 

# Constraints:

# 1 <= s.length <= 100
# s consists of lowercase English letters only.


class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """

        v_map={}
        c_map={}
    

        for c in s:
            if c in 'aeiou':
                if c not in v_map:
                    v_map[c]=1
                else:
                    v_map[c]+=1

            else:
                if c not in c_map:
                    c_map[c]=1
                else:
                    c_map[c]+=1


        c_max=0
        v_max=0
        if c_map:
            c_max=max(c_map.values())

        if v_map:
            v_max=max(v_map.values())
 
        return  v_max + c_max

        
