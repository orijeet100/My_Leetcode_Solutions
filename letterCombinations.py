# Medium
# Topics
# premium lock icon
# Companies
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


class Solution(object):

    


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        
        """
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        ans=[]


        if(len(digits)==0):
            return []


        def all_possible_2_list(s1,s2):
            all_pos=[]
            for i in range(0,len(s1)):
                for j in range(0,len(s2)):
                    all_pos.append(s1[i]+s2[j])

            return all_pos

        def combination(num):
            
            if(len(num)<=1):
                return [char for char in phone[num]]
            else:
                ans=all_possible_2_list(combination(num[:1]),combination(num[1:]))
            return ans

        return combination(digits)
        
