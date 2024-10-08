'''
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Input: s = "a)b(c)d"
Output: "ab(c)d"

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
'''

class Solution:
    # time: O(n)
    # mem: O(n) - в python лучше не получится т к нужна
    # обязательно новая строка для ответа (строки не меняются)
    def minRemoveToMakeValid(self, s: str) -> str:
        # в python строки не изменяемы поэтому нужно сделать список из символов
        # который уже можно менять
        result = list(s)
        stack = [] # храним индексы для символа (
        for i in range(len(result)):
            char = result[i]
            if char == '(':
                stack.append(i)
            elif char == ')' and len(stack) == 0:
                # скобка ")" лишняя и должна быть удалена
                result[i] = ''
            elif char == ')' and len(stack) != 0:
                stack.pop()

        # проходимся по всем лишним скобкам "(" и удаляем их
        for i in stack:
            result[i] = ""

        # делаем строку из элементов списка 
        return "".join(result)