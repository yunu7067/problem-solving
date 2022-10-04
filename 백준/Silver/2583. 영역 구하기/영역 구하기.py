from collections import defaultdict, deque
import sys

input = sys.stdin.readline

# N: row, M: Column
N, M, K = map(int, input().rstrip().split())
board = [[False] * M for _ in range(N)]
# initialize
for _ in range(K):
    sc, sr, ec, er = map(int, input().rstrip().split())
    for _r in range(sr, er):
        for _c in range(sc, ec):
            board[_r][_c] = True

areas = []
area = 0
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
Q = deque([])
for _r in range(N):
    for _c in range(M):
        if not board[_r][_c]:
            area += 1
            Q.append([_r, _c])
            board[_r][_c] = True
        while Q:
            cr, cc = Q.popleft()
            for dr, dc in d:
                nr, nc = cr + dr, cc + dc
                if not (0 <= nr < N and 0 <= nc < M):
                    continue
                if not board[nr][nc]:
                    Q.append([nr, nc])
                    board[nr][nc] = True
                    area += 1

        if area != 0:
            areas.append(area)
            area = 0

areas.sort()

print(len(areas))
print(*areas)