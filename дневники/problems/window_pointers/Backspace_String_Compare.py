'''
Given two strings s and t, return true if they are equal when both are
 typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
'''

class Solution:
    def findNextNonSkip(self, s: str, i: int) -> int:
        skipCount = 0
        while i >= 0 and (skipCount > 0 or s[i] == '#'):
            if s[i] == '#':
                skipCount += 1
                i -= 1
                continue
            skipCount -= 1
            i -= 1
        return i

    def backspaceCompare(self, s: str, t: str) -> bool:
        p1, p2 = len(s), len(t)
        while p1 > 0 and p2 > 0:
            p1 = self.findNextNonSkip(s, p1 - 1)
            p2 = self.findNextNonSkip(t, p2 - 1)
            if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
                return False
        return self.findNextNonSkip(s, p1 - 1) == self.findNextNonSkip(t, p2 - 1)
        