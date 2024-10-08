'''
https://leetcode.com/problems/daily-temperatures/

Given an array of integers temperatures represents the daily temperatures,
 return an array answer such that answer[i] is the number of days you have 
 to wait after the ith day to get a warmer temperature. 
 If there is no future day for which this is possible, keep answer[i] == 0 instead.

 
 Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input: temperatures = [30,60,90]
Output: [1,1,0]
'''
from typing import List

class Solution:
    # time: O(n)
    # mem: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        # в стеке всегда храним убывающую последовательность
        # например: [[1, 20], [3, 8], [5, 1]]
        # [1, 20] -> в 1 день температура была 20
        stack = []
        for i, temperature in enumerate(temperatures):
            # пока текущая температура больше чем температура в стеке
            # вынимаем удаляем из стека элементы и
            # вычисляем для них ответ
            while len(stack) > 0 and stack[-1][1] < temperature:
                idx, _ = stack.pop()
                result[idx] = i - idx
            stack.append([i, temperature])
        return result