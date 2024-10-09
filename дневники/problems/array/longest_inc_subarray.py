'''
https://leetcode.com/problems/longest-continuous-increasing-subsequence/

Given an unsorted array of integers nums, return the length of
 the longest continuous increasing subsequence (i.e. subarray). 
 The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r 
(l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and 
for each l <= i < r, nums[i] < nums[i + 1].

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not 
continuous as elements 5 and 7 are separated by element

Input: nums = [2,2,2,2,2]
Output: 1
'''
from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 1
        curr_sum = 1
        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx - 1]:
                curr_sum += 1
            else:
                result = max(curr_sum, result)
                curr_sum = 1
        result = max(curr_sum, result)
        return result
    
class Solution:
    # time: O(n)
    # mem (дополнительная): O(1)
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        prev = float('-inf')
        max_length = 0 # максимальная длина возрастающей последовательности
        curr_length = 0 # текущая длина возрастающей последовательности
        for num in nums:
            # т к последовательности по условию не прерывающаяся
            # то мы на кажой итерации или увеличиваем ответ - если
            # приходит число больше чем предыдущее или делаем ответ 1
            # т к непрерывная возрастающая последовательности кончилась
            # и мы начинаем новую возрастающую последовательности
            if prev < num:
                curr_length += 1
            else:
                curr_length = 1
            max_length = max(max_length, curr_length) # на каждой итерации обновляем ответ
            prev = num
        return max_length