'''
https://leetcode.com/problems/range-sum-query-immutable/

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums
 between indices left and right inclusive where left <= right.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums
between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
'''
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        prefix_sum = [0,]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        self.prefix_sum = prefix_sum
        
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]