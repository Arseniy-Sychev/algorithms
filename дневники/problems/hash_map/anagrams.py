'''
АНАГРАМЫ

Даны две сстроки s и t, нужно вернуть True если t является аннограмой s
и False в противном случае. (слова состоящии из одинаковых букв, но в разном порядке)

Пример
s = anagram
t = nagaram -> True

Вся программа будет работать 
Время O(n) Память O(1) так как размер массивов не может быть больше 26(кол-во букв)
'''
class Solution():
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0 for i in range(26)]
        for char in s:
            count[ord(char) - ord("a")] += 1
        for char in t:
            count[ord(char) - ord("a")] -= 1
        
        return count == [0 for i in range(26)]
    