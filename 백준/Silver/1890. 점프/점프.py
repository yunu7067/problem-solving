import sys

input = sys.stdin.readline
N = int(input())

B = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]
DP[0][0] = 1

for r in range(N):
    for c in range(N):
        if DP[r][c] == 0 or B[r][c] == 0:
            continue
        if r + B[r][c] < N:
            DP[r + B[r][c]][c] += DP[r][c]
        if c + B[r][c] < N:
            DP[r][c + B[r][c]] += DP[r][c]

print(DP[N - 1][N - 1])