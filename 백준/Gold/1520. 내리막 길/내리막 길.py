import sys

input = sys.stdin.readline
M, N = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(M)]
DP = [[-1] * N for _ in range(M)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def dfs(cr, cc):
    if cr == M - 1 and cc == N - 1:
        return 1
    DP[cr][cc] = 0
    for dr, dc in d:
        nr, nc = cr + dr, cc + dc
        if not (0 <= nr < M and 0 <= nc < N):
            continue
        if map[nr][nc] < map[cr][cc]:
            if DP[nr][nc] == -1:
                DP[cr][cc] += dfs(nr, nc)
            else:
                DP[cr][cc] += DP[nr][nc]
    return DP[cr][cc]

print(dfs(0, 0))