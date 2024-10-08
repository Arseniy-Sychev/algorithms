'''
You are given an array representing a row of seats where seats[i] = 1 represents
a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and
the closest person to him is maximized. 

Return that maximum distance to the closest person.

Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
'''
from typing import List
class Solution:
    # time: O(n)
    # mem:  O(1)
    def maxDistToClosest(self, seats: List[int]) -> int:
        l = 0
        r = 0
        result = 0
        while l < len(seats):
            # before
            # l
            # 1 1 1 1 0 0 1 1
            # r

            # бежим правым указателем пока в интервале [l, r]
            # находятся все последовательные числа
            while r + 1 < len(seats) and seats[r] == seats[r + 1]:
                r += 1
            # after
            # l
            # 1 1 1 1 0 0 1 1
            #       r

            # обновляем ответ только если в палавающем окне были 0-ли
            if seats[r] == 0:
                # если 0 прижат к стенке слева или справа, т. е.
                # 1 0 0 0
                #   l   r

                # 0 0 0 1
                # l   r
                # то свободных мест будет r - l + 1 т к посадим в самый край
                if l == 0 or r == len(seats) - 1:
                    result = max(result, r - l + 1)
                # в данном случае окно распологается между 1-ами:
                # 1 0 0 0 1
                #   l   r
                # поэтому находим число мест по формуле (r - l + 2) // 2
                else:
                    result = max(result, (r - l + 2) // 2)

            # интервалы не пересекаются, поэтому сдвигаем
            # на r + 1 - именно отсюда будет начинаться
            # следующий интервал
            l = r + 1
            r = r + 1
        return result

