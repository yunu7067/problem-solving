from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline
d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    island_count = 0
    Q = deque()
    for _r in range(h):
        for _c in range(w):
            if board[_r][_c] == 1 and not visited[_r][_c]:
                island_count += 1
                visited[_r][_c] = True
                Q.append([_r, _c])
            while Q:
                cr, cc = Q.popleft()

                for nd in d:
                    nr, nc = cr + nd[0], cc + nd[1]
                    if not (0 <= nr < h) or not (0 <= nc < w):
                        continue
                    if board[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        Q.append([nr, nc])
    print(island_count)