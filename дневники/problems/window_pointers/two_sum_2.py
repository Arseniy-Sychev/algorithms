'''
Given a 1-indexed array of integers numbers that is already 
sorted in non-decreasing order, find two numbers such that they add up to a 
specific target number. Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one 
as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. 
You may not use the same element twice.

Your solution must use only constant extra space.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3]
'''
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            if numbers[p1] + numbers[p2] > target:
                p2 -= 1
                continue
            elif numbers[p1] + numbers[p2] < target:
                p1 += 1
                continue
            else:
                return [p1 + 1, p2 + 1]
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l < r:
            curr_sum: int = nums[l] + nums[r]
            # если текущая сумма равна target
            # -> возвращаем индексы пары чисел
            if curr_sum == target:
                return [l + 1, r + 1]
            # если текущая сумма больше target
            # -> сдвигаем правый указатель чтобы уменьшить общую сумму
            elif curr_sum > target:
                r -= 1
            # если текущая сумма больше target
            # -> сдвигаем левый указатель чтобы увеличить общую сумму
            else:
                l += 1
        
        return [-1, -1]
        