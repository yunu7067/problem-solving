from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]
Q = deque([])

street_num = 0
street_dict = defaultdict(int)

for r in range(N):
    for c in range(N):
        if board[r][c] == 1 and not visited[r][c]:
            street_num += 1
            Q.append((r, c, street_num))
            visited[r][c] = True
            street_dict[street_num] += 1

            while Q:
                cr, cc, cstnum = Q.popleft()
                for i in range(4):
                    nr, nc = cr + dr[i], cc + dc[i]
                    if not (0 <= nr < N) or not (0 <= nc < N):
                        continue
                    if board[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        street_dict[street_num] += 1
                        Q.append((nr, nc, cstnum))

print(street_num)
a = list(street_dict.values())
a.sort()
for b in a:
    print(b)