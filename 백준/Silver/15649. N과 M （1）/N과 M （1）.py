from itertools import permutations
import sys
from typing import List

def NM(M: int, nums: List, p: List):
    if M <= 0:
        print(" ".join(map(str, p)))
        return
    for num in nums:
        next_nums, next_p = nums.copy(), p.copy()
        next_nums.remove(num)
        next_p.append(num)
        NM(M - 1, next_nums, next_p)

N, M = map(int, sys.stdin.readline().split())
nums = list(range(1, N + 1))
NM(M, nums, [])
