'''
ПОИСК ОСИ СИММЕТРИИ

даны точки на оси кординат, необходимо определить можно ли построить линию
симметриии
'''
from typing import List

class Solution():
    def isReflected(self, points: List[List[int]]) -> bool:
        max_point = max(x for x, y in points)
        min_point = min(x for x, y in points)
        point_set = {(x, y) for x, y in points}

        for x, y in points:
            if (max_point + min_point - x, y) not in point_set:
                return False
        return True
