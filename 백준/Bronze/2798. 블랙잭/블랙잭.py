from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
combs = combinations(nums, 3)
sim_sum = 0

for comb in combs:
    cur_sum = sum(comb)
    if cur_sum == M:
        print(M)
        exit(0)
    elif sim_sum < cur_sum <= M:
        sim_sum = cur_sum

print(sim_sum)
