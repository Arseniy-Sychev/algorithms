'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

'''
from typing import List

class Solution:
    def istarget(self, nums, target):
        l = 0
        r = len(nums) 
        while r - l > 1:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        return nums[l] == target

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if self.istarget(matrix[i], target):
                return True
        return False
    
class Solution:
    # time: O(log (N * M))
    # mem:  O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # чтобы работать с 2-D массивом как с 1-D
        def elementFromMatrix(i: int):
            n = len(matrix[0])
            return matrix[i // n][i % n]

        def good(i: int):
            return elementFromMatrix(i) <= target
        
        # обычный бинарный поиск как для 1-D массива
        l, r = 0, len(matrix) * len(matrix[0])
        while r - l > 1:
            m = (l + r) // 2
            if good(m):
                l = m
            else:
                r = m
        return elementFromMatrix(l) == target

