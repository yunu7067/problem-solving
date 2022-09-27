from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
piece_count = 0
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
t = 0
while True:
    visited = [[False] * M for _ in range(N)]
    Q = deque()
    exist = False
    for _r in range(N):
        for _c in range(M):
            if board[_r][_c] != 0 and not visited[_r][_c]:
                exist = True
                Q.append([_r, _c])
                visited[_r][_c] = True
                piece_count += 1
                if piece_count > 1:
                    print(t)
                    exit()

            while Q:
                cr, cc = Q.popleft()
                ocean_count = 0
                for dd in d:
                    nr, nc = cr + dd[0], cc + dd[1]
                    if not (0 <= nr < N and 0 <= nc < M):
                        continue
                    if board[nr][nc] == 0 and not visited[nr][nc]:
                        ocean_count += 1
                    if board[nr][nc] != 0 and not visited[nr][nc]:
                        Q.append([nr, nc])
                        visited[nr][nc] = True

                board[cr][cc] = max(0, board[cr][cc] - ocean_count)

    if not exist:
        print(0)
        exit()
    piece_count = 0
    t += 1