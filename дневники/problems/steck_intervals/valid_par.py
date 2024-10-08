'''
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()[]{}"

Output: true

Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        if len(s) <= 1 or s[0] in "}])":
            return False

        for idx in range(len(s)):
            if s[idx] == "(" or s[idx] == "{" or s[idx] == "[":
                result.append(s[idx])
            elif len(result) != 0 and ((s[idx] == ")" and result[-1] == "(") or (s[idx] == "}" and result[-1] == "{") or (s[idx] == "]" and result[-1] == "[")):
                result.pop(-1)
            else:
                return False

        if len(result) != 0:
            return False
        else:
            return True
        

class Solution:
    # time: O(n)
    # mem: O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'{':'}', '(':')', '[':']'}
        for char in s:
            if char in pairs:
                # если скобка открытая - просто добавляем в стек
                stack.append(char)
                continue

            # перед нами закрывающаяся скобка, но стек пуст
            if len(stack) == 0:
                return False
            # удаляем последний элемент из стека
            lastChar = stack.pop()
            # проверяем что последний элемент в стеке и текущий образуют пару
            # если пару не образуют, то вернем False
            if pairs[lastChar] != char:
                return False  
        return len(stack) == 0