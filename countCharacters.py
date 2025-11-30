# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).

# Return the sum of lengths of all good strings in words.

 

# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

# Constraints:

# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# words[i] and chars consist of lowercase English letters.


class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """

        char_array=[0]*27
        for char in chars:
            index=ord(char)-97
            char_array[index]+=1
        ans=0
        for word in words:
            toAdd=True
            set_word=set(word)
            for char in set_word:
                if char_array[ord(char)-97]<word.count(char):
                    toAdd=False
                    break
                
            if toAdd==True:
                ans+=len(word)

        return ans
                
            

        
