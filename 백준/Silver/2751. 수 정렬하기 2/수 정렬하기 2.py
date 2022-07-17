from itertools import combinations
import sys
from typing import List, Tuple


N = int(sys.stdin.readline().rstrip())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
temp = [None] * N


def merge(st: int, en: int):
    mid: int = int((st + en) / 2)
    left_i = st
    right_i = mid
    for i in range(st, en):
        if right_i == en:
            temp[i] = nums[left_i]
            left_i += 1
        elif left_i == mid:
            temp[i] = nums[right_i]
            right_i += 1
        elif nums[left_i] <= nums[right_i]:
            temp[i] = nums[left_i]
            left_i += 1
        else:
            temp[i] = nums[right_i]
            right_i += 1
    for i in range(st, en):
        nums[i] = temp[i]


def merge_sort(st: int, en: int):
    if st + 1 == en:
        return
    mid: int = int((st + en) / 2)
    merge_sort(st, mid)
    merge_sort(mid, en)
    merge(st, en)


merge_sort(0, N)
print(" ".join(map(str, nums)))