# from collections import defaultdict, deque
from heapq import heappop, heappush
import sys
from typing import List

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
pedia = {}


for idx in range(1, N + 1):
    name = input().rstrip()
    pedia[name] = idx
    pedia[str(idx)] = name

for _ in range(M):
    q = input().rstrip()
    print(pedia[q])