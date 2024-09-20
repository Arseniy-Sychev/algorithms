'''
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Input: nums = [3,0,1]
Output: 2

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8

Input: nums = [0,1]
Output: 2
'''
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_num = {i for i in range(len(nums) + 1)}
        res = set(nums)
        result = list(set_num - res)
        return result[0]
    
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr_sum = sum(nums)
        res_sum = sum([i for i in range(len(nums) + 1)])
        return res_sum - curr_sum
    
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        overall_sum = sum(range(len(nums) + 1))
        return overall_sum - sum(nums)