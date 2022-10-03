from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
Q = deque([[0, 0]])
visited = [[-1] * M for _ in range(N)]
visited[0][0] = 1
Q2 = deque()  # 만난 1을 넣는 큐

while Q:
    cr, cc = Q.popleft()
    for dr, dc in d:
        nr, nc = cr + dr, cc + dc
        if not (0 <= nr < N and 0 <= nc < M):
            continue
        if visited[nr][nc] == -1:
            if board[nr][nc] == 0:
                Q.append([nr, nc])
            else:
                Q2.append([nr, nc])
            visited[nr][nc] = visited[cr][cc] + 1

for pos in Q2:
    Q3 = deque([pos])
    while Q3:
        cr, cc = Q3.popleft()
        for dr, dc in d:
            nr, nc = cr + dr, cc + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if (
                visited[nr][nc] == -1 or visited[cr][cc] + 1 < visited[nr][nc]
            ) and board[nr][nc] == 0:
                Q3.append([nr, nc])
                visited[nr][nc] = visited[cr][cc] + 1


print(visited[N - 1][M - 1])