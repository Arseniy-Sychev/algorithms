'''
https://leetcode.com/problems/rotate-array/

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''
from typing import List

class Solution:
    def rotateSubArr(self, nums: List[int], i: int, j: int):
        # nums - передается по ссылке
        # nums=[1, 2, 3, 4], i=1, j=3 -> [1, 3, 2, 4]
        j -= 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return nums

    def rotate(self, nums: List[int], k: int) -> None:
        # если есть массив [1, 2, 3] то сдвиг на 1 и сдвиг на 4 равны
        # и мы вместо того чтобы сдигать на 4 сдвигать хотим на 1
        k = k % len(nums)

        self.rotateSubArr(nums, 0, len(nums))
        self.rotateSubArr(nums, 0, k)
        self.rotateSubArr(nums, k, len(nums))