'''
ОБЩИЙ ПРЕФИКС

You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i]
 is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains 
all integers from 1 to n exactly once.
'''
from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
            freq = [0 for i in range(len(A) + 1)]
            result = []
            common = 0
            for idx in range(len(A)):
                freq[A[idx]] += 1
                freq[B[idx]] += 1
                if A[idx] == B[idx]:
                    common += 1
                    result.append(common)
                    continue
                if A[idx] != B[idx] and freq[A[idx]] == 2:
                    common += 1
                if A[idx] != B[idx] and freq[B[idx]] == 2:
                    common += 1
                result.append(common)
                
            return result