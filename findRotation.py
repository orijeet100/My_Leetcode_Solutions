# Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

 

# Example 1:


# Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
# Example 2:


# Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
# Output: false
# Explanation: It is impossible to make mat equal to target by rotating mat.
# Example 3:


# Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """

        size=len(mat)
        mat_new=mat

        def rotate_matrix():
            curr=copy.deepcopy(mat_new)
            for i in range(size):
                for j in range(size):
                    curr[j][size-i-1]=mat_new[i][j]
            return curr

        for _ in range(4):
                if mat_new==target:
                    return True
                mat_new=rotate_matrix()

        return False


        
