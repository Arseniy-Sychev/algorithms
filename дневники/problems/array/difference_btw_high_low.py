'''
You are given a 0-indexed integer array nums, where 
nums[i] represents the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so 
that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.

Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.
'''
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        p1 = 0
        p2 = k - 1
        result = nums[-1] - nums[0]
        while p2 < len(nums):
            result = min(result, nums[p2] - nums[p1])
            p1 += 1
            p2 += 1
        return result
    