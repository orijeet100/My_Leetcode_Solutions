# Given a circular array nums, find the maximum absolute difference between adjacent elements.

# Note: In a circular array, the first and last elements are adjacent.

 

# Example 1:

# Input: nums = [1,2,4]

# Output: 3

# Explanation:

# Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.

# Example 2:

# Input: nums = [-5,-10,-5]

# Output: 5

# Explanation:

# The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.

 


class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_diff=float('-inf')

        length=len(nums)
        for i in range(0,length):

            comp = abs(nums[i] - nums[0]) if i == length - 1 else abs(nums[i] - nums[i + 1])

            
            if comp>max_diff:
                max_diff=comp

        
        return max_diff
