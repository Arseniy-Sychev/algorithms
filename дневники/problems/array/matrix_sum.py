'''
https://leetcode.com/problems/longest-continuous-increasing-subsequence/

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary
 diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

'''
from typing import List
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j:
                    result += mat[i][j]
                elif i == len(mat) - j - 1 and i != j:
                    result += mat[i][j]                
        return result