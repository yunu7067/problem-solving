from collections import defaultdict, deque
import sys
from typing import List

input = sys.stdin.readline
N = int(input())
board = []
nums = set()

for _ in range(N):
    _a = list(map(int, input().rstrip().split()))
    board.append(_a)
    nums.update(_a)
nums = list(nums)
nums.sort()


d = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def calc(B: List[List[int]], target: int):
    visited = [[False] * N for _ in range(N)]
    Q = deque()
    cur_count = 0

    for _r in range(N):
        for _c in range(N):
            if not visited[_r][_c]:
                if B[_r][_c] > target:
                    Q.append([_r, _c])
                    cur_count += 1
                visited[_r][_c] = True
            while Q:
                cr, cc = Q.popleft()
                for dr, dc in d:
                    nr, nc = cr + dr, cc + dc
                    if not (0 <= nr < N and 0 <= nc < N):
                        continue
                    if not visited[nr][nc] and B[nr][nc] > target:
                        Q.append([nr, nc])
                        visited[nr][nc] = True

    return cur_count


max_count = 1

for level in nums:
    max_count = max(max_count, calc(board, level))
print(max_count)