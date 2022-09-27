from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
empty_pos = []
virus_pos = []
dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]

for _r in range(N):
    _temp = list(map(int, input().split()))
    board.append(_temp)
    for _c, _v in enumerate(_temp):
        if _v == 0:
            empty_pos.append([_r, _c])
        elif _v == 2:
            virus_pos.append([_r, _c])

max_safe_count = 0
for comb in combinations(empty_pos, 3):
    visited = [[False] * M for _ in range(N)]
    for v in virus_pos:
        if not visited[v[0]][v[1]]:
            visited[v[0]][v[1]] = True
            Q = deque([v])
            while Q:
                cr, cc = Q.popleft()
                for i in range(4):
                    nr, nc = cr + dr[i], cc + dc[i]
                    if not (0 <= nr < N) or not (0 <= nc < M):
                        continue
                    if (
                        [nr, nc] != comb[0]
                        and [nr, nc] != comb[1]
                        and [nr, nc] != comb[2]
                        and board[nr][nc] == 0
                        and not visited[nr][nc]
                    ):
                        visited[nr][nc] = True
                        Q.append([nr, nc])
    cur_safe_count = 0

    for _r in range(N):
        for _c in range(M):
            if (
                [_r, _c] != comb[0]
                and [_r, _c] != comb[1]
                and [_r, _c] != comb[2]
                and board[_r][_c] == 0
                and not visited[_r][_c]
            ):
                cur_safe_count += 1
    max_safe_count = max(max_safe_count, cur_safe_count)

print(max_safe_count)