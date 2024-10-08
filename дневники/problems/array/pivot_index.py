'''
https://leetcode.com/problems/find-pivot-index/

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all
 the numbers strictly to the left of the index is equal to the sum of all 
 the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum 
is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

'''           
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0,]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        for idx in range(len(nums)):
            if prefix_sum[idx] == prefix_sum[-1] - prefix_sum[idx + 1]:
                return idx
        return -1
    
class Solution:
    # time: O(n)
    # mem(доп): O(1)
    def pivotIndex(self, nums: List[int]) -> int:
        # сумма всех элементов массива nums
        numsSum = sum(nums)

        # текущая сумма всех элементов слева
        leftSum = 0
        for i, num in enumerate(nums):
            # rightSum - сумма элементов справа
            # 0 1 2 3 4 5
            #     i
            # если i = 2, то leftSum = 0 + 1
            # rightSum = 3 + 4 + 5
            rightSum = numsSum - leftSum - num
            if leftSum == rightSum:
                return i
            leftSum += num
        return -1