# You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line. For any index i, nums[i] = [starti, endi] where starti is the starting point of the ith car and endi is the ending point of the ith car.

# Return the number of integer points on the line that are covered with any part of a car.

 

# Example 1:

# Input: nums = [[3,6],[1,5],[4,7]]
# Output: 7
# Explanation: All the points from 1 to 7 intersect at least one car, therefore the answer would be 7.
# Example 2:

# Input: nums = [[1,3],[5,8]]
# Output: 7
# Explanation: Points intersecting at least one car are 1, 2, 3, 5, 6, 7, 8. There are a total of 7 points, therefore the answer would be 7.
 

# Constraints:

# 1 <= nums.length <= 100
# nums[i].length == 2
# 1 <= starti <= endi <= 100


class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """

        nums=sorted(nums, key=lambda x: x[0])

        # print(nums)

        start=nums[0][0]
        end=max_element = max(max(row) for row in nums)

        n = end-start+1  # Desired size of the list
        my_list = [-1] * n

        for num in nums:
            for index in range(num[0],num[1]+1):
                # print(index)
                if my_list[index-start]==-1:
                    my_list[index-start]=1

        count=0
        for num in my_list:
            if num==1:
                count+=1

        return count


        
