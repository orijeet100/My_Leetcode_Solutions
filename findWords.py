# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

 

# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]

# Output: ["Alaska","Dad"]

# Explanation:

# Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

# Example 2:

# Input: words = ["omk"]

# Output: []

# Example 3:

# Input: words = ["adsdf","sfd"]

# Output: ["adsdf","sfd"]

 

# Constraints:

# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase). 
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        r1="qwertyuiop"
        r2="asdfghjkl"
        r3="zxcvbnm"


        ans=[]

        for word in words:
            c1=0
            c2=0
            c3=0

            to_add=True

            for char in word.lower():
                if char in r1:
                    c1=1
                
                elif char in r2:
                    c2=1

                else:
                    c3=1

                if c1+c2+c3>1:
                    to_add=False
                    break

            # print(to_add)
            ans.append(word) if to_add else None

        return ans





        
