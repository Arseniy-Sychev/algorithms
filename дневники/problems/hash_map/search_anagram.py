'''
ПОИСК АНАГРАМ В СТРОКЕ

Given two strings s and p, return an array of all 
the start indices of p's anagrams in s. You may return the answer in any order.

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

Input: s = "abab", p = "ab"
Output: [0,1,2]

'''
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        # Подсчитываем частоты символов для p
        p_count = [0] * 26
        s_count = [0] * 26
        result = []
        a_ord = ord('a')
        
        # Заполняем частоты для строки p и первой подстроки s
        for i in range(len(p)):
            p_count[ord(p[i]) - a_ord] += 1
            s_count[ord(s[i]) - a_ord] += 1
        
        # Сравниваем окна, начиная с первого
        for i in range(1, len(s) - len(p) + 1):
                # Сдвиг окна: обновляем частоту символа
            s_count[ord(s[i - 1]) - a_ord] -= 1
            s_count[ord(s[i + len(p) - 1]) - a_ord] += 1
            
            # Если частоты совпадают, добавляем начальную позицию подстроки
            if s_count == p_count:
                result.append(i)

        return result