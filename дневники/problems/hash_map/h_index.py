'''
https://leetcode.com/problems/h-index/description/

H ИНДЕКС

Given an array of integers citations where citations[i]
 is the number of citations a researcher received for their ith paper,
   return the researcher's h-index.

According to the definition of h-index on Wikipedia: 
The h-index is defined as the maximum value of h such that the given 
researcher has published at least h papers that have each been cited at least h times.
Input: citations = [3,0,6,1,5]
Output: 3
'''
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = [0 for i in range(len(citations) + 1)]
        h = len(citations)
        cnt = 0

        for num in citations:
            count[min(num, len(citations))] += 1

        for num in reversed(count):
            cnt += num
            if cnt >= h:
                return h
            h -= 1