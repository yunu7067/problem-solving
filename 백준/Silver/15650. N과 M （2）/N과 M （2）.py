from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(range(1, N + 1))
combs = list(combinations(nums, M))
for comb in combs:
    print(" ".join(map(str,comb)))
