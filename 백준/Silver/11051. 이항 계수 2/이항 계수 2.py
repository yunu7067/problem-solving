import sys

N, M = map(int, sys.stdin.readline().split())
D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for n in range(1, N + 1):
    D[n][0] = D[n][n] = 1
    for k in range(1, n):
        D[n][k] = (D[n - 1][k - 1] + D[n - 1][k]) % 10_007

print(D[N][M])