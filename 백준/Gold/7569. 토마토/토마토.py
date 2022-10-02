from collections import deque
import sys

input = sys.stdin.readline
M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[-1] * M for _ in range(N)] for _ in range(H)]
d = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 0, -1], [0, -1, 0], [-1, 0, 0]]
Q = deque()
for _h in range(H):
    for _r in range(N):
        for _c in range(M):
            if board[_h][_r][_c] == 1:
                Q.append((_h, _r, _c, 0))
                visited[_h][_r][_c] = 0
            elif board[_h][_r][_c] == -1:
                visited[_h][_r][_c] = 0

while Q:
    ch, cr, cc, cday = Q.popleft()

    for dh, dr, dc in d:
        nh, nr, nc, nday = ch + dh, cr + dr, cc + dc, cday + 1
        if not (0 <= nh < H and 0 <= nr < N and 0 <= nc < M):
            continue
        if visited[nh][nr][nc] == -1:
            Q.append((nh, nr, nc, nday))
            visited[nh][nr][nc] = nday


max_day = -1
for _h in range(H):
    for _r in range(N):
        for _c in range(M):
            if visited[_h][_r][_c] == -1:
                print(-1)
                exit()
            max_day = max(max_day, visited[_h][_r][_c])
print(max_day)