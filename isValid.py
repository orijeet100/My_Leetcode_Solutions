# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.




class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2!=0:
            return False

        map={
            '(':1,
            '{':2,
            '[':3,
            ')':-1,
            '}':-2,
            ']':-3,
        }

        open_brack=[]
        ans=0
        for char in s:
            if map[char]>0:
                open_brack.append(char)

            else:
                if len(open_brack)>0:
                    last_open=open_brack.pop()
                    if map[char]+map[last_open]!=0:
                        return False
            
            ans+=map[char]
            
        return len(open_brack)==0 and ans==0