'''
https://leetcode.com/problems/monotonic-array/description/


An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Input: nums = [1,2,2,3]
Output: true

Input: nums = [6,5,4,4]
Output: true

Input: nums = [1,3,2]
Output: false
'''
from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # идея в том, что нам не важно монотонно возрастает массив
        # или монотонно убыват, поэтому мы заводим 2 флага:
        # на монотонное возрастание и на монотонное убывание
        is_inc = True
        is_dec = True
        for i in range(1, len(nums)):
            is_inc = is_inc and nums[i - 1] <= nums[i]
            is_dec = is_dec and nums[i - 1] >= nums[i]
        return is_inc or is_dec

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_inc = True
        is_dec = True
        
        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx - 1]:
                is_dec = False
            elif nums[idx] < nums[idx - 1]:
                is_inc = False
                      
        if (is_inc == True and is_dec == False) or (is_inc == False and is_dec == True) or (is_inc == True and is_dec == True):
            return True
        else:
            return False