from collections import deque
import sys
from typing import List

input = sys.stdin.readline

N = int(input())
B = []
pos = deque([])
for _r in range(N):
    _row = list(map(int, input().rstrip().split()))
    for (_c, _v) in enumerate(_row):
        if _v == 9:
            pos.append([_r, _c])
            _row[_c] = 0
    B.append(_row)


def bfs(n: int, start_pos: List[int], shark_size: int, board: List[List[int]]):
    d = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    visited = [[-1] * n for _ in range(N)]
    r, c = start_pos
    visited[r][c] = 0
    Q = deque([start_pos])
    min_move = sys.maxsize
    tl_pos = None

    while Q:
        cr, cc = Q.popleft()
        for dr, dc in d:
            nr, nc, ntime = cr + dr, cc + dc, visited[cr][cc] + 1
            if not (0 <= nr < N and 0 <= nc < N) or ntime > min_move:
                continue
            if visited[nr][nc] == -1 and board[nr][nc] <= shark_size:
                if 0 < board[nr][nc] < shark_size:
                    if min_move == sys.maxsize:
                        min_move = ntime
                        tl_pos = [nr, nc]
                    else:
                        if tl_pos[0] > nr:
                            tl_pos = [nr, nc]
                        elif tl_pos[0] == nr and tl_pos[1] > nc:
                            tl_pos = [nr, nc]
                Q.append([nr, nc])
                visited[nr][nc] = ntime
    if min_move == sys.maxsize:
        return (0, None)
    else:
        return (min_move, tl_pos)


size, time, eat = 2, 0, 0
while pos:
    cur_pos = pos.popleft()
    spend_time, next_pos = bfs(N, cur_pos, size, B)
    if next_pos == None:
        break
    pos.append(next_pos)
    B[next_pos[0]][next_pos[1]] = 0
    time += spend_time
    eat += 1
    if eat == size:
        eat = 0
        size += 1

print(time)