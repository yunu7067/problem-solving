from typing import List

class Solution:
    def 연습문제2(self, arr: List, N: int):
        arr_set = set(arr)

        for num in arr:
            remainder = 100 - num
            if remainder in arr_set and remainder != 50:
                return 1

        return 0
