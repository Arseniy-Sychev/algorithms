'''
Given an integer array nums, move all 0's to the end of it while
 maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: nums = [0]
Output: [0]
[1, 3, 0, 0, 12]
       |
              |         

'''
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0
        while p2 < len(nums):
            if nums[p1] == 0 and nums[p2] == 0:
                p2 += 1
            elif nums[p1] == 0 and nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 += 1
            elif nums[p1] != 0:
                p1 += 1
                p2 += 1
class Solution:
    # time: O(n)
    # mem: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        # Note: задача может формулироваться как "удалить все 0 из массива"
        # тут смысл такой же, просто делаем resize в конце или попаем (зависит от ЯП)

        freeIdx = 0 # указывает на какую позицию поставим следующий элемент не равный 0
        for num in nums:
            if num == 0:
                continue
            nums[freeIdx] = num
            freeIdx += 1
        
        for i in range(freeIdx, len(nums)):
            nums[i] = 0

            
