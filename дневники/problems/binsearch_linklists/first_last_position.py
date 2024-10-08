'''
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Input: nums = [], target = 0
Output: [-1,-1]
'''
from typing import List

class Solution:
    def first_target(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        l = -1
        while r - l > 1:
            mid = (r + l) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        return r if nums[r] == target else -1

    def last_target(self, nums: List[int], target: int) -> int:
        r = len(nums)
        l = 0
        while r - l > 1:
            mid = (r + l) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        return l if nums[l] == target else -1


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        l = self.first_target(nums, target)
        r = self.last_target(nums, target)
        return [l, r]