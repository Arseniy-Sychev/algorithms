'''
Given a binary array nums, return the maximum number 
of consecutive 1's in the array.

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits
are consecutive 1s. The maximum number of consecutive 1s is 3.
'''
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        r = 0
        