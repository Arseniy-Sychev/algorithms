from typing import List
'''
Given the array of integers nums, you will choose two different indices i and j of that array. 
Return the maximum value of (nums[i]-1)*(nums[j]-1).

Input: nums = [3,4,5,2]
Output: 12 
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return((nums[-1] - 1) * (nums[-2] - 1))
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = max(nums)
        nums.remove(m1)
        m2 = max(nums)
        return (m1 - 1) * (m2 - 1)
    
class Solution:
    # time: O(n)
    # mem: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        max_num = 0
        second_max_num = 0
        for num in nums:
            if num > max_num:
                second_max_num = max_num
                max_num = num
            else:
                second_max_num = max(second_max_num, num)
        
        return (max_num - 1) * (second_max_num - 1)