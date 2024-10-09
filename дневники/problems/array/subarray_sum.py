'''
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, 
return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
Input: nums = [1,1,1], k = 2
Output: 2

Input: nums = [1,2,3], k = 3
Output: 2
'''
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_sum = {0: 1}
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in prefix_sum:
                result += prefix_sum[curr_sum - k]
            if curr_sum not in prefix_sum:
                prefix_sum[curr_sum] = 0
            prefix_sum[curr_sum] += 1
        
        return result