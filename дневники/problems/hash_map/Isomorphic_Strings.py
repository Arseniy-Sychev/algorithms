'''
https://leetcode.com/problems/isomorphic-strings/description/

ИЗОМОРФНЫЕ СТРОКИ

Паттерн maзping
Даны две строки s и t. Определите изоморфны ли они.
Две строки изоморфны, если символы в s можно заменить, что бы получить t
Пример:
s = abacaba
t = totxtot -> изоморфны (a=t, b=o, c=x)

s = foo
t = bar -> не изоморфны (f=b, o=a/r)

Решение через мэпинг двух строк, ключ буквы первой строки, 
значение буквы второй строки
Можно сделать через массивы и он будет работать быстрее, 
но этот способ не интуитивен и не универсален.
нужно что бы у нас было ограничение на малые английские буквы и записываем сопоставления через ord.

Вся программа будет работать 
Время O(n) Память O(n)
'''
class Solution():
    def is_isomorphic(self, s: str, t: str) -> bool:
        sDict, tDict = {}, {}

        for i in range(len(s)):
            if s[i] in sDict and sDict[s[i]] != t[i]:
                return False
            if t[i] in tDict and tDict[t[i]] != s[i]:
                return False
            sDict[s[i]] = t[i]
            tDict[t[i]] = s[i]
        return True