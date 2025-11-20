# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0
 

# Constraints:

# 1 <= text.length <= 104
# text consists of lower case English letters only.

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        mapping={}

        for char in text:
            if char in mapping:
                mapping[char]+=1
            
            else:
                mapping[char]=1

        ans=10000

        if  mapping.get("l",0)<2 or mapping.get("o",0)<2:
            return 0
        
        mapping["l"]=mapping["l"]/2
        mapping["o"]=mapping["o"]/2
        for char in "balon":
            ans=min(ans,mapping.get(char,0))

        return ans
