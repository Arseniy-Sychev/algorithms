'''
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        p1 = 0
        p2 = len(nums) - 1
        
        while p1 <= p2:
            if nums[p1] ** 2 < nums[p2] ** 2:
                result.append(nums[p2] ** 2)
                p2 -= 1
            else:
                result.append(nums[p1] ** 2)
                p1 += 1
        result.reverse()
        return result
         