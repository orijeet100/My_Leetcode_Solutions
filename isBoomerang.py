# Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

# A boomerang is a set of three points that are all distinct and not in a straight line.

 

# Example 1:

# Input: points = [[1,1],[2,3],[3,2]]
# Output: true
# Example 2:

# Input: points = [[1,1],[2,2],[3,3]]
# Output: false
 

# Constraints:

# points.length == 3
# points[i].length == 2
# 0 <= xi, yi <= 100

class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """

        if (points[0][0] == points[1][0] and points[0][1] == points[1][1]) or (points[1][0] == points[2][0] and points[1][1] == points[2][1]) or (points[0][0] == points[2][0] and points[0][1] == points[2][1]):
            return False

        def slope(l1, l2):
            return float(l1[1] - l2[1]) / (l1[0] - l2[0]) if l1[0] - l2[0] != 0 else float('inf')


        return slope(points[1],points[0])!=slope(points[0],points[2])

        
