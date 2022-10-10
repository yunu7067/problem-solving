from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [[s for s in input().rstrip()] for _ in range(R)]
visited = [[-1] * C for _ in range(R)]
area, area_idx = {}, 1
Q = deque()
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for r in range(R):
    for c in range(C):
        if board[r][c] != "#" and visited[r][c] == -1:
            Q.append([r, c])
            visited[r][c] = area_idx
            area[area_idx] = {"v": 0, "o": 0}
            area_idx += 1
            if board[r][c] != ".":
                area[visited[r][c]][board[r][c]] += 1

        while Q:
            cr, cc = Q.popleft()
            for dr, dc in d:
                nr, nc = cr + dr, cc + dc
                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                if board[nr][nc] != "#" and visited[nr][nc] == -1:
                    Q.append([nr, nc])
                    visited[nr][nc] = visited[r][c]
                    if board[nr][nc] != ".":
                        area[visited[r][c]][board[nr][nc]] += 1

sheep = 0
wolf = 0
for count in area.values():
    if count["o"] > count["v"]:
        sheep += count["o"]
    else:
        wolf += count["v"]

print(sheep, wolf)