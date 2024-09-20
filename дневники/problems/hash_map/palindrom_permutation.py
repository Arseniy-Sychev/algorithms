'''
ПЕРЕСТАНОВКА БУКВ

Дана строка s, верните True если перестановка строки может 
образовать палиндром

code - False
aab - True
carerac - True
'''

class Solution():
    def canPermutePalindrom(self, s: str) -> bool:
        hash_map = {}
        count = 0
        for letter in s:
            hash_map[letter] = hash_map.get(letter, 0) + 1
        
        for element in hash_map:
            if hash_map[element] % 2 != 0:
                count += 1
            if count > 1:
                return False
        return True
    