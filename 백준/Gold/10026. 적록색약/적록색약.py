from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
board = [[s for s in input().rstrip()] for i in range(N)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
Q = deque()
diff = []

# 정상
visited = [[False] * N for _ in range(N)]
count = {"R": 0, "G": 0, "B": 0}

for _r in range(N):
    for _c in range(N):
        if not visited[_r][_c]:
            color = board[_r][_c]
            Q.append([_r, _c, color])
            visited[_r][_c] = True
            count[color] += 1

        while Q:
            cr, cc, ccolor = Q.popleft()
            for dr, dc in d:
                nr, nc = cr + dr, cc + dc
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if not visited[nr][nc]:
                    if ccolor == board[nr][nc]:
                        Q.append([nr, nc, ccolor])
                        visited[nr][nc] = True


diff.append(count["R"] + count["G"] + count["B"])

# 적록
visited = [[False] * N for _ in range(N)]
count = {"R": 0, "G": 0, "B": 0}

for _r in range(N):
    for _c in range(N):
        if not visited[_r][_c]:
            color = board[_r][_c]
            Q.append([_r, _c, color])
            visited[_r][_c] = True
            count[color] += 1

        while Q:
            cr, cc, ccolor = Q.popleft()
            for dr, dc in d:
                nr, nc = cr + dr, cc + dc
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if not visited[nr][nc]:
                    if (
                        (ccolor == board[nr][nc])
                        or (ccolor == "R" and board[nr][nc] == "G")
                        or (ccolor == "G" and board[nr][nc] == "R")
                    ):
                        Q.append([nr, nc, ccolor])
                        visited[nr][nc] = True


diff.append(count["R"] + count["G"] + count["B"])

print(*diff)