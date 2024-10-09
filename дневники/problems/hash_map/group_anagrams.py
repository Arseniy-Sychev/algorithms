'''
https://leetcode.com/problems/group-anagrams/description/

ГРУППИРОВКА АНАГРАМ

Given an array of strings strs, group the anagrams
 together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''
from typing import List
from collections import defaultdict

def group_anagrams(strs):
    def dict_count(word):
        res = [0] * 26
        for char in word:
            res[ord(char) - ord('a')] += 1
        return tuple(res)
    
    ana_map = defaultdict(list)
    
    for word in strs:
        ana_map[dict_count(word)].append(word)
    
    result = list(ana_map.values())
    return result

#альтернативное решение через сортировку не оптимальное

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            hash_map = {}

            for word in strs:
                sort_word = "".join(sorted(word))
                if sort_word not in hash_map:
                    hash_map[sort_word] = [word]
                else:
                    hash_map[sort_word].append(word)

            return list(hash_map.values())