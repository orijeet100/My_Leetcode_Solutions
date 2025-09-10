# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution(object):

    def twoSum(self,nums, target,skip):

        pair_index={}

        ans=[]

        for i,num in enumerate(nums):
            if i==skip:
                continue
            if (target-num) in pair_index:
                ans.append([nums[i],nums[pair_index[(target-num)]]])
            pair_index[num]=i

        return ans


    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target=set()
        nums.sort()
        if nums[0]==nums[len(nums)-1] and nums[0] + nums[1] + nums[2] == 0:
            return [[nums[0],nums[1],nums[2]]]
        for index,i in enumerate(nums):
            ans=self.twoSum(nums,-i,index)
            if len(ans)!=0:
                for ele in ans:
                    ele.append(i)
                    ele.sort()
                    target.add(tuple(ele))
        return list(target)